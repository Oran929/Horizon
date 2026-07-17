---
layout: default
title: "AI行业热点: 2026-07-17 (ZH)"
date: 2026-07-17
lang: zh
briefing: ainews
---

> 从 77 条内容中筛选出 9 条重要资讯。

---

1. [Firefox 被编译为 WebAssembly 在浏览器中运行](#item-1) ⭐️ 9.0/10
2. [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](#item-2) ⭐️ 9.0/10
3. [华为昇腾 950 超节点首发，算力达英伟达 6.7 倍](#item-3) ⭐️ 9.0/10
4. [首次在宜居带岩石系外行星发现大气层](#item-4) ⭐️ 8.0/10
5. [EU AI Act OpenRAG：面向 RAG 的法律结构化分块数据集](#item-5) ⭐️ 8.0/10
6. [Truth Social 将向华尔街出售特朗普帖子的快速访问权限](#item-6) ⭐️ 8.0/10
7. [NVIDIA NeMo Automodel 与 Diffusers 实现可扩展微调](#item-7) ⭐️ 7.0/10
8. [中国大模型备案潮涌，AI 合规成必答题](#item-8) ⭐️ 7.0/10
9. [英伟达与 Hugging Face 合作推动机器人 AI 发展](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Firefox 被编译为 WebAssembly 在浏览器中运行](https://simonwillison.net/2026/Jul/16/firefox-in-webassembly/#atom-everything) ⭐️ 9.0/10

Puter 已将完整的 Firefox 浏览器编译为 WebAssembly，使其能够在 Chrome 等另一个浏览器中运行，并提供了现场演示。该项目使用了价值约 25,000 美元的 Claude Opus 和 Fable AI 代币，通过订阅计划降低了实际成本。 这是一项突破性的技术成就，展示了通过 WebAssembly 在另一个浏览器中运行像浏览器这样完整复杂应用的可行性。它为沙盒浏览、遗留软件保存以及基于 Web 的新型计算形式打开了可能性。 该演示使用 Wisp 协议通过 Puter 的服务器代理所有网络流量，因为浏览器代码无法打开任意网络连接。团队不得不扩展服务器以处理来自 Hacker News 的流量，该项目声称支持端到端加密，并通过检查 WebSocket 消息得到了验证。

rss · Simon Willison · 7月16日 23:34

**背景**: WebAssembly (WASM) 是一种低级二进制指令格式，可在现代网络浏览器中以接近原生的速度运行。将像 Firefox 这样的完整浏览器编译为 WASM 极具挑战性，因为其体积和复杂性巨大；生成的 gecko.wasm 文件大小为 233MB。选择 Firefox 的 Gecko 引擎是因为它支持强大的单进程模式，简化了移植工作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/MercuryWorkshop/wisp-protocol">GitHub - MercuryWorkshop/ wisp - protocol : Wisp is a low-overhead...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Gecko_(software)">Gecko (software) - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**社区讨论**: Hacker News 社区对这一技术壮举表示兴奋和惊叹，许多人讨论了其对浏览器沙盒和遗留软件的影响。一些人担心代理所有流量的成本和实用性，而另一些人则称赞了 AI 辅助开发的巧妙运用。

**标签**: `#WebAssembly`, `#Firefox`, `#browser`, `#AI-assisted development`, `#demo`

---

<a id="item-2"></a>
## [Kimi K3 2.8T-A50B：最大开源模型，Opus 4.8 级别性能，Sonnet 5 价格](https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，这是一个拥有 2.8 万亿参数的开源模型，支持 100 万 token 上下文和原生多模态输入，声称其性能与 Opus 4.8 相当，但价格与 Sonnet 5 相近。 作为有史以来最大的开源模型，Kimi K3 显著降低了前沿 AI 能力的门槛，可能加速开源社区的研究和应用。 Kimi K3 采用 Kimi Delta Attention (KDA) 和 Attention Residuals 架构，使用稀疏专家混合设计，在 896 个专家中激活 16 个，相比 K2 扩展效率提升约 2.5 倍。

rss · Latent Space · 7月17日 01:46

**背景**: Kimi K3 基于 Kimi Linear 构建，这是一种混合线性注意力架构，在各种场景下均优于全注意力。Attention Residuals 用基于输入的自适应注意力替代了标准残差连接，提升了表示质量。该模型的完整权重预计将在未来几天内开放。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.latent.space/p/ainews-kimi-k3-28t-a50b-the-largest">[AINews] Kimi K3 2.8T-A50B: the largest open model ever released; Opus 4.8-class at Sonnet 5 pricing</a></li>
<li><a href="https://rohitai.com/blog/kimi-k3-open-model-harness-contract">Kimi K3: The 2.8T Model Promising Open Weights—and a Hidden Harness Contract</a></li>
<li><a href="https://arxiv.org/abs/2510.26692">Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>

</ul>
</details>

**社区讨论**: 社区评论幽默地批评了“骑自行车的鹈鹕”基准测试，指出模型可能在训练数据中见过此类示例。一些用户比较了定价和速度，发现 Kimi K3 最便宜但最慢。其他人讨论了分词器的奇怪之处和隐藏的系统提示。

**标签**: `#AI`, `#open-source`, `#large language model`, `#Kimi K3`, `#model release`

---

<a id="item-3"></a>
## [华为昇腾 950 超节点首发，算力达英伟达 6.7 倍](https://www.ithome.com/0/978/019.htm) ⭐️ 9.0/10

在 2026 年世界人工智能大会上，华为首次公开展示了昇腾 950 超节点（Atlas 950 SuperPoD），该集群通过灵衢互联协议连接最多 8192 颗昇腾 NPU，提供 1 EFLOPS FP8 和 2 EFLOPS FP4 算力。据中银证券报告，其总算力达到英伟达搭载 144 张卡的 NVL144 系统的 6.7 倍。 这标志着华为在 AI 硬件领域的重大突破，可能重塑与英伟达在 AI 芯片市场的竞争格局。宣称的 6.7 倍性能优势可能加速中国国内 AI 基础设施的采用，减少对外国芯片的依赖。 Atlas 950 超节点采用华为自研的灵衢（UnifiedBus）互联协议，具备 TB 级带宽和 3 微秒超低往返时延。它还拥有 256 TB 全局统一内存，可扩展至 8192 颗 NPU；而较小的 Atlas 850E 风冷版本可在标准数据中心部署，无需液冷改造。

telegram · zaihuapd · 7月17日 10:27

**背景**: 华为的昇腾系列 AI 处理器旨在与英伟达的 GPU 在 AI 训练和推理领域竞争。超节点架构于 2025 年推出，通过灵衢互联协议将多台物理机器连接成一个逻辑系统，实现大规模并行计算。此次发布正值美国持续限制向中国出口先进 AI 芯片之际，推动了对国产替代方案的需求。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.huaweicentral.com/huawei-atlas-950-superpod/">Huawei Atlas 950 SuperPoD claims 6.7x more computing power ...</a></li>
<li><a href="https://lucaberton.com/blog/huawei-atlas-950-superpod-ai-infrastructure/">Huawei Atlas 950 AI SuperPoD: 8,192 NPUs as One Machine</a></li>
<li><a href="https://www.huawei.com/en/news/2025/9/hc-xu-keynote-speech">Groundbreaking SuperPoD Interconnect: Leading a New Paradigm ...</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#Huawei`, `#Ascend`, `#supercomputing`, `#NVIDIA`

---

<a id="item-4"></a>
## [首次在宜居带岩石系外行星发现大气层](https://www.bbc.com/news/articles/cy4kdd1e0ejo) ⭐️ 8.0/10

天文学家利用詹姆斯·韦伯太空望远镜在红矮星宜居带的岩石系外行星 LHS 1140b 上探测到了大气层，这是首次在潜在类地行星上确认存在大气。 这一发现挑战了此前认为红矮星行星因强烈恒星辐射无法保持大气的假设，为研究附近岩石世界的宜居性和潜在生物特征开辟了新领域。 LHS 1140b 是一颗超级地球，质量约为地球的 5.6 倍，半径大 70%，距离 49 光年，很可能是一个海洋世界，水的质量占比 9-19%；其大气层是通过氦气逃逸到太空中被探测到的。

hackernews · neversaydie · 7月17日 14:06 · [社区讨论](https://news.ycombinator.com/item?id=48947560)

**背景**: 红矮星比太阳更冷更小，其宜居带非常靠近恒星，使行星暴露在强烈的恒星耀斑和辐射下，可能剥离大气层。LHS 1140b 于 2017 年被发现，最初被认为是一颗致密岩石行星，但后来的测量显示其密度较低，与富含水的成分一致。在这样的行星上探测到大气层，为了解行星演化和地球以外生命的可能性提供了关键见解。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/LHS_1140_b">LHS 1140 b</a></li>
<li><a href="https://www.science.org/content/article/astronomers-spot-first-atmosphere-around-potentially-habitable-alien-world">Astronomers spot first atmosphere around a potentially ... - AAAS</a></li>
<li><a href="https://www.nytimes.com/2026/07/16/science/astronomy-exoplanet-atmosphere.html">Astronomers Find an Atmosphere on a Nearby Earthlike Planet</a></li>

</ul>
</details>

**社区讨论**: 评论者对红矮星周围的岩石行星能保持大气层表示惊讶，有人最初怀疑它是一颗正在被蒸发的迷你海王星，但后来指出 JWST 数据排除了这种可能。其他人讨论了费米悖论以及未来探测器（如太阳透镜望远镜）更详细研究此类行星的潜力。

**标签**: `#exoplanets`, `#JWST`, `#astronomy`, `#habitable zone`, `#atmosphere`

---

<a id="item-5"></a>
## [EU AI Act OpenRAG：面向 RAG 的法律结构化分块数据集](https://www.reddit.com/r/MachineLearning/comments/1uytlac/eu_ai_act_openrag_933_legally_structured_chunks/) ⭐️ 8.0/10

EU AI Act OpenRAG 数据集已发布，它提供了欧盟 AI 法案的 933 个法律结构化分块，并附有 BGE-M3 嵌入向量，存储在一个 SQLite 文件中，在召回率和命中率上优于滑动窗口基线方法。 该数据集能够为法律自然语言处理任务实现更准确的检索增强生成（RAG），在场景文章召回率和问答文章命中率上均有提升，这对合规和法律分析应用至关重要。 该数据集包含精确的 EUR-Lex 链接、第 113 条适用日期元数据以及刻意窄化的派生标签，模糊案例保留为 NULL；文本分类与更广泛的监管制度关联分开存储。

reddit · r/MachineLearning · /u/Automatic-Forever-63 · 7月17日 08:18

**背景**: 检索增强生成（RAG）是一种技术，通过在生成响应前从外部来源检索相关信息来增强大型语言模型。BGE-M3 是一个支持稠密检索、稀疏检索和多向量检索的多语言嵌入模型。EUR-Lex 是欧盟法律的官方在线数据库。欧盟 AI 法案（第 2024/1689 号法规）是管理人工智能的里程碑式法律框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/BAAI/bge-m3">BAAI/bge-m3 · Hugging Face</a></li>
<li><a href="https://en.wikipedia.org/wiki/Retrieval-augmented_generation">Retrieval-augmented generation - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/EUR-Lex">EUR-Lex</a></li>

</ul>
</details>

**社区讨论**: 未提供社区讨论内容，因此无法总结。

**标签**: `#RAG`, `#Legal NLP`, `#EU AI Act`, `#Embeddings`, `#SQLite`

---

<a id="item-6"></a>
## [Truth Social 将向华尔街出售特朗普帖子的快速访问权限](https://www.cnn.com/2026/07/16/business/truth-social-data-wall-street) ⭐️ 8.0/10

特朗普媒体科技集团周四宣布，Truth Social 将于 8 月 1 日推出 Truth API，以毫秒级速度向机构客户提供平台排名前 10 账号（包括唐纳德·特朗普）的实时帖子。 此举将特朗普的帖子货币化用于高频算法交易，可能为交易者提供不公平的信息优势，并引发对市场操纵和利益冲突的严重担忧，因为特朗普的帖子此前曾导致市场剧烈波动。 该 API 以毫秒级速度向高频交易者提供帖子，但定价尚未公布。CNN 此前报道称，特朗普曾利用 Truth Social 宣传自己刚买入的股票。

telegram · zaihuapd · 7月17日 01:02

**背景**: 高频交易（HFT）利用算法和超快执行速度从微小价差中获利，通常在毫秒级别。Truth Social 已成为特朗普宣布政策的主要渠道，其关于关税、伊朗及霍尔木兹海峡的帖子曾多次引发股市和油市剧烈波动。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zh.wikipedia.org/wiki/特朗普媒体与科技集团">特朗普媒体与科技集团 - 维基百科，自由的百科全书</a></li>
<li><a href="https://zhuanlan.zhihu.com/p/20982511912">高频交易（HFT）：算法交易的闪电世界 - 知乎</a></li>

</ul>
</details>

**标签**: `#Truth Social`, `#API`, `#algorithmic trading`, `#market manipulation`, `#ethics`

---

<a id="item-7"></a>
## [NVIDIA NeMo Automodel 与 Diffusers 实现可扩展微调](https://huggingface.co/blog/nvidia/scale-diffusers-finetuning-nemo-automodel) ⭐️ 7.0/10

NVIDIA 与 Hugging Face 将 NeMo Automodel 与 Diffusers 集成，实现了视频和图像扩散模型的可扩展微调。该集成使从业者能够利用分布式训练和优化内核进行大规模模型适配。 该集成使生成式视频和图像模型的大规模微调更加普及，降低了将最先进扩散模型适配到自定义数据集和任务的复杂性和成本。 NeMo Automodel 是一个基于 PyTorch DTensor 的 SPMD 训练库，支持多节点分布式训练和优化内核。与 Diffusers 的集成使得可以使用相同的可扩展基础设施微调 Stable Diffusion 和视频扩散等模型。

rss · Hugging Face Blog · 7月17日 15:57

**背景**: 扩散模型是一类学习去噪数据的生成模型，广泛用于图像和视频生成。针对特定任务微调这些模型通常需要大量计算资源。NeMo Automodel 提供了一个分布式训练框架，简化了跨多个 GPU 和节点的扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.nvidia.com/nemo/automodel">NeMo AutoModel Documentation | NVIDIA NeMo AutoModel</a></li>
<li><a href="https://github.com/NVIDIA-NeMo/Automodel">GitHub - NVIDIA - NeMo / Automodel : Pytorch Distributed native...</a></li>
<li><a href="https://huggingface.co/blog/nvidia/accelerating-fine-tuning-nvidia-nemo-automodel">Accelerating Transformers Fine-Tuning with NVIDIA NeMo AutoModel</a></li>

</ul>
</details>

**标签**: `#fine-tuning`, `#NVIDIA`, `#Diffusers`, `#video models`, `#image models`

---

<a id="item-8"></a>
## [中国大模型备案潮涌，AI 合规成必答题](https://news.google.com/rss/articles/CBMib0FVX3lxTE45QmpRWnNUVkZHZklUUVdrSXFwR3dZYTVGdkRabXdqSzhMaVRBZE9TdXUwd3J5bnlMaDVSYmNwd1R5MV9sNXBZRkFJTm40SjZRSmlHcnZxb21CSmdLeXhKMGJuY19vZDZlTEt3cEwyUQ?oc=5) ⭐️ 7.0/10

据《新民周刊》报道，中国正迎来大模型备案潮，根据《生成式人工智能服务管理暂行办法》，合规已从可选变为强制要求。 这一转变标志着中国 AI 监管环境日趋成熟，影响所有大语言模型的开发者和部署者。企业必须优先考虑合规，以避免处罚并确保市场准入。 截至 2026 年初，中国已有超过 796 款大模型完成备案，2025 年 12 月单月备案量达 85 个，创下峰值。向公众提供生成文本、图片、音频、视频等内容的模型均需备案。

google_news · 新民周刊 · 7月17日 08:59

**背景**: 中国的《生成式人工智能服务管理暂行办法》自 2023 年 8 月起施行，要求具有舆论属性或社会动员能力的 AI 服务进行备案。备案流程涉及提交模型安全、数据来源和内容治理等材料。该监管框架旨在平衡创新与安全可控。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://zhuanlan.zhihu.com/p/1910099650351986326">2025大模型备案全攻略:政策解读+材料清单+流程详解+避坑指南</a></li>
<li><a href="https://cloud.tencent.com/developer/article/2642884">2026年最新大模型备案公示名单-腾讯云开发者社区-腾讯云</a></li>
<li><a href="https://blog.csdn.net/tongxiaojituan/article/details/156934391">网信办发布！2025年大模型备案+登记具体清单（附备案攻略_全国已有663...</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#China`, `#large language models`, `#compliance`

---

<a id="item-9"></a>
## [英伟达与 Hugging Face 合作推动机器人 AI 发展](https://news.google.com/rss/articles/CBMif0FVX3lxTE94MTAxZEFWaEdMOWhOME1rYzdmS0JUbk1mbjgzSmkyX1o4aDRKMHJMNHVNbDdLQWNMVGpUeHRqRUlWTEE4bG9IVkZoSExpUGNvMGxMNGR0RUVBbHFpMGdlN0JJMHpITjVJbkd4RWt3UHcyZjZ1SUNfT0Y2Mm5GMnM?oc=5) ⭐️ 7.0/10

英伟达与 Hugging Face 宣布合作，通过将 Hugging Face 的 LeRobot 平台与英伟达的 AI、Omniverse 和 Isaac 机器人技术集成，加速开源 AI 机器人领域的发展。 此次合作可能使机器人 AI 开发民主化，类似于大语言模型（LLM）的爆发式普及，从而推动制造业、医疗和物流等行业的广泛创新。 该合作将 Hugging Face 的 LeRobot 开源 AI 平台与英伟达的仿真和机器人工具（包括 Isaac Lab 和 Omniverse）相结合，为机器人策略学习提供可扩展的基准测试和数据集。

google_news · PANews · 7月17日 05:09

**背景**: 像 GPT-4 这样的大语言模型（LLM）因开源平台和社区贡献而迅速普及。类似地，机器人 AI 此前较为分散，共享资源有限。此次合作旨在为机器人模型和数据创建一个中心化枢纽，可能引发类似的发展轨迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/hugging-face-lerobot-open-source-robotics/">Hugging Face and NVIDIA to Accelerate Open-Source AI Robotics ...</a></li>
<li><a href="https://www.timesofai.com/news/hugging-face-nvidia-collaboration-ai-robotics/">Hugging Face NVIDIA Partner to AI Robotics Research</a></li>
<li><a href="https://huggingface.co/nvidia">Org profile for NVIDIA on Hugging Face , the AI community building...</a></li>

</ul>
</details>

**标签**: `#NVIDIA`, `#Hugging Face`, `#Robotics`, `#AI`, `#Collaboration`

---