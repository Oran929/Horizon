---
layout: default
title: "AI行业热点: 2026-07-25 (ZH)"
date: 2026-07-25
lang: zh
briefing: ainews
---

> 从 64 条内容中筛选出 9 条重要资讯。

---

1. [SGLang v0.5.16：DSpark 推测解码与 Inkling 支持](#item-1) ⭐️ 9.0/10
2. [Anthropic 发布 Claude Opus 5，性能媲美 Fable 5 价格减半](#item-2) ⭐️ 9.0/10
3. [vLLM v0.26.0 新增 Inkling 模型家族与 DeepSeek-V4 优化](#item-3) ⭐️ 8.0/10
4. [开放权重 AI 正经历类似 Kubernetes 的崛起](#item-4) ⭐️ 8.0/10
5. [Tile 安全漏洞使跟踪变得轻而易举](#item-5) ⭐️ 8.0/10
6. [Ruff v0.16.0 将默认 lint 规则从 59 条扩展到 413 条](#item-6) ⭐️ 8.0/10
7. [Claude Opus 5 展现出最佳提示注入防御能力](#item-7) ⭐️ 8.0/10
8. [黄仁勋谈中国 AI、特朗普与万亿 Agent 时代](#item-8) ⭐️ 8.0/10
9. [黄仁勋入驻 X，联署 25 家公司力挺开源 AI](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SGLang v0.5.16：DSpark 推测解码与 Inkling 支持](https://github.com/sgl-project/sglang/releases/tag/v0.5.16) ⭐️ 9.0/10

SGLang v0.5.16 引入了 DSpark，一种基于置信度的推测解码算法，在 DeepSeek-V4-Pro 上达到 383.7 tok/s，并增加了对 Inkling 的支持，这是一个拥有 975B 参数、支持 1M token 上下文的多模态 MoE 模型。该版本还包括来自 169 位贡献者的 574 个 PR，新增了 LongCat 2.0 等模型，并对 Blackwell GPU 上的线性注意力进行了性能优化。 DSpark 基于置信度的验证窗口显著提升了推测解码效率，创下了 LLM 推理速度的新纪录。Inkling 以开放权重形式发布，拥有 41B 活跃参数和可控思考能力，推动了大规模多模态 AI 的前沿发展，使先进能力对社区更加可及。 DSpark 使用半自回归块草稿和基于草稿置信度的可变验证长度，通过 --speculative-algorithm DSPARK 和 SGLANG_RAGGED_VERIFY_MODE=compact 启用。Inkling 混合了滑动窗口、全注意力和 Mamba2 线性注意力，配备 NVFP4 MoE 和可选的视觉/音频塔，在 Blackwell 上达到高达 71.7k tok/s 的输入速度和 171.0 tok/s 的每用户解码速度。

github · Qiaolin-Yu · 7月25日 00:13

**背景**: 推测解码通过使用小型草稿模型提出 token，再由大型目标模型并行验证，从而加速 LLM 推理。SGLang 是一个高性能推理引擎，支持 EAGLE-3 和 MTP 等多种推测算法。DSpark 通过根据草稿模型的置信度自适应调整验证窗口大小，减少了计算浪费，改进了固定长度草稿的方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2607.05147">[2607.05147] DSpark: Confidence-Scheduled Speculative ...</a></li>
<li><a href="https://www.lmsys.org/blog/2026-07-06-dspark-sglang">DSpark in SGLang: Speculative Decoding with Confidence-Driven ...</a></li>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling: Our Open-Weights Model - Thinking Machines Lab</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#speculative decoding`, `#SGLang`, `#MoE`, `#high-performance computing`

---

<a id="item-2"></a>
## [Anthropic 发布 Claude Opus 5，性能媲美 Fable 5 价格减半](https://simonwillison.net/2026/Jul/24/introducing-claude-opus-5/#atom-everything) ⭐️ 9.0/10

Anthropic 于 2026 年 7 月 22 日发布了 Claude Opus 5，这是一款新的旗舰 AI 模型，其智能水平接近 Claude Fable 5，但价格仅为后者的一半，目前在 Artificial Analysis 排行榜上领先。 Claude Opus 5 以显著更低的价格提供了接近前沿的智能水平，使开发者和企业能够更经济地使用先进 AI 能力，可能重塑 AI 模型定价的竞争格局。 Claude Opus 5 的定价与 Opus 4.8 相同，并提供快速模式（价格为基本模型的两倍）。它未针对网络任务进行训练，但在发现漏洞方面有所改进，不过在漏洞利用方面仍落后于 Mythos 5。

rss · Simon Willison · 7月24日 23:48

**背景**: Anthropic 的 Claude 模型系列包括多个层级：Haiku（能力最弱）、Sonnet、Opus（能力最强），以及较新的 Mythos 和 Fable 系列。Claude Fable 5 是更强大的 Mythos 5 的公开版本，增加了安全措施。Artificial Analysis 排行榜根据多个基准测试的性能对 AI 模型进行排名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Claude_Opus">Claude Opus</a></li>
<li><a href="https://openrouter.ai/anthropic/claude-opus-5">Claude Opus 5 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://llm-stats.com/benchmarks/artificial-analysis">Artificial Analysis Leaderboard - llm-stats.com</a></li>

</ul>
</details>

**社区讨论**: 社区反响积极，有评论称“没人能在提炼 Fable 方面打败 Anthropic！”——这表明社区高度认可该模型的性价比，以及 Anthropic 将高端能力提炼到更实惠模型中的能力。

**标签**: `#AI`, `#Anthropic`, `#Claude Opus 5`, `#machine learning`, `#model release`

---

<a id="item-3"></a>
## [vLLM v0.26.0 新增 Inkling 模型家族与 DeepSeek-V4 优化](https://github.com/vllm-project/vllm/releases/tag/v0.26.0) ⭐️ 8.0/10

vLLM v0.26.0 引入了 Inkling 模型家族的完整支持栈、跨厂商的 DeepSeek-V4 性能优化、fp32 lm_head 支持以及每个 KV-cache 组可选的灵活注意力后端。 此版本显著提升了 LLM 推理的效率和灵活性，支持 Inkling 和 DeepSeek-V4 等前沿模型，同时在 NVIDIA、AMD 和 Intel 硬件上均实现了性能改进。 该版本包含来自 212 位贡献者的 411 次提交，包括针对 DeepSeek-V4 的专用路由内核（端到端 TPOT 提升 2.94%）、Hopper FA4 相对注意力机制以及 Inkling 家族的 ModelOpt NVFP4 量化支持。

github · khluu · 7月25日 10:38

**背景**: vLLM 是一个开源的高吞吐量 LLM 推理引擎。Inkling 模型家族来自 Thinking Machines Lab，是一种多模态 Mamba 混合专家架构。DeepSeek-V4 是一个需要高效推理优化的大型语言模型。Flash Attention 4 (FA4) 是最新的注意力算法，针对 Hopper GPU 进行了优化。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.linkedin.com/posts/vllm-project_inkling-our-open-weights-model-activity-7483227870585311232-81uL">Thinking Machines Lab Releases TML Inkling 1T-Parameter Model</a></li>
<li><a href="https://build.nvidia.com/thinkingmachines/inkling/modelcard">inkling Model by Thinkingmachines | NVIDIA NIM</a></li>
<li><a href="https://arxiv.org/html/2603.05451v1">FlashAttention-4: Algorithm and Kernel Pipelining Co-Design for Asymmetric Hardware Scaling</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#GPU optimization`, `#model serving`, `#open source`

---

<a id="item-4"></a>
## [开放权重 AI 正经历类似 Kubernetes 的崛起](https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/) ⭐️ 8.0/10

Tobi Knaup 认为，开放权重 AI 模型正沿着与 Kubernetes 相同的轨迹发展，成为 AI 基础设施的事实标准。这一转变对监管、定价和协作开发具有深远影响。 如果开放权重 AI 成为标准，它可能使 AI 访问民主化、降低成本并促进创新，类似于 Kubernetes 改变云计算的方式。这也引发了关于按来源禁止模型的可行性以及 AI 推理经济学的讨论。 这个类比并不完美：与 Kubernetes 不同，开放权重模型不允许检查或修改源代码，改进也无法回流到共享的上游。然而，社区讨论指出，开放权重模型为推理成本提供了基准，使定价更加合理。

hackernews · tknaup · 7月25日 14:49 · [社区讨论](https://news.ycombinator.com/item?id=49048034)

**背景**: 开放权重 AI 模型发布其训练后的权重，允许用户运行和微调，但并非完全开源，因为训练数据和代码通常不公开。Kubernetes 之所以成为容器编排的标准，是因为它开源、社区驱动，并允许众多公司贡献代码。这个类比表明，开放权重 AI 可能类似地成为 AI 应用的默认基础设施层。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://tobi.knaup.me/2026-07-25-open-weight-ai-is-having-its-kubernetes-moment/">Open-weight AI is having its Kubernetes moment . | Tobi Knaup</a></li>
<li><a href="https://sourcefeed.dev/a/open-weight-ais-kubernetes-moment-is-missing-its-cncf">Open-Weight AI's Kubernetes Moment Is Missing Its... — SourceFeed</a></li>
<li><a href="https://artificialanalysis.ai/models">Comparison of AI Models across Intelligence, Performance, and Price</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了禁止中国模型的可行性，有人指出权重只是数字，无法分配原产国。其他人讨论了 token 经济学，指出开放权重模型提供了成本基准，并希望有类似 Linux 的协作模型开发。

**标签**: `#open-weight AI`, `#Kubernetes`, `#AI regulation`, `#model economics`, `#open source`

---

<a id="item-5"></a>
## [Tile 安全漏洞使跟踪变得轻而易举](https://blog.adafruit.com/2026/03/05/tiles-security-is-so-bad-its-a-feature-for-stalkers/) ⭐️ 8.0/10

一篇学术论文揭示，Tile 追踪器缺乏位置不可区分性，广播未加密的静态 MAC 地址和唯一 ID，使得技术娴熟的跟踪者可以轻松追踪用户。这与苹果和谷歌通过加密实现位置不可区分性的方法形成对比。 Tile 追踪系统的这一根本性缺陷带来了严重的隐私风险，尤其对弱势群体而言，并凸显了物联网追踪行业需要更强安全标准的必要性。这项研究可能迫使 Tile 采用类似苹果和谷歌的加密方法。 该论文（arXiv:2510.00350）指出，Tile 广播未加密的静态 MAC 地址和唯一 ID，使得将标签与其所有者的位置历史关联变得轻而易举。相比之下，苹果和谷歌使用嵌入在 BLE 广告中的公钥对位置信息进行端到端加密。

hackernews · sambellll · 7月25日 18:18 · [社区讨论](https://news.ycombinator.com/item?id=49050152)

**背景**: 位置不可区分性是一种隐私属性，确保攻击者无法区分两个相邻位置，从而防止跟踪。Tile 追踪器是基于蓝牙的设备，用于定位丢失物品，但其缺乏加密使用户面临被跟踪的风险。苹果和谷歌联合制定了行业规范以应对不必要的跟踪，其中包括加密的位置广播。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/tile-tracking-tags-can-be-exploited-by-tech-savvy-stalkers-researchers-say/">Tile Tracking Tags Can Be Exploited by Tech-Savvy Stalkers, Researchers Say | WIRED</a></li>
<li><a href="https://www.malwarebytes.com/blog/news/2025/09/tile-trackers-plagued-by-weak-security-researchers-warn">Tile trackers plagued by weak security, researchers warn | Malwarebytes</a></li>
<li><a href="https://www.apple.com/newsroom/2023/05/apple-google-partner-on-an-industry-specification-to-address-unwanted-tracking/">Apple, Google partner on an industry specification to address ...</a></li>

</ul>
</details>

**社区讨论**: 论文的最后一位作者 mspecter 加入了讨论并回答问题。一些评论者对存在廉价专用跟踪设备的情况下实际威胁提出质疑，而另一些人则赞赏与苹果和谷歌加密系统的技术对比。

**标签**: `#security`, `#privacy`, `#IoT`, `#tracking`, `#research`

---

<a id="item-6"></a>
## [Ruff v0.16.0 将默认 lint 规则从 59 条扩展到 413 条](https://simonwillison.net/2026/Jul/25/ruff/#atom-everything) ⭐️ 8.0/10

Ruff v0.16.0 于 2026 年 7 月 23 日发布，将默认 lint 规则从 59 条大幅增加到 413 条，启用了许多之前可选的规则，这些规则能够捕获语法错误和运行时错误。 这一变化意味着现有的 Python 项目无需任何配置即可自动检测数百个额外问题，显著提升了整个生态系统的代码质量。使用 Ruff 的开发者需要处理许多新的警告，但该工具的自动修复和 AI 集成使得升级变得可控。 此次更新将 Ruff 的总规则数从 708 条增加到 968 条，新的默认规则包括语法错误（例如 load-before-global-declaration）和即时运行时错误（例如 yield-in-init）的规则。作者在三个主要项目上运行了新的 Ruff，发现了数百个问题，其中 sqlite-utils 报告了 1618 个错误（1538 个已自动修复）。

rss · Simon Willison · 7月25日 22:44

**背景**: Ruff 是一个用 Rust 编写的极速 Python linter 和代码格式化工具，由 Astral（现为 OpenAI 的一部分）开发。它旨在用一个二进制文件替代 Flake8、isort 和 Black 等多个工具，提供超过 900 条内置规则。该工具因其速度和全面的规则集而在 Python 社区中被广泛采用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/astral-sh/ruff">GitHub - astral-sh/ruff: An extremely fast Python linter and code formatter, written in Rust. · GitHub</a></li>
<li><a href="https://realpython.com/ruff-python/">Ruff: A Modern Python Linter for Error-Free and Maintainable Code – Real Python</a></li>

</ul>
</details>

**标签**: `#ruff`, `#python`, `#linting`, `#tooling`, `#release`

---

<a id="item-7"></a>
## [Claude Opus 5 展现出最佳提示注入防御能力](https://simonwillison.net/2026/Jul/25/boris-cherny/#atom-everything) ⭐️ 8.0/10

Boris Cherny 宣布，根据系统卡中详述的评估和红队测试，Claude Opus 5 是 Anthropic 迄今为止最不易受提示注入攻击的模型。 提示注入是 LLM 的关键安全漏洞，因此更强的防御能力直接提升了 AI 系统的安全性和可信度，尤其对企业级部署意义重大。 该声明得到了提示注入评估和红队测试结果的支持，这些结果记录在 Claude Opus 5 系统卡的第 73 页。

rss · Simon Willison · 7月25日 00:42

**背景**: 提示注入是一种攻击方式，恶意输入会覆盖模型的指令，导致意外行为。红队测试是通过对抗性测试来发现漏洞。系统卡是详细说明模型能力、安全评估和部署决策的文件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Prompt_injection">Prompt injection</a></li>
<li><a href="https://en.wikipedia.org/wiki/Red_teaming">Red teaming</a></li>
<li><a href="https://www.anthropic.com/system-cards">Model system cards \ Anthropic</a></li>

</ul>
</details>

**标签**: `#prompt-injection`, `#anthropic`, `#claude`, `#generative-ai`, `#ai`

---

<a id="item-8"></a>
## [黄仁勋谈中国 AI、特朗普与万亿 Agent 时代](https://news.google.com/rss/articles/CBMif0FVX3lxTE1kMllJUFJ1ZE9ZX1E5OGtIMnVmNF9hejlET0NUdHFjTXlCdWtkUEMzQTBfS2tnbWVPS2E2cGtRc21qUXZYLUxVNXlLNDVEXzJSQjVaNDczWm9USkNLeG1oT05BRUlYcVFfVnVuTXlzRmRRM00waDBMRFVwUXpta1E?oc=5) ⭐️ 8.0/10

英伟达 CEO 黄仁勋表示华尔街误解了 DeepSeek，驳斥 AI 末日论为胡扯，并预测芯片需求将扩大 5 到 10 倍。 黄仁勋的评论为 AI 基础设施和市场预期提供了关键见解，直接影响投资者、AI 开发者和半导体行业。 黄仁勋特别提到了“万亿 Agent 时代”，即软件必须为大规模自主 Agent 构建，他认为这一趋势将导致芯片需求激增。

google_news · PANews · 7月25日 15:02

**背景**: DeepSeek 是一家中国 AI 公司，发布了 DeepSeek Coder 和 DeepSeek-V4 等模型。“万亿 Agent 时代”指的是未来数万亿自主 AI Agent 代表人类运作，重塑软件和工作方式。AI 末日论认为高级 AI 可能导致人类灭绝。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://m.theblockbeats.info/en/news/61483">Next-Generation Software Built for Trillion-Agent Scale - BlockBeats</a></li>
<li><a href="https://en.wikipedia.org/wiki/Existential_risk_from_artificial_intelligence">Existential risk from artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#semiconductors`, `#NVIDIA`, `#DeepSeek`, `#industry trends`

---

<a id="item-9"></a>
## [黄仁勋入驻 X，联署 25 家公司力挺开源 AI](https://news.google.com/rss/articles/CBMif0FVX3lxTE43d0l1aVI3c2Yxd0YwZE5xM2UtbDBuTFJadVdiai1LS2hxWXBtaHhXLUdfbTEzU01nV01LOURYLTFKekQ2aG51RHJBanMwNjVzMG5wUi1JbUJaTGxCWFIxaHpDX1piQnMwOGppQUtxX2dUWUpwNFltZHhnU2FaMGM?oc=5) ⭐️ 7.0/10

英伟达 CEO 黄仁勋在 X（原 Twitter）上发布了首条推文，分享了一封由包括微软和 Palantir 在内的 25 家巨头联署的公开信，力挺开源 AI 模型的重要性。 这标志着行业在开源 AI 背后形成了重要联盟，可能影响美国政策，并推动 AI 开发走向更开放、协作的方向。 该信强调开放模型能增强安全性、网络安全和创新，并呼吁采取平衡策略，同时发展前沿封闭模型和开放模型。

google_news · 新浪网 · 7月25日 05:55

**背景**: 开源 AI 模型是任何人都可以使用、修改和分发的公开系统。关于开放与封闭 AI 模型的争论日益激烈，涉及安全性、控制力和国家竞争力。黄仁勋首次在 X 上发帖，标志着行业领袖大力倡导开放模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://x.com/jensenhuang">Jensen Huang (@JensenHuang) / Posts / X</a></li>
<li><a href="https://x.com/JensenHuang/status/2080643682408321103">For my first post, I’m sharing a letter @NVIDIA signed on why ...</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#NVIDIA`, `#industry news`, `#Jensen Huang`

---