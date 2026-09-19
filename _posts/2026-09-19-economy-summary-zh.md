---
layout: default
title: "金融市场摘要: 2026-09-19 (ZH)"
date: 2026-09-19
lang: zh
briefing: economy
---

> 从 118 条内容中筛选出 4 条重要资讯。

---

1. [SemiAnalysis 探讨 Engram 模型的 DRAM/SSD 卸载协同设计](#item-1) ⭐️ 7.0/10
2. [《纽约时报》起诉 OpenAI 与微软，指控其“前所未有地窃取”内容](#item-2) ⭐️ 7.0/10
3. [纽森通过行政命令重启加州 AI“终止开关”](#item-3) ⭐️ 7.0/10
4. [Coinbase 申请上市苹果、特斯拉、英伟达单只股票永续期货](#item-4) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [SemiAnalysis 探讨 Engram 模型的 DRAM/SSD 卸载协同设计](https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign) ⭐️ 7.0/10

SemiAnalysis 发布了一篇题为《Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD Offloading》的技术深度文章，探讨了 Engram 等新模型架构如何将嵌入查找卸载到 DRAM 和 SSD，以降低对 HBM 容量的需求。文章还涉及 DeepSeek V4.1 Flash、AgentX、InferenceX 以及 NVMe 实验，包括在 B200 GPU 上使用未优化的 vLLM 分支，将 Engram 表存储在本地 SSD 的内存映射文件中。 这项分析的重要性在于，将嵌入表从昂贵的 HBM 卸载到更便宜的 DRAM 和 SSD，可能大幅降低大模型推理服务的成本，并重塑内存与存储硬件的总体可寻址市场。它还表明，Engram 和 DeepSeek V4.1 Flash 等新兴模型架构可能推动 AI 推理基础设施对 NVMe SSD 和大容量 DRAM 的需求。 在 B200 GPU 上，SemiAnalysis 创建了一个未优化的 vLLM 分支，将 Engram 表存储在本地 SSD 的内存映射文件中，使操作系统能在其他应用需要内存时回收这些表页。不过，已有研究指出，SSD 每比特读取能耗远高于 DRAM，因此在解码阶段将 MoE 专家权重卸载到 SSD 可能带来能效方面的权衡。

rss · SemiAnalysis · 9月18日 14:34

**背景**: Engram 是一种模型架构概念，它将嵌入查找与主计算路径分离，使大型嵌入表可以存放在更便宜的存储层级中，而不是 HBM 中。HBM（高带宽内存）是堆叠在 AI 加速器旁边的高速昂贵内存，而 DRAM 和 NVMe SSD 以更低成本提供大得多的容量，但延迟和每次访问的能耗更高。DeepSeek V4.1 Flash 是 DeepSeek 近期推出的多模态模型，在 45T token 上训练，采用稀疏注意力，上下文扩展至 100 万 token，正是推动此类卸载策略的典型架构。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://newsletter.semianalysis.com/p/engrams-embedding-entendre-codesign">Engrams Embedding Entendre: Codesign for Efficient DRAM/SSD ...</a></li>
<li><a href="https://arxiv.org/html/2508.06978">SSD Offloading for LLM Mixture-of-Experts Weights Considered...</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash">deepseek -ai/ DeepSeek - V 4 . 1 - Flash · Hugging Face</a></li>

</ul>
</details>

**标签**: `#AI/ML`, `#Systems`, `#Memory`, `#Storage`, `#Hardware`

---

<a id="item-2"></a>
## [《纽约时报》起诉 OpenAI 与微软，指控其“前所未有地窃取”内容](https://finance.yahoo.com/video/astonishing-theft-unprecedented-proportions-nyt-134822530.html) ⭐️ 7.0/10

《纽约时报》已在纽约南区联邦地区法院起诉 OpenAI 和微软，指控其未经许可复制该报受版权保护的新闻内容，用于训练 OpenAI 的旗舰模型 ChatGPT。该案于 2023 年底提起，此后已有另外十一家出版商加入诉讼。 这是传统媒体与 AI 开发者之间的一场标志性对决，可能重新界定合理使用原则如何适用于生成式 AI 模型的训练，进而迫使企业为训练数据付费授权并承担数十亿美元的赔偿。其判决结果将影响整个 AI 行业的数据获取方式，并波及每一家作品被纳入训练语料的出版商。 该诉讼提交至纽约南区联邦地区法院，核心主张是：将整部作品复制进训练数据集，依据《美国法典》第 17 编第 106 条即构成直接侵权，无论模型后续如何使用这些内容。微软于 2019 年首次投资 OpenAI，这一点是主张微软对涉嫌复制行为负有连带责任的关键。

openbb · NVDA · 9月18日 13:48

**背景**: 合理使用是美国的一项法律原则，允许在特定情形下未经许可有限度地使用受版权保护的作品，也是 AI 公司面对训练数据侵权指控时的主要抗辩理由。生成式 AI 模型必须基于海量文本进行训练，其中大量内容受版权保护，而开发者通常并未事先取得权利人许可。法院直到最近才开始就此类训练是否构成合理使用作出裁决，而早期判决的方向并不一致。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.copyright.gov/fair-use/">U.S. Copyright Office Fair Use Index</a></li>
<li><a href="https://ailawsuittracker.com/issues/training-data-copyright/">AI Training Data Copyright Lawsuits (2026)</a></li>
<li><a href="https://www.channelnewsasia.com/world/new-york-times-microsoft-openai-theft-6393561">NYT alleges Microsoft , OpenAI knew using news content was theft</a></li>

</ul>
</details>

**标签**: `#AI`, `#copyright`, `#lawsuit`, `#OpenAI`, `#New York Times`

---

<a id="item-3"></a>
## [纽森通过行政命令重启加州 AI“终止开关”](https://www.barrons.com/articles/california-newsom-ai-kill-switch-executive-order-c7a352df?siteid=yhoof2&yptr=yahoo) ⭐️ 7.0/10

加州州长加文·纽森于 2026 年 9 月 18 日签署行政命令，要求州政府机构加快制定 AI 安全规则，并开发能够关闭最强大 AI 模型的紧急“终止开关”。该命令还设立了一个专家小组，为加州如何加强 AI 安全法律提出建议。 加州是众多全球领先 AI 公司的所在地，因此其监管选择可能为其他州树立先例，并影响国家层面的 AI 政策。此举表明 AI 安全监管正获得越来越强的政治动力，尽管批评者警告强制关闭能力可能拖慢创新或在技术上难以实现。 “终止开关”概念此前曾出现在纽森于 2024 年否决的立法中，而此次行政命令通过机构规则制定而非新法律将其重新提出。该命令本身并未对 AI 开发者施加具有约束力的要求，而是指示州政府机构和一个新的专家小组起草建议和安全规则。

openbb · NVDA · 9月18日 20:45

**背景**: AI“终止开关”通常指能力控制措施，使人类能够监控并关闭 AI 系统，尤其是那些可能以偏离目标或危险方式行动的高级模型。这类控制措施被普遍视为对齐研究的补充而非替代，因为随着系统变得更智能，其有效性会下降。纽森的行政命令出台之际，近期涉及强大模型的事件引发了公众对失控 AI 的更大担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/09/18/california-newsom-executive-order-ai.html">California Gov. Newsom issues executive order to rein in AI</a></li>
<li><a href="https://calmatters.org/politics/2026/09/ai-rules-newsom-state-directive/">Newsom orders California agencies to develop new AI safety ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_kill_switch">AI kill switch</a></li>

</ul>
</details>

**标签**: `#AI regulation`, `#California`, `#AI safety`, `#policy`, `#executive order`

---

<a id="item-4"></a>
## [Coinbase 申请上市苹果、特斯拉、英伟达单只股票永续期货](https://finance.yahoo.com/markets/options/articles/coinbase-files-list-single-stock-210130400.html) ⭐️ 7.0/10

Coinbase 已向监管机构提交申请，计划上市与苹果、特斯拉和英伟达挂钩的单只股票永续期货，旨在将加密风格的 24/5 衍生品交易引入美国个股市场。这些拟议合约目前正等待监管批准后方可推出。 这标志着传统金融与加密衍生品的显著融合，可能为美国交易者提供对主要科技股的杠杆化、全天候交易渠道。若获批，可能促使其他交易所跟进，并重塑散户投机股票的方式。 与传统期货不同，永续合约没有到期日，并使用资金费率机制使合约价格与现货市场保持一致，从而实现连续交易。Coinbase 的申请紧随 Kraken 母公司 Payward 的类似举措，后者提议推出 10 只单只股票永续合约，交易时间为 24/5。

openbb · NVDA · 9月18日 21:01

**背景**: 永续期货是一种跟踪资产价格且无到期日的衍生品合约，最初在加密货币市场因高流动性和 24/7 交易而流行。单只股票永续合约将这一结构应用于苹果、特斯拉和英伟达等个股，而非加密代币。在美国，此类产品需要监管批准，而 Coinbase Derivatives 一直在扩展其产品线，包括将 USDC 作为期货交易抵押品。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cointelegraph.com/news/coinbase-files-to-bring-single-stock-perpetual-futures-to-us-market">Coinbase Seeks Approval to Bring Stock Perps to US</a></li>
<li><a href="https://cryptobriefing.com/payward-kraken-single-stock-perpetual-futures/">Payward files to offer single - stock perpetual futures on Kraken for...</a></li>
<li><a href="https://b2broker.com/news/what-are-the-perpetual-futures-how-do-they-work/">What Are the Perpetual Futures & How do They Work?</a></li>

</ul>
</details>

**标签**: `#cryptocurrency`, `#derivatives`, `#Coinbase`, `#stock market`, `#regulation`

---