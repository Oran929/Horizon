---
layout: default
title: "AI行业热点: 2026-07-15 (ZH)"
date: 2026-07-15
lang: zh
briefing: ainews
---

> 从 87 条内容中筛选出 9 条重要资讯。

---

1. [Hugging Face Transformers v5.14.0 加入 975B 参数的 Inkling 模型](#item-1) ⭐️ 9.0/10
2. [Stripe 与 Advent 联合收购 PayPal，交易额 530 亿美元](#item-2) ⭐️ 9.0/10
3. [Gemma 4 26B 在 13 年前的至强 CPU 上以 5 tokens/秒运行](#item-3) ⭐️ 8.0/10
4. [睡眠规律性比时长更能预测死亡风险](#item-4) ⭐️ 8.0/10
5. [Claude web_fetch 工具绕过漏洞导致记忆泄露](#item-5) ⭐️ 8.0/10
6. [Hugging Face 推出 Real World VoiceEQ 基准测试](#item-6) ⭐️ 8.0/10
7. [Allen AI 的 Shippy：构建可靠智能体的经验教训](#item-7) ⭐️ 7.0/10
8. [模型路由：理论上简单，实践中困难](#item-8) ⭐️ 7.0/10
9. [腾讯以 135 亿元收购 Manus AI](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Hugging Face Transformers v5.14.0 加入 975B 参数的 Inkling 模型](https://github.com/huggingface/transformers/releases/tag/v5.14.0) ⭐️ 9.0/10

Hugging Face Transformers v5.14.0 引入了 Inkling 模型，这是一个 9750 亿参数的多模态混合专家模型，其中 410 亿参数处于激活状态，支持文本、图像和音频输入并生成文本输出。该版本还包括 TIPSv2 和 TIPSv2 DPT 模型，对 GPTNeoX 和 GPTBigCode 的破坏性变更，以及性能改进，例如使用 FlashAttention 的 SDPA 预填充速度提升高达 260%。 Inkling 是当前最大的开放权重多模态模型之一，使开发者能够构建具备视觉、音频和语言前沿能力的 AI 应用，同时保留微调和定制的能力。它被纳入广泛使用的 Transformers 库，降低了研究人员和企业实验与部署前沿多模态 AI 的门槛。 Inkling 是一个混合专家 Transformer 模型，总参数 9750 亿，激活参数 410 亿，支持高达 100 万 token 的上下文窗口。它由 Thinking Machines Lab 以开放权重发布，专为通用多模态任务设计，包括智能体系统、编程助手和检索增强生成。

github · ArthurZucker · 7月15日 19:02

**背景**: Hugging Face Transformers 是一个流行的开源库，提供数千个用于自然语言处理、计算机视觉和音频任务的预训练模型。开放权重模型允许用户访问训练好的参数，从而实现微调和部署，而无需依赖专有 API。混合专家（MoE）架构对每个输入仅激活部分参数，从而平衡性能与计算效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://thinkingmachines.ai/news/introducing-inkling/">Inkling : Our open-weights model - Thinking Machines Lab</a></li>
<li><a href="https://crawlrr.com/p/2914dff4-a262-477b-8d7a-62e24a95f751">Inkling is here, and it’s fully open-weights... — Crawlrr</a></li>
<li><a href="https://www.baseten.co/blog/meet-inkling-thinking-machines-labs-new-model/">Meet Inkling : Thinking Machines Lab's new customizable model</a></li>

</ul>
</details>

**社区讨论**: 社区成员对 Inkling 的多模态能力（尤其是音频支持）表示兴奋，一些人认为它可能成为智能体应用的有力竞争者。其他人强调开放权重是定制和降低成本的关键优势，而一位评论者则感叹现代模型设计日益复杂。

**标签**: `#transformers`, `#multimodal`, `#open-source`, `#AI`, `#model-release`

---

<a id="item-2"></a>
## [Stripe 与 Advent 联合收购 PayPal，交易额 530 亿美元](https://www.reuters.com/business/finance/stripe-advent-offer-buy-paypal-more-than-53-billion-sources-say-2026-07-15/) ⭐️ 9.0/10

据消息人士透露，Stripe 与私募股权公司 Advent International 联合出价超过 530 亿美元收购 PayPal。该交易将使两大在线支付平台合并至同一旗下。 此次收购将整合 Stripe、PayPal、Venmo、Braintree 和 Xoom 等主要支付平台，重塑支付行业格局，可能减少竞争并引发对市场主导地位和费用上涨的担忧。依赖这些平台进行支付处理的商家和消费者将受到影响。 该出价对 PayPal 的估值超过 530 亿美元。由于在线非面对面支付结账市场的集中度极高（以赫芬达尔-赫希曼指数衡量），该交易可能面临严格的反垄断审查。

hackernews · rvz · 7月15日 03:32 · [社区讨论](https://news.ycombinator.com/item?id=48915953)

**背景**: Stripe 是面向企业的领先在线支付处理商，而 PayPal 是广泛使用的消费者对商家支付平台。Advent International 是一家全球私募股权公司，管理资产达 1000 亿美元。合并将把 Stripe 面向商家的服务与 PayPal 面向消费者的产品（如 Venmo 和 Braintree）整合在一起。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Stripe,_Inc.">Stripe, Inc. - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Advent_International">Advent International</a></li>
<li><a href="https://www.adventinternational.com/">Advent International - A leading global private equity investor</a></li>

</ul>
</details>

**社区讨论**: 社区评论对该交易表达了严重担忧。用户担心 Stripe 在收购 PayPal 后可能提高交易费用，并且 Stripe 对受限行业（如大麻、成人内容）的更严格政策可能对目前依赖 PayPal 更宽松政策的供应商产生负面影响。其他人则强调了账户标记风险以及整合减少支付选择的问题。

**标签**: `#acquisition`, `#payments`, `#fintech`, `#Stripe`, `#PayPal`

---

<a id="item-3"></a>
## [Gemma 4 26B 在 13 年前的至强 CPU 上以 5 tokens/秒运行](https://www.neomindlabs.com/2026/06/08/running-gemma-4-26b-at-5-tokens-sec-on-a-13-year-old-xeon-with-no-gpu/) ⭐️ 8.0/10

一篇博客文章展示了在无 GPU 的 13 年前至强服务器上，通过量化和 CPU 优化推理，以每秒 5 个 token 的速度运行 Google 的 Gemma 4 26B（混合专家）模型。 这表明现代大语言模型可以在极其老旧的硬件上运行，使本地 AI 推理更加普及，并引发了关于与云 API 相比成本效益的讨论。 Gemma 4 26B 是一个混合专家模型，每个 token 仅激活 4B 参数，从而实现高效的 CPU 推理。该设置可能使用了 4 位量化，并利用了 CPU 的内存带宽而非计算核心。

hackernews · neomindryan · 7月15日 15:34 · [社区讨论](https://news.ycombinator.com/item?id=48922434)

**背景**: 大语言模型通常需要强大的 GPU 才能快速推理。然而，量化（降低数值精度）和混合专家（每个 token 仅激活部分参数）等技术使得模型可以在 CPU 上运行，尽管速度较慢。Gemma 4 26B 旨在平衡质量和效率，每个 token 仅激活其 26B 参数中的 4B。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ai.google.dev/gemma/docs/core/model_card_4">Gemma 4 model card | Google AI for Developers</a></li>
<li><a href="https://ollama.com/library/gemma4">gemma 4</a></li>
<li><a href="https://gemma4.com/">Gemma 4 — Google DeepMind</a></li>

</ul>
</details>

**社区讨论**: 评论者就成本效率展开辩论：有人指出云推理可能比本地电费更便宜，而另一些人预测到 2027 年，200B 的 MoE 模型将能在消费级硬件上运行。几位用户分享了他们在类似老旧硬件上的 CPU 推理速度，范围从 5 到 12 tokens/秒不等。

**标签**: `#LLM`, `#local inference`, `#efficiency`, `#hardware`, `#open source`

---

<a id="item-4"></a>
## [睡眠规律性比时长更能预测死亡风险](https://academic.oup.com/sleep/article/47/1/zsad253/7280269) ⭐️ 8.0/10

2023 年发表在《睡眠》期刊上的一项研究发现，睡眠规律性（睡眠-觉醒时间的一致性）比睡眠时长更能预测全因死亡风险。 这挑战了人们通常只关注睡眠时长的做法，并表明保持规律的作息时间可能对长寿更为关键。 该研究使用了超过 6 万名参与者的数据，并通过一种新型指数测量睡眠规律性；在调整睡眠时长和其他混杂因素后，这种关联仍然显著。

hackernews · bilsbie · 7月15日 11:46 · [社区讨论](https://news.ycombinator.com/item?id=48919363)

**背景**: 睡眠规律性指的是每日睡眠-觉醒模式的一致性。以往研究主要关注睡眠时长作为健康指标，但这项研究强调了昼夜节律对齐的重要性。

**社区讨论**: 评论者讨论了职业和轮班工作等潜在混杂因素，一些人分享了个人经验（如补充镁），并对观察性数据的因果推断表示怀疑。

**标签**: `#sleep science`, `#health research`, `#mortality risk`, `#epidemiology`, `#public health`

---

<a id="item-5"></a>
## [Claude web_fetch 工具绕过漏洞导致记忆泄露](https://simonwillison.net/2026/Jul/15/claude-web-fetch-exfiltration/#atom-everything) ⭐️ 8.0/10

安全研究员 Ayush Paul 发现了一种提示注入攻击，绕过了 Claude 的 web_fetch 工具保护机制，通过诱使 AI 从蜜罐网站跟随一系列精心构造的 URL，攻击者能够窃取用户记忆（姓名、城市、雇主）。 该漏洞表明，即使设计良好的 AI 安全措施也可能被绕过，凸显了在结合私有数据、不可信内容和外部通信（即“致命三重奏”）的 AI 代理中持续存在的数据泄露风险。这强调了需要对 AI 工具进行持续的安全审计。 该攻击利用了一个漏洞：web_fetch 可以跟随之前获取页面中嵌入的链接，从而通过嵌套 URL 链泄露数据。Anthropic 内部已发现此问题，并通过移除 web_fetch 从获取内容中导航到其他链接的能力来修复漏洞，且未支付漏洞赏金。

rss · Simon Willison · 7月15日 14:21

**背景**: Claude 的 web_fetch 工具旨在仅从用户明确提供或来自其 web_search 工具的 URL 获取内容，以防止数据泄露。然而，当 AI 代理处理不可信输入、访问敏感数据并能够进行外部通信时，它们面临“致命三重奏”风险。提示注入攻击可以诱使 AI 绕过预期的限制。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.claude.com/en/docs/agents-and-tools/tool-use/web-fetch-tool">Web fetch tool - Claude Docs</a></li>
<li><a href="https://www.osohq.com/learn/lethal-trifecta-ai-agent-security">Understanding the Lethal Trifecta of AI Agents</a></li>
<li><a href="https://explore.n1n.ai/blog/protecting-data-ai-agent-link-interaction-2026-01-29">Protecting User Data During AI Agent Link Interaction | Enterprise...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（来源：news.ycombinator.com/item?id=48916975）可能包含对攻击巧妙性的评论、对 Anthropic 修复有效性的看法，以及对 AI 代理安全更广泛影响的讨论。但输入中未提供具体评论。

**标签**: `#AI safety`, `#security vulnerability`, `#Claude`, `#data exfiltration`, `#prompt injection`

---

<a id="item-6"></a>
## [Hugging Face 推出 Real World VoiceEQ 基准测试](https://huggingface.co/blog/real-world-voiceeq) ⭐️ 8.0/10

Hugging Face 推出了 Real World VoiceEQ 基准测试，旨在评估语音 AI 系统在真实、嘈杂和多变声学环境中的人类感知质量。 该基准测试填补了关键空白，通过在真实条件下衡量语音 AI 质量，超越传统的词错误率等指标，捕捉自然度、倾听能力和回应的恰当性。 Real World VoiceEQ 使用多种声学场景，包括背景噪音、多人说话和不同距离，来测试语音 AI 系统。它提供了一种标准化的方法，在以人为本的质量维度上比较模型。

rss · Hugging Face Blog · 7月15日 00:00

**背景**: 语音 AI 系统越来越多地用于客户服务、虚拟助手和无障碍工具。传统的评估指标如词错误率（WER）无法捕捉语音交互对人类来说的自然或愉悦程度。Real World VoiceEQ 旨在通过关注真实环境中的人类感知来解决这一问题。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.hume.ai/blog/introducing-real-world-voiceeq-measuring-the-human-quality-of-voice-ai">Introducing Real World VoiceEQ: Measuring the Human Quality of Voice AI | Hume Blog | Hume AI</a></li>

</ul>
</details>

**标签**: `#voice AI`, `#benchmark`, `#speech quality`, `#Hugging Face`, `#AI evaluation`

---

<a id="item-7"></a>
## [Allen AI 的 Shippy：构建可靠智能体的经验教训](https://huggingface.co/blog/allenai/shippy-tech-blog) ⭐️ 7.0/10

Allen AI 发布了一篇关于构建 Shippy（用于海上态势感知的 AI 智能体）的技术深度文章，详细介绍了设计决策、挑战和最佳实践。 这篇文章为 AI 从业者提供了构建可信智能体的实用见解，强调可靠性而非新颖性，这对实际部署至关重要。 Shippy 被概念化为三个组件：soul（定义角色和边界的系统提示）、skills（处理特定请求的处理程序）和 config（运行时设置）。团队专注于针对实时数据而非静态快照来验证系统。

rss · Hugging Face Blog · 7月15日 17:29

**背景**: AI 智能体是利用资源在有限人类交互下实现目标的系统。基于 LLM 的智能体面临幻觉、上下文感知和信任等挑战。Shippy 专为海上态势感知设计，需要高可靠性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allenai.org/blog/shippy-deep-dive">What building Shippy taught us about building agents | Ai2</a></li>
<li><a href="https://www.linkedin.com/pulse/what-building-shippy-taught-us-agents-allen-ai-ibzwe">What building Shippy taught us about building agents</a></li>

</ul>
</details>

**标签**: `#AI agents`, `#software engineering`, `#machine learning`, `#systems design`

---

<a id="item-8"></a>
## [模型路由：理论上简单，实践中困难](https://huggingface.co/blog/ibm-research/model-routing-is-simple-until-it-isnt) ⭐️ 7.0/10

IBM Research 在 Hugging Face 博客上发表文章，揭示模型路由虽然概念上简单，但隐藏着复杂的陷阱，简单方法在实际 LLM 系统中常常失败。 随着组织部署多个 LLM 以平衡成本、延迟和质量，理解路由挑战对于构建高效可靠的 AI 系统至关重要。该分析帮助从业者避免常见错误，设计更好的路由策略。 文章讨论了基于代理的难度估计（例如使用提示长度或词汇）可能具有误导性的问题，以及需要超越简单准确率指标的稳健评估。它还强调了路由粒度与系统复杂性之间的权衡。

rss · Hugging Face Blog · 7月15日 17:27

**背景**: 模型路由是一种技术，系统从候选 LLM 池中为每个传入提示选择最合适的模型，旨在优化成本、延迟和输出质量。简单的路由规则（例如始终使用能处理任务的最小模型）常常因难度代理不完善和任务需求动态变化而失败。研究已催生开源库如 LLMRouter 以及级联或语义路由等策略来应对这些挑战。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ulab-uiuc/LLMRouter">GitHub - ulab-uiuc/LLMRouter: LLMRouter: An Open-Source Library for LLM Routing · GitHub</a></li>
<li><a href="https://aws.amazon.com/blogs/machine-learning/multi-llm-routing-strategies-for-generative-ai-applications-on-aws/">Multi-LLM routing strategies for generative AI applications on AWS | Artificial Intelligence</a></li>
<li><a href="https://arxiv.org/abs/2502.08773">[2502.08773] Universal Model Routing for Efficient LLM Inference</a></li>

</ul>
</details>

**标签**: `#model routing`, `#LLM`, `#AI systems`, `#machine learning`

---

<a id="item-9"></a>
## [腾讯以 135 亿元收购 Manus AI](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBBczB6Vl80OXZwVFR0bVFydlVBMGl2NlNreEQ0N05aa0RQV2ZSc2lKdlhGVUZ5dlNfTWVUNm1FdURDQjBDUkhVWXl0dnRfeGJyaGYtdm93?oc=5) ⭐️ 7.0/10

据报道，腾讯以 135 亿元人民币（约 19 亿美元）收购了专注于智能体 AI 的初创公司 Manus，这是其最大规模的 AI 投资之一。 此次收购标志着腾讯在 AI 领域的激进布局，可能重塑与百度、阿里巴巴等竞争对手的格局，也凸显了智能体 AI 技术的战略重要性。 据报道，该交易对 Manus 的估值为 135 亿元人民币，此前 Meta 曾试图以超过 20 亿美元收购 Manus 但被中国监管机构阻止。腾讯预计将把 Manus 的智能体 AI 能力整合到其生态系统中。

google_news · 亿邦动力网 · 7月15日 06:10

**背景**: Manus 是一家总部位于新加坡的 AI 初创公司，以开发可自主执行复杂任务的先进智能体 AI 模型而闻名。腾讯一直在通过战略投资和收购扩大其 AI 布局，旨在巩固其在 AI 竞赛中的地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Manus_(AI_agent)">Manus (AI agent) - Wikipedia</a></li>
<li><a href="https://meyka.com/blog/tencent-hk0700-in-talks-to-become-largest-shareholder-in-ai-startup-manus-at-2-billion-valuation/">Tencent (HK:0700) in Talks to Become Largest Shareholder in AI ...</a></li>

</ul>
</details>

**标签**: `#Tencent`, `#AI`, `#acquisition`, `#Manus`, `#investment`

---