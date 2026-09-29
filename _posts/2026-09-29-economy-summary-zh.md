---
layout: default
title: "金融市场摘要: 2026-09-29 (ZH)"
date: 2026-09-29
lang: zh
briefing: economy
---

> 从 110 条内容中筛选出 6 条重要资讯。

---

1. [AMD 以 82 亿美元收购李飞飞的 World Labs](#item-1) ⭐️ 9.0/10
2. [SemiAnalysis 分析 GLM-5.3 稀疏注意力对 HBM 内存的影响](#item-2) ⭐️ 7.0/10
3. [三星向 KKR 与英伟达支持的 AI 基础设施公司 Helix 投资 10 亿美元](#item-3) ⭐️ 7.0/10
4. [英伟达推动玻璃封装，或重塑 AI 芯片格局](#item-4) ⭐️ 7.0/10
5. [台积电 2 纳米晶圆产能预计将超出此前预期](#item-5) ⭐️ 7.0/10
6. [中国考虑允许字节跳动和阿里巴巴购买新的英伟达芯片](#item-6) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [AMD 以 82 亿美元收购李飞飞的 World Labs](https://finance.yahoo.com/news/amd-acquires-world-labs-8-203900428.html) ⭐️ 9.0/10

AMD 于 2026 年 9 月 28 日宣布已达成最终协议，以 82 亿美元收购由人工智能先驱李飞飞博士创立的人工智能模型与研究实验室 World Labs。这是 AMD 有史以来第二大收购，此前 AMD 曾对该公司进行过投资。 这笔收购是对“物理 AI”（即在现实世界中感知并行动的人工智能系统）的重大战略押注，表明 AMD 意图在机器人和具身智能领域与英伟达的 Cosmos AI 模型展开竞争。这可能重塑人工智能硬件与软件格局，并加剧芯片、模型和机器人平台之间的竞争。 AMD 表示 World Labs 团队将继续专注于人工智能模型研究，并将这笔交易定位为强化“开放”人工智能生态，但收购后能否留住顶尖研究人才并无保证。82 亿美元的价格使其成为 AMD 史上第二大收购，仅次于此前收购专注于推理的芯片设计公司 Taalas 的协议。

openbb · NVDA · 9月28日 23:17

**背景**: World Labs 由李飞飞与 Justin Johnson、Christoph Lassner 和 Ben Mildenhall 共同创立，他们都是计算机视觉和图形学领域的世界知名技术专家。“物理 AI”指将模型与传感器、控制系统和执行器结合，从而在物理世界中感知、推理并行动的人工智能系统，涵盖机器人、自动驾驶汽车和智能工厂。这与主要停留在信息领域的数字 AI 或生成式 AI 形成对比，该术语在 2020 年代的人工智能热潮中日益受到关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsroom.amd.com/news/amd-acquire-world-labs/">AMD to Acquire World Labs to Advance the... - AMD Newsroom</a></li>
<li><a href="https://www.cnbc.com/2026/09/28/amd-fei-fei-li-world-labs.html">AMD acquiring Fei-Fei Li's World Labs AI firm in deal worth $8.2B - CNBC</a></li>
<li><a href="https://en.wikipedia.org/wiki/Physical_AI">Physical AI</a></li>

</ul>
</details>

**社区讨论**: LinkedIn 和科技媒体的评论认为，这笔交易本质上是为了打造英伟达 Cosmos AI 模型竞争对手而进行的人才收购，同时指出收购后留住顶尖人才并无保证，AMD 的“开放”人工智能主张仍需获得开发者认可。

**标签**: `#AMD`, `#World Labs`, `#acquisition`, `#physical AI`, `#Fei-Fei Li`

---

<a id="item-2"></a>
## [SemiAnalysis 分析 GLM-5.3 稀疏注意力对 HBM 内存的影响](https://newsletter.semianalysis.com/p/sparse-savings-persistent-demand-inside-glm53) ⭐️ 7.0/10

SemiAnalysis 发布了一篇深度分析文章，探讨 GLM-5.3 的稀疏注意力机制，研究 KV 缓存卸载、HiSparse、DeepSeek 风格稀疏注意力以及 IndexShare 如何影响 HBM 内存使用和持续性需求。报告将这些技术描述为从单纯节省内存容量转向 LLM 推理基础设施中持续性内存需求的转变。 随着大语言模型扩展到数千亿参数，HBM 内存容量和带宽已成为推理服务的主要瓶颈，因此减少 KV 缓存占用的技术直接影响硬件成本和部署可行性。该分析对 AI 基础设施规划者、GPU 厂商和云服务提供商决定为 GLM-5.3 等稀疏注意力模型配置多少 HBM 具有重要意义。 GLM-5.3 是一个 753B 参数的 MoE 模型，采用 DeepSeek 风格稀疏注意力和原生 FP8 权重，其 Flash 变体使用 34 层 Kimi Delta Attention 加 11 层稀疏 MLA。HiSparse 是一种精确的、与索引器无关的分层 KV 缓存，仅在 GPU 上保留少量热 KV 缓冲区，而将完整 KV 历史存储在 CPU 固定内存中，从而减少解码阶段每个请求的 GPU 内存占用。

rss · SemiAnalysis · 9月28日 19:26

**背景**: 稀疏注意力减少了模型需要关注的键值对数量，从而削减随上下文长度增长的 KV 缓存。KV 缓存卸载将不常访问的缓存数据从稀缺的 GPU HBM 转移到更便宜的 CPU 内存或存储层，而像 HiSparse 这样的分层方案则在 GPU 上保留少量热工作集。GLM-5.3 是 Z.ai 最新的模型系列，其将线性注意力层与稀疏注意力层相结合的设计旨在平衡局部依赖建模与全局上下文检索。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.z.ai/guides/vlm/glm-5.3-flash">GLM - 5 . 3 -Flash/FlashX - Overview - Z.AI DEVELOPER DOCUMENT</a></li>
<li><a href="https://docs.sglang.io/docs/advanced_features/hisparse_guide">HiSparse : Hierarchical Sparse Attention - SGLang Documentation</a></li>
<li><a href="https://handbook.modular.com/inference-optimization/kv-cache-offloading/">KV cache offloading | LLM Inference Handbook</a></li>

</ul>
</details>

**标签**: `#LLM inference`, `#sparse attention`, `#HBM memory`, `#AI infrastructure`, `#GLM`

---

<a id="item-3"></a>
## [三星向 KKR 与英伟达支持的 AI 基础设施公司 Helix 投资 10 亿美元](https://www.wsj.com/tech/ai/samsung-commits-1-billion-to-ai-infrastructure-firm-backed-by-kkr-nvidia-d1039c57?siteid=yhoof2&yptr=yahoo) ⭐️ 7.0/10

三星已承诺向 Helix Digital Infrastructure 投资 10 亿美元，这是一家由私募股权公司 KKR 发起、专注于 AI 基础设施的公司，已获得超过 100 亿美元的承诺资本。此次投资使三星与 KKR、英伟达、科威特投资局和 Vistra 一同成为该新公司的支持方。 这笔交易表明，大型企业集团正在对 AI 基础设施而非仅仅是 AI 模型或芯片进行大规模财务押注，这可能重塑数据中心、能源和半导体领域的竞争格局。在 AI 算力需求全球激增之际，三星的参与也加深了其与英伟达和 KKR 的战略联系。 Helix Digital Infrastructure 由 KKR 发起，拥有超过 100 亿美元的承诺资本，除三星外还获得英伟达、Vistra 和科威特投资局的支持。三星将这笔投资定位为依托其关联公司在 AI 基础设施全栈中的能力，为未来与 Helix 的合作奠定基础。

openbb · NVDA · 9月28日 23:37

**背景**: KKR 是一家领先的全球投资公司，在私募股权、基础设施和另类资产领域拥有四十多年的经验。Helix Digital Infrastructure 是一家新成立的、专注于 AI 的基础设施公司，汇集来自主要投资者的资本，用于建设数据中心及相关 AI 算力。三星是一家韩国企业集团，业务涵盖半导体、消费电子和显示器，使其在 AI 硬件供应链中拥有广泛的利益。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.samsung.com/global/samsung-to-invest-usd-1-billion-in-ai-infrastructure-company-helix">Samsung To Invest USD 1 Billion in AI Infrastructure Company Helix...</a></li>
<li><a href="https://dcpulse.com/news/kkr-launches-helix-ai-infrastructure-firm">KKR Launches Helix AI Infrastructure Firm With $10 Billion</a></li>
<li><a href="https://www.kkr.com/">KKR : A Leading Global Investment Firm | KKR</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Samsung`, `#Nvidia`, `#investment`, `#industry news`

---

<a id="item-4"></a>
## [英伟达推动玻璃封装，或重塑 AI 芯片格局](https://finance.yahoo.com/technology/ai/articles/nvidia-glass-packaging-push-could-224627650.html) ⭐️ 7.0/10

据报道，英伟达正在推动在 AI 芯片中采用玻璃封装，这一转变可能改变先进半导体的设计与制造方式。该举措旨在用玻璃替代芯片封装中传统的有机树脂基板。 先进封装已成为 AI 芯片竞赛中的关键瓶颈，而玻璃基板有望提升性能、良率和尺寸稳定性。若被采用，这一转变可能影响从康宁等材料供应商到封装代工厂及 AI 基础设施厂商的整条半导体供应链。 与 ABF 或 BT 树脂等有机基板相比，玻璃基板具有更低的热膨胀系数（CTE）和更高的表面平整度，有助于实现更精细的布线和玻璃通孔。然而，玻璃封装在大规模量产上仍面临挑战，且目前并非英伟达已确认的产品发布。

openbb · NVDA · 9月28日 22:46

**背景**: 芯片封装是将半导体裸片封装并连接到基板、进而与整个系统相连的工艺。传统基板使用有机树脂，但随着 AI 芯片变得更大更复杂，这些材料在散热、翘曲和精细布线方面逐渐吃力。玻璃因其更平整、热稳定性更好且能实现更高密度互连而被视为替代方案，这对多芯粒 AI 加速器尤为重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.nextpcb.com/blog/glass-substrate-what-is-it">Glass Substrate : What It Is & Why It Matters in Chip Packaging</a></li>
<li><a href="https://www.ajupress.com/view/20260105152112913">Packaging becomes the real bottleneck in AI race... | AJU PRESS</a></li>
<li><a href="https://www.corning.com/worldwide/en/products/advanced-optics/product-materials/semiconductor-laser-optic-components/semiconductor-glass-wafers.html">Semiconductor Glass Wafers | Semiconductor Packaging | Corning</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#AI chips`, `#semiconductor packaging`, `#hardware`, `#industry news`

---

<a id="item-5"></a>
## [台积电 2 纳米晶圆产能预计将超出此前预期](https://finance.yahoo.com/technology/articles/tsmc-2nm-wafer-capacity-exceed-030730906.html) ⭐️ 7.0/10

据 EDN 报道，台积电 2 纳米晶圆产能目前预计将超出此前预期，表明市场对其最先进制程的需求强于预期。此次上调预期意味着台积电正在量产前加速 N2 产能建设。 2 纳米产能超出预期之所以重要，是因为苹果、英伟达和 AMD 等主要芯片设计厂商预计将依赖该制程生产下一代产品。这也进一步巩固了台积电在与三星 SF2 和英特尔 18A 的先进制程竞赛中的领先地位，对 AI 硬件供应具有广泛影响。 2 纳米制程是 3 纳米之后的完整一代升级，通常引入全环绕栅极纳米片等新型晶体管架构，从而提升性能与能效。产能通常以每月晶圆开工量衡量，而台积电整个网络的 300 毫米总产能目前已达到约每月 160 万片晶圆。

openbb · NVDA · 9月28日 03:07

**背景**: 在半导体制造中，“2 纳米”指的是一个工艺世代，而非实际物理尺寸，就像 5G 代表一种无线标准一样。台积电的 2 纳米制程名为 N2，与三星的 SF2 和英特尔的 18A 竞争，后者已于 2025 年底进入量产。先进制程对 AI 加速器、智能手机和数据中心芯片至关重要，因为这些领域对每瓦性能要求极高。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/2_nm_process">2 nm process - Wikipedia</a></li>
<li><a href="https://www.lambdafin.com/articles/semiconductor-wafer-starts">Semiconductor Wafer Starts 2026: Capacity, Nodes, and Foundry Share - Lambda Finance</a></li>
<li><a href="https://www.all-about-industries.com/the-2-nanometer-process-and-the-performance-trap-a-2f968ac60f1fbd4861382353e778aed0/">The 2-Nanometer Process and the Performance Trap</a></li>

</ul>
</details>

**标签**: `#TSMC`, `#2nm`, `#semiconductor manufacturing`, `#chip technology`, `#AI hardware`

---

<a id="item-6"></a>
## [中国考虑允许字节跳动和阿里巴巴购买新的英伟达芯片](https://finance.yahoo.com/technology/articles/china-weighs-letting-bytedance-alibaba-192115872.html) ⭐️ 7.0/10

据 CNBC 援引路透社的报道，中国据称正在考虑允许字节跳动和阿里巴巴购买新的英伟达 AI 芯片，北京已为其三家最大科技公司购买英伟达 H200 人工智能芯片开了绿灯。这标志着中国立场的转变，因为它在平衡自身 AI 发展需求与推动国内芯片生产之间寻求平衡。 这一潜在的政策松绑可能显著重塑全球 AI 硬件格局，影响英伟达的收入、美中科技关系以及中国 AI 产业的竞争态势。如果获批，这将使中国领先的 AI 公司能够获得更先进的计算能力，同时仍在推进国产替代方案。 报道指出，中国将允许其三家最大科技公司购买英伟达的 H200 芯片，但批准的具体范围和条件仍不明确。与此同时，字节跳动和阿里巴巴一直在开发和采购国产 AI 芯片，以减少对美国供应商的依赖。

openbb · BABA · 9月28日 19:21

**背景**: 英伟达的先进 AI 芯片（如 H200）一直受到美国出口限制，这些限制旨在遏制中国获取用于 AI 训练和推理的前沿半导体。作为回应，字节跳动和阿里巴巴等中国科技巨头加快了自研 AI 芯片的步伐，并从国内供应商采购，同时也在探索获取受限英伟达硬件的变通方法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/27/china-bytedance-alibaba-nvidia-chips.html">China may let ByteDance, Alibaba buy new Nvidia chips : The...</a></li>
<li><a href="https://www.reuters.com/world/asia-pacific/bytedance-developing-ai-chip-manufacturing-talks-with-samsung-sources-say-2026-02-11/">Exclusive: ByteDance developing AI chip, in manufacturing talks with Samsung, sources say | Reuters</a></li>
<li><a href="https://thecomputechain.substack.com/p/inside-alibabas-ai-chip-strategy">Inside Alibaba’s AI Chip Strategy: Self-Reliance, Pragmatic ...</a></li>

</ul>
</details>

**标签**: `#Nvidia`, `#China`, `#AI chips`, `#geopolitics`, `#tech policy`

---