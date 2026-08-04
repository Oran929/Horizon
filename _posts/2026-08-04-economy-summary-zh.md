---
layout: default
title: "金融市场摘要: 2026-08-04 (ZH)"
date: 2026-08-04
lang: zh
briefing: economy
---

> 从 114 条内容中筛选出 4 条重要资讯。

---

1. [Kimi K3：压缩记忆、深度注意力与潜在路由](#item-1) ⭐️ 8.0/10
2. [大型科技公司云积压订单达 2.3 万亿美元，推动 AI 资本支出](#item-2) ⭐️ 7.0/10
3. [Arm 悄然打造其下一个重大 AI 优势](#item-3) ⭐️ 7.0/10
4. [阿里巴巴 Qwen3.8-Max 加剧与美国对手的 AI 竞赛](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Kimi K3：压缩记忆、深度注意力与潜在路由](https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the) ⭐️ 8.0/10

SemiAnalysis 发布了对 Kimi K3 架构的深度技术分析，重点介绍了其在压缩记忆、跨深度注意力和潜在专家路由方面的创新。该模型采用 Kimi Delta Attention (KDA) 和 Attention Residuals (AttnRes)，以扩展到超过万亿参数规模。 该分析意义重大，因为 Kimi K3 的架构可能为大型语言模型的推理效率树立新标准，有望降低计算成本，并支持在资源受限的设备上部署。记忆压缩和路由方面的创新可能影响整个行业未来的 AI 系统设计。 Kimi K3 采用 LatentMoE，在分发前压缩路由令牌，在聚合后解压缩，并在上投影前应用 RMSNorm。该模型还使用跨深度注意力，允许注意力头关注前几层的 KV 对，并将专家权重以打包的 4 位格式存储在 NVMe 上。

rss · SemiAnalysis · 8月3日 19:42

**背景**: 大型语言模型通常使用注意力机制来处理序列，但扩展到万亿参数需要高效的内存和计算管理。混合专家（MoE）模型将令牌路由到专门的专家，但在高维空间中的路由成本较高。LatentMoE 通过将令牌投影到低维潜在空间，将路由维度与隐藏维度解耦，从而减少参数负载和通信流量。跨深度注意力，如 Mixture-of-Depths Attention，允许注意力头访问前几层的表示，改善信息流动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/kimi-k3-the-manos-the-mythos-the?action=share">Kimi K3: The Manos, The Mythos, The Legendos</a></li>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://arxiv.org/abs/2603.15619">[2603.15619] Mixture-of-Depths Attention</a></li>

</ul>
</details>

**社区讨论**: 此新闻项未提供社区评论。

**标签**: `#AI architecture`, `#inference`, `#memory compression`, `#attention mechanisms`, `#Kimi K3`

---

<a id="item-2"></a>
## [大型科技公司云积压订单达 2.3 万亿美元，推动 AI 资本支出](https://finance.yahoo.com/technology/article/big-techs-cloud-backlog-just-hit-23-trillion--and-its-feeding-ai-capex-plans-181459457.html) ⭐️ 7.0/10

大型科技公司的云积压订单已达到创纪录的 2.3 万亿美元，这一趋势正在推动其大规模的人工智能资本支出计划。文章强调，这一财务趋势正在助长这些公司对 AI 基础设施的激进投资。 这一里程碑凸显了云服务的强劲需求以及大型科技公司为 AI 发展提供资金的能力。它标志着持续的投资周期，可能塑造科技行业乃至整体经济的竞争格局。 这 2.3 万亿美元的积压订单代表了尚未履行的云合同承诺，为亚马逊、微软和 Alphabet 等公司提供了收入管道。这一积压订单是它们计划 AI 资本支出的关键驱动因素，预计 2026 年主要参与者的 AI 资本支出将超过 6500 亿美元。

openbb · NVDA · 8月3日 18:14

**背景**: 云积压订单是指客户已签署但尚未消费的云服务合同的价值。AI 资本支出（capex）是公司在 AI 基础设施上的投入，如数据中心、芯片和能源。大型科技公司正大力投资 AI，而它们的云积压订单为这些投资提供了稳定的收入基础。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fourweekmba.com/the-ai-capex-race/">The AI Capex Race - FourWeekMBA</a></li>
<li><a href="https://tech-insider.org/big-tech-650-billion-ai-infrastructure-capex-2026/">Big Tech's $650B AI Capex Surge Reshaping the Economy [2026]</a></li>

</ul>
</details>

**标签**: `#cloud`, `#AI`, `#capex`, `#big tech`, `#financial trends`

---

<a id="item-3"></a>
## [Arm 悄然打造其下一个重大 AI 优势](https://finance.yahoo.com/technology/ai/articles/arm-quietly-builds-next-big-174956235.html) ⭐️ 7.0/10

据报道，Arm 正在开发一项新的面向 AI 的硬件计划，旨在更直接地参与 AI 半导体市场竞争。此举可能重塑 AI 硬件格局，但具体技术细节尚未公开。 这一进展意义重大，因为 Arm 架构已为大多数移动和嵌入式设备提供支持，而进军 AI 硬件领域可能挑战 NVIDIA 和 Intel 等主导厂商。它还可能通过为 AI 工作负载提供更节能的替代方案，影响更广泛的 AI 生态系统。 文章缺乏具体技术细节，但表明 Arm 正在利用其在低功耗设计和广泛授权合作方面的现有优势。该计划仍处于早期阶段，尚未提供官方公告或产品时间表。

openbb · NVDA · 8月3日 17:49

**背景**: Arm 设计半导体知识产权（IP），并将其授权给苹果、高通和三星等公司，而非自行制造芯片。其架构以能效著称，非常适合移动设备，如今正扩展至面向 AI 的硬件，以满足日益增长的端侧 AI 处理需求。

**标签**: `#AI`, `#hardware`, `#Arm`, `#semiconductors`, `#industry`

---

<a id="item-4"></a>
## [阿里巴巴 Qwen3.8-Max 加剧与美国对手的 AI 竞赛](https://finance.yahoo.com/technology/ai/articles/alibabas-qwen3-8-max-intensifies-161900767.html) ⭐️ 7.0/10

阿里巴巴发布了 Qwen3.8-Max，这是其迄今最强大的大语言模型，拥有 2.4 万亿参数和 100 万 token 的上下文窗口。该模型采用混合专家（MoE）架构，并计划于下周开放权重。 此次发布加剧了中国与美国 AI 公司之间的竞争，挑战了美国在大语言模型领域的主导地位。通过开放权重，阿里巴巴可能吸引全球开发者，并将平衡转向开源替代方案。 Qwen3.8-Max 总参数达 2.4 万亿，约为之前 Qwen3.5 模型的七倍。完整的 Qwen3.8 模型预计将以开放权重发布，但具体日期、许可证或独立基准尚未公布。

openbb · BABA · 8月3日 16:19

**背景**: 大语言模型（LLM）是在大量文本上训练的 AI 系统，能够理解和生成类似人类的语言。阿里巴巴的 Qwen 系列包括多种文本、视觉和音频模型，公司一直在发布开放权重模型，以与 OpenAI 的 GPT 系列等封闭系统竞争。Qwen3.8-Max 的发布标志着阿里巴巴在全球 AI 竞赛中领先的雄心。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://siliconangle.com/2026/08/03/alibaba-debuts-qwen3-8-max-model-2-4t-parameters/">Alibaba debuts Qwen3.8-Max model with 2.4T parameters - SiliconANGLE</a></li>
<li><a href="https://www.marktechpost.com/2026/08/03/alibaba-qwen-releases-qwen3-8-max/">Alibaba Qwen Releases Qwen3.8-Max: A 2.4 Trillion Parameter MoE Model and the Most Capable One in the Qwen Family to Date - MarkTechPost</a></li>
<li><a href="https://kie.ai/blog/what-is-qwen3-8-max">What Is Qwen3.8-Max? Alibaba's 2.4T Flagship</a></li>

</ul>
</details>

**标签**: `#AI`, `#Alibaba`, `#Qwen`, `#LLM`, `#competition`

---