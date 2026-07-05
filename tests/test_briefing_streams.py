import asyncio
import json
from datetime import datetime, timezone
from pathlib import Path
from types import SimpleNamespace

import pytest
from pydantic import ValidationError

from src.ai.summarizer import DailySummarizer
from src.models import BriefingConfig, Config, ContentItem, SourceType, WebhookConfig
from src.orchestrator import HorizonOrchestrator
from src.services.webhook import WebhookNotifier
from src.storage.manager import StorageManager


def _run_async(coro):
    return asyncio.run(coro)


def _item() -> ContentItem:
    return ContentItem(
        id="rss:test:1",
        source_type=SourceType.RSS,
        title="Test item",
        url="https://example.com/item",
        published_at=datetime(2026, 4, 24, 12, 0, 0, tzinfo=timezone.utc),
        ai_score=8.0,
        ai_summary="Short summary",
    )


def test_briefing_slug_is_normalized_and_validated() -> None:
    assert BriefingConfig(slug="AInews").slug == "ainews"

    with pytest.raises(ValidationError):
        BriefingConfig(slug="bad slug")


def test_stream_specific_storage_filename() -> None:
    assert (
        StorageManager.daily_summary_filename("2026-04-24", "zh", "ainews")
        == "horizon-2026-04-24-ainews-zh.md"
    )
    assert (
        StorageManager.daily_summary_filename("2026-04-24", "zh")
        == "horizon-2026-04-24-zh.md"
    )


def test_orchestrator_stream_post_filename_and_title() -> None:
    orchestrator = HorizonOrchestrator.__new__(HorizonOrchestrator)
    orchestrator.config = SimpleNamespace(
        briefing=BriefingConfig(
            slug="economy",
            title_zh="金融市场摘要",
            title_en="Financial Market Briefing",
        )
    )

    assert (
        orchestrator._post_filename("2026-04-24", "zh")
        == "2026-04-24-economy-summary-zh.md"
    )
    assert (
        orchestrator._post_title("2026-04-24", "zh")
        == "金融市场摘要: 2026-04-24 (ZH)"
    )


def test_summary_uses_briefing_title() -> None:
    summary = _run_async(
        DailySummarizer().generate_summary(
            [_item()],
            "2026-04-24",
            10,
            language="zh",
            title="AI行业热点",
        )
    )

    assert summary.startswith("# AI行业热点 - 2026-04-24")


def test_webhook_uses_briefing_title_and_slug(monkeypatch) -> None:
    monkeypatch.setenv("TEST_AINEWS_URL", "https://example.com/webhook")
    notifier = WebhookNotifier(
        WebhookConfig(
            enabled=True,
            url_env="TEST_AINEWS_URL",
            delivery="summary_and_items",
            platform="feishu",
            layout="collapsible",
        ),
        briefing=BriefingConfig(slug="ainews", title_zh="AI行业热点"),
    )

    messages = notifier.build_daily_summary_messages(
        summary="# AI行业热点",
        important_items=[_item()],
        all_items_count=10,
        date="2026-04-24",
        lang="zh",
        summarizer=DailySummarizer(),
    )

    assert messages[0]["message_title"] == "AI行业热点 2026-04-24"
    assert messages[0]["briefing_slug"] == "ainews"
    assert messages[0]["briefing_title"] == "AI行业热点"
    body = messages[0]["_request_body_override"]
    assert body["card"]["header"]["title"]["content"] == "AI行业热点 2026-04-24"


def test_new_github_configs_load_and_route_to_separate_webhooks() -> None:
    ainews = Config.model_validate(
        json.loads(Path("data/config.github.ainews.json").read_text(encoding="utf-8"))
    )
    economy = Config.model_validate(
        json.loads(Path("data/config.github.economy.json").read_text(encoding="utf-8"))
    )

    assert ainews.briefing and ainews.briefing.slug == "ainews"
    assert economy.briefing and economy.briefing.slug == "economy"
    assert ainews.webhook and ainews.webhook.url_env == "HORIZON_AINEWS_URL"
    assert economy.webhook and economy.webhook.url_env == "HORIZON_ECONOMY_URL"
    assert "semiconductors" not in ainews.filtering.category_groups["ai"].categories
    assert "semiconductors" in economy.filtering.category_groups["finance"].categories


def test_stream_webhook_envs_are_independent(monkeypatch) -> None:
    monkeypatch.setenv("HORIZON_AINEWS_URL", "https://example.com/ai")
    monkeypatch.setenv("HORIZON_ECONOMY_URL", "https://example.com/economy")

    ai_notifier = WebhookNotifier(
        WebhookConfig(enabled=True, url_env="HORIZON_AINEWS_URL")
    )
    economy_notifier = WebhookNotifier(
        WebhookConfig(enabled=True, url_env="HORIZON_ECONOMY_URL")
    )

    assert ai_notifier.url == "https://example.com/ai"
    assert economy_notifier.url == "https://example.com/economy"
