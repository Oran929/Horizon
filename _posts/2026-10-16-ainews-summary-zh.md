---
layout: default
title: "AI行业热点: 2026-10-16 (ZH)"
date: 2026-10-16
lang: zh
briefing: ainews
---

> 从 77 条内容中筛选出 8 条重要资讯。

---

1. [Hugging Face Transformers v5.20.0 新增 Meta 816B Muse Spark Open 与 Ling 3.0](#item-1) ⭐️ 8.0/10
2. [Meta 发布 816B 开放权重模型 Muse Spark Open](#item-2) ⭐️ 8.0/10
3. [神经网络是“干净”的：机械可解释性的新论点](#item-3) ⭐️ 8.0/10
4. [Citizen Lab 揭露：定向广告被用于投递零点击间谍软件](#item-4) ⭐️ 8.0/10
5. [Anthropic 在 IPO 前向投资者披露第三季度营收达 168 亿美元](#item-5) ⭐️ 8.0/10
6. [Modal 年经常性收入达 10 亿美元、估值 160 亿美元，成为纽约最新 AI 基础设施十角兽](#item-6) ⭐️ 8.0/10
7. [IBM 发布 Granite Switch 4.1 统一多模态端点](#item-7) ⭐️ 7.0/10
8. [华为开源 AgentOS Enterprise，打造企业级 Agent 底座](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Hugging Face Transformers v5.20.0 新增 Meta 816B Muse Spark Open 与 Ling 3.0](https://github.com/huggingface/transformers/releases/tag/v5.20.0) ⭐️ 8.0/10

Hugging Face 发布了 Transformers v5.20.0，为多个新模型加入了原生支持，其中最引人注目的是 Meta 的 Muse Spark Open——一个拥有 8160 亿总参数、每 token 激活 420 亿参数、上下文窗口最高达 1,048,576 token 的多模态混合专家模型，以及 InclusionAI 的 Ling 3.0 Flash 混合 MoE 语言模型。该版本还引入了 Kolibri 1、MiniCPM-V 4.7、UnlimitedOcr 和 UltraBERT。 由于 Transformers 是加载和运行开源模型事实上的标准库，原生支持这些架构意味着开发者无需编写自定义代码或使用 trust_remote_code 即可使用 Meta 最大的多模态 MoE 模型和 InclusionAI 的混合注意力模型。这使生态工具链始终与开源权重模型的前沿保持同步。 Muse Spark Open 接受文本、图像、音频和视频输入并输出文本，针对多文件编辑、调试和工具调用等智能体编程任务进行训练，提供 BF16 和 NVFP4 两种格式。Ling 3.0 Flash 将五个 Kimi Delta Attention 层与一个 Multi-head Latent Attention 层分组，并以 BailingHybridForCausalLM 原生加载；UnlimitedOcr 则是一个 3B 参数的 OCR 模型，上下文长度为 32,768 token，用 Reference Sliding Window Attention 替换解码器注意力层以保持 KV 缓存恒定。

github · vasqu · 10月15日 18:05

**背景**: 混合专家（MoE）模型将前馈层拆分为许多专门的“专家”子网络，并只把每个 token 路由到其中少数几个，因此模型可以拥有巨大的总参数量而每个 token 只激活其中一小部分——这正是 Muse Spark Open 总参数达 8160 亿、但每 token 仅激活 420 亿的原因。NVFP4 是随 NVIDIA Blackwell GPU 架构引入的 4 位浮点格式，可在极低精度下实现推理且精度损失很小。像 Ling 3.0 这样的混合注意力设计将不同的注意力机制交错组合（此处为 Kimi Delta Attention 与 Multi-head Latent Attention），以在效率与质量之间取得平衡。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/">Introducing NVFP4 for Efficient and Accurate Low-Precision...</a></li>

</ul>
</details>

**标签**: `#huggingface`, `#transformers`, `#multimodal`, `#mixture-of-experts`, `#llm`

---

<a id="item-2"></a>
## [Meta 发布 816B 开放权重模型 Muse Spark Open](https://research.meta.ai/blog/muse-spark-open) ⭐️ 8.0/10

Meta 发布了 Muse Spark Open，这是一个大型开放权重混合专家模型，总参数量 8160 亿、激活参数 420 亿，并以 Muse-Spark-Open-816B-A42B 的名称发布在 Hugging Face 上。它被称为迄今最强的美国开放权重模型，并针对 Mac Studio 等硬件进行了优化，同时支持 Unsloth、MLX 等多种模型运行器。 这是美国主要实验室对开放权重生态的一次重要投入，而此时 Kimi K3、Qwen3.8 等中国模型正主导着最大规模的开放权重发布。它的许可条款以及与竞品的性能对比，可能影响开发者在生产负载中选择开放模型还是专有模型。 该模型采用混合专家架构，提供两个官方检查点，包括 BF16 版本和旨在降低内存占用的低精度 NVFP4 变体。其许可证允许广泛使用，但当被许可方及其关联方的总营收超过 2000 万美元时，会限制“模型即服务”形式的提供。

hackernews · bigwheels · 10月15日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=50107379)

**背景**: 开放权重模型是指其学习到的参数（权重和偏置）被公开发布的 AI 模型，任何人都可以下载和运行，但修改或再分发的权限取决于许可证。这与开源 AI 不同，后者还会发布源代码、训练数据和技术文档。开放权重发布已成为地缘政治焦点，DeepSeek、阿里云和 Moonshot AI 等中国实验室倾向采用宽松许可证，而许多美国实验室则对较大模型保持专有。Meta 的 Muse Spark 系列既包含闭源消费级模型，也包含这个新的开放权重变体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Open-weight_model">Open-weight model</a></li>
<li><a href="https://huggingface.co/blog/meta-muse-spark-open">Welcome Muse Spark Open : open -weight frontier multimodal...</a></li>

</ul>
</details>

**社区讨论**: 评论者指出，Artificial Analysis 的基准测试显示 Muse Spark Open 的表现不及 Qwen3.8 Flash Next 和 GLM 5.3 Flash，说明 Meta 在开放权重领域还需追赶。其他人则讨论许可证问题，指出 2000 万美元营收条款意味着它并非完全开放；也有人称赞 Meta 努力支持几乎所有模型运行器，并认为 Meta 是在构建具有粘性的生态护城河，而非出租前沿智能。

**标签**: `#AI`, `#open-weight models`, `#Meta`, `#machine learning`, `#model release`

---

<a id="item-3"></a>
## [神经网络是“干净”的：机械可解释性的新论点](https://already-clean.goodfire.com/) ⭐️ 8.0/10

Nick Cammarata 是 OpenAI 早期机械可解释性工作的合著者，他发表了一篇题为《神经网络是干净的》的博客文章，认为神经网络比此前认为的更容易解释，并在 X 上分享了该文章。文章重新审视了著名的“混乱神经元”，检查了工具失败案例，并梳理了多义性在网络中的表现，声称“测序 AI 基因组”可能比该领域设想的更可行。 如果神经网络确实比假设的更容易解释，这可能加速机械可解释性和 AI 对齐研究，因为理解模型正在构建什么被广泛视为解决对齐问题的前提。该文章引发了 184 条评论的实质性辩论，表明这一主张既有高价值又在社区内存在争议。 该博客被描述为一份庞大的证据简报，论证“测序 AI 基因组”比想象中更容易，并包含一个链接，Cammarata 称其为“第一个我觉得自己基本理解的非平凡神经网络”。批评者指出，这些主张可能超出了实际证明的范围，并提到早已为人所知的现象，如渐进式特征复杂性、彩票假设，以及暗示压缩表示的多模态差距研究，这些现象与参数过载并不互斥。

hackernews · themgt · 10月15日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=50105647)

**背景**: 机械可解释性是可解释 AI 的一个子领域，旨在像逆向工程传统软件一样，逆向工程神经网络的内部结构、算法和电路。AI 对齐是引导 AI 系统朝向预期目标和价值观的更广泛挑战，许多研究者认为可解释性对其至关重要，因为我们无法对齐那些内部机制尚不理解的系统。多义性——即单个神经元对多个不相关特征作出响应的现象——长期以来一直是解释神经网络的主要障碍。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mechanistic_interpretability">Mechanistic interpretability</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_alignment">AI alignment</a></li>

</ul>
</details>

**社区讨论**: 评论者意见分歧：一些人称赞 Cammarata 是“一股自然力量”，并强调他的发布帖认为可解释性可能是当今最重要的科学问题；另一些人则认为这些主张超出了已证明的范围，并引用彩票假设和多模态差距研究作为反例。一位评论者将文章的语气比作 Anthropic 机械可解释性团队在首批大规模 SAE 结果出炉时的早期热情，形容其为一种认为已找到关键范式的“轻躁狂能量”。

**标签**: `#interpretability`, `#neural networks`, `#AI alignment`, `#mechanistic interpretability`, `#machine learning`

---

<a id="item-4"></a>
## [Citizen Lab 揭露：定向广告被用于投递零点击间谍软件](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/) ⭐️ 8.0/10

Citizen Lab 发布研究，揭露一家名为 Discover Tech 的以色列公司利用全球在线广告网络，仅通过向设备投放恶意广告，就向数十台设备投递了零点击雇佣间谍软件。该报告被《卫报》、The Verge、TechCrunch、Wired 和《金融时报》等媒体报道，首次提供了通过广告技术基础设施分发间谍软件的技术证据。 这一发现将无处不在的定向广告生态系统变成了国家级监控的潜在攻击面，引发了关于广告技术问责、平台安全和国家安全的紧迫问题。它影响所有看到在线广告的用户，并可能迫使监管机构和广告网络重新思考广告投放的审核与安全机制。 报告详细描述了该攻击活动的分发和命令控制环节，但对激活零点击恶意软件的具体机制语焉不详，一位广告技术工程师批评这一点有夸大之嫌。攻击利用了复杂多方的广告技术供应链，其中并不存在单一的“广告提供商”，这使得责任归属和缓解措施都变得困难。

hackernews · jcomp · 10月15日 10:43 · [社区讨论](https://news.ycombinator.com/item?id=50101813)

**背景**: Citizen Lab 是多伦多大学的一个跨学科研究实验室，研究信息控制，并在揭露针对记者和人权倡导者的间谍软件方面发挥了重要作用。雇佣间谍软件是指出售给政府的商业监控工具，能够远程入侵手机，通常无需用户任何交互（零点击）。零点击攻击尤其危险，因为受害者无需点击链接或打开文件就会被感染。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.wired.com/story/nightmare-scenario-zero-click-spyware-is-infecting-phones-via-targeted-ads/">‘Nightmare Scenario’: Zero-Click Spyware Is Infecting Phones ...</a></li>
<li><a href="https://techcrunch.com/2026/10/15/citizen-lab-says-governments-are-abusing-online-ads-to-hack-people-with-zero-click-spyware/">Governments are hacking people with ' zero-click' spyware by ...</a></li>

</ul>
</details>

**社区讨论**: 评论者讨论了更广泛的影响：一些人呼吁禁止整个在线广告行业，而一位有 13 年经验的广告技术工程师则认为报告在“零点击”方面有夸大之嫌，并指出广告技术生态系统中没有单一可问责的“广告提供商”。其他人则对以色列科技公司与政府监控的联系表示担忧，并质疑以色列为何成为领先的网络强国。

**标签**: `#cybersecurity`, `#spyware`, `#adtech`, `#privacy`, `#zero-click-exploit`

---

<a id="item-5"></a>
## [Anthropic 在 IPO 前向投资者披露第三季度营收达 168 亿美元](https://simonwillison.net/2026/Oct/15/anthropic-tells-investors/) ⭐️ 8.0/10

Anthropic 周三向投资者披露，其第三季度（7 月至 9 月）营收环比增长近 50%，达到 168 亿美元，高于第二季度的 115 亿美元和第一季度的约 48 亿美元。公司还透露，模型蒸馏贡献了 5% 至 7% 的营收，并在第三季度被大幅削减；剔除股权激励后的调整后营业利润率为 11%。 这是外界迄今对一家领先前沿 AI 实验室财务状况最清晰的观察之一，而 Anthropic 正筹备可能高达 1000 亿美元融资、估值约 2 万亿美元的 IPO。此次披露表明前沿模型营收正在快速扩张，但在计入算力成本后利润率依然微薄，同时各大实验室正在积极打击竞争对手的蒸馏行为。 第三季度 Anthropic 每在算力上花费 1 美元，就能产生 1.70 美元营收；剔除股权激励后的调整后营业利润率为 11%，这意味着按 GAAP 计算的利润率会更低。根据披露的 5% 至 7% 蒸馏营收占比推算，仅第二季度竞争对手实验室在蒸馏 Anthropic 模型上的花费就可能超过 5 亿美元；此外，Anthropic 似乎已不再在投资者沟通中强调“年化运行率营收”这一指标。

rss · Simon Willison · 10月15日 13:04

**背景**: 模型蒸馏是一种用更先进模型的输出训练较小或竞争模型的技術，实际上是通过大量 API 调用逆向工程其能力；这一做法颇具争议，因为它让竞争对手得以“搭便车”利用另一家实验室的研究和算力。股权激励是支付给员工的股权，将其从营业利润中剔除后得到的非 GAAP 数字通常比 GAAP 数字更好看。Anthropic 已于 2026 年 6 月 1 日秘密提交 IPO 申请，据报道目标是在 2026 年 11 月上市。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>
<li><a href="https://www.scientificamerican.com/article/what-is-ai-model-distillation-and-why-is-it-so-hard-to-stop/">What is AI model distillation , and why is it so hard to stop?</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic_IPO">Anthropic IPO</a></li>

</ul>
</details>

**标签**: `#Anthropic`, `#AI industry`, `#revenue`, `#IPO`, `#financials`

---

<a id="item-6"></a>
## [Modal 年经常性收入达 10 亿美元、估值 160 亿美元，成为纽约最新 AI 基础设施十角兽](https://www.latent.space/p/ainews-modals-1b-arr-16b-series-d) ⭐️ 8.0/10

Modal 宣布其年经常性收入（ARR）已达到 10 亿美元，同时完成 160 亿美元的 D 轮融资估值，在短短五个月内使用量和估值均增长至三倍，过去一年增长达 15 倍。这使其成为纽约市最新的 AI 基础设施十角兽。 这种快速增长是 AI 基础设施市场的重要信号，表明用于运行 AI 工作负载的无服务器计算平台需求正在急剧加速。这使 Modal 跻身 AI 基础设施公司的精英梯队，并可能加剧云计算和无服务器 GPU 领域的竞争。 Modal 是一个无服务器计算平台，让开发者无需管理基础设施即可运行机器学习推理、微调和批处理等计算密集型工作负载。五个月内使用量和估值增长 3 倍、一年内增长 15 倍，凸显了需求的规模，不过该公告本身提供的技术细节有限。

rss · Latent Space · 10月15日 10:08

**背景**: Modal 是一个无服务器计算平台，让开发者可以轻松在云端运行机器学习推理、微调和批处理等计算密集型工作负载，而无需配置或管理硬件。无服务器计算是一种云服务类别，客户无需自行部署或管理服务器即可使用云能力。十角兽是指估值超过 100 亿美元的初创公司，比 10 亿美元的“独角兽”称号更高一级。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://fourweekmba.com/decacorn/">Decacorn Companies 2026: 10 Giants Worth $10B+... - FourWeekMBA</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#Modal`, `#funding`, `#cloud computing`, `#serverless`

---

<a id="item-7"></a>
## [IBM 发布 Granite Switch 4.1 统一多模态端点](https://huggingface.co/blog/ibm-granite/granite-switch-4-1) ⭐️ 7.0/10

IBM 发布了 Granite Switch 4.1，这是一个统一模型端点，可通过单一托管端点处理聊天、决策和语音任务。其 30B 版本是一个模块化大语言模型，将基础模型、多个适配器和一个编码器组合在一起；Granite 4.1 系列还包括 3B 和 8B 的稠密语言模型，提供基础版和指令微调版。 此次发布通过让开发者以单一集成模式访问聊天、决策和语音能力，而无需管理多个独立模型和 API，从而简化了多模态 AI 的部署。这反映了行业向统一模型 API 发展的趋势，可降低 AI/ML 从业者构建生产应用的运维复杂度。 Granite Switch 4.1 30B 的模块化架构将基础模型、多个适配器和一个编码器组合到单一托管端点中；其语音组件 granite-speech-4.1-2b 是一个紧凑的多语言语音语言模型，由三个组件组成，合并为一个 2B 参数的检查点。Granite 4.1 系列涵盖 3B、8B 和 30B 参数规模，每种均提供基础版和指令微调版。

rss · Hugging Face Blog · 10月15日 20:34

**背景**: Granite 是 IBM 面向企业推出的开源 AI 模型系列，Granite 4.1 是其最新一代稠密语言模型。统一端点意味着开发者向一个 API 地址发送请求，系统会自动将其路由到适合任务的模型或适配器，而无需为聊天、决策和语音分别部署。多模态 AI 指的是能够在单一框架内处理并生成文本、音频等不同类型数据的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/ibm-granite/granite-speech-4.1-2b">ibm- granite / granite - speech - 4 . 1 -2b · Hugging Face</a></li>

</ul>
</details>

**社区讨论**: r/LocalLLaMA 上的社区讨论指出，Granite Switch 4.1 30B 是一个模块化大语言模型，将基础模型、多个适配器和一个编码器组合起来，使单一托管端点能够提供多种能力。r/unsloth 社区也在 IBM Granite 4.1 系列整体发布时关注到了这一版本。

**标签**: `#AI`, `#Machine Learning`, `#Multimodal`, `#IBM Granite`, `#Model Release`

---

<a id="item-8"></a>
## [华为开源 AgentOS Enterprise，打造企业级 Agent 底座](https://news.google.com/rss/articles/CBMitAFBVV95cUxOMUV2SVJSYVRSVTBFRVRJNzFtdWlmUC1pTUJkNGFteVU0UDk5dDhfeHZIZ2JvRW5uODhlR1RpMXdZb0dERDhNeklUbFNiYVVzSjNzQW10YmJnVXhJYXkxR1FBWUxBajRCalR3cmJoNWE3NUZ6ZjNMLXl6UnZuRWF0ZkpPdzB4MjN2NjJaeW1qakduNVIxc2gzaTRoeVJWMTJXTEo0YThVbV9CVG5jd0kyb1BpcmU?oc=5) ⭐️ 7.0/10

华为正式开源了企业级 Agent 底座平台 AgentOS Enterprise，并公开了其架构设计与落地路径。该项目由华为 2012 实验室、华为云、计算、终端及算力先遣队等多个团队联合高校与开发者共同打造，属于 openJiuwen 开源项目的一部分。 这是企业级 AI Agent 基础设施领域的一项重要进展，提供了一个基础平台，有望加速 Agent 系统在企业环境中的采用和标准化。同时，这也使华为成为新兴开源 Agent 生态中的重要参与者，与其他企业级 Agent 平台展开竞争。 该平台被设计为企业级 Agent 底座，强调架构设计与可落地的部署路径。它属于 openJiuwen 项目，由华为多个部门与外部合作伙伴协同开发。

google_news · 积墨 AI · 10月15日 00:00

**背景**: AI Agent 是能够感知环境、做出决策并执行任务以实现目标的自主软件系统，通常基于大语言模型。企业级 Agent 平台提供大规模构建、部署和管理这些 Agent 的基础设施，解决编排、安全以及与现有业务系统集成等挑战。华为此次开源旨在为这类系统提供标准化底座，类似于 Infobip 的 AgentOS 或其他开源 AgentOS 项目。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://accesspath.com/software/agentos-mv0fw9qmxown">华 为 多团队开源Jiuwen AgentOS ，构建企业级多智能体底座 | 前途科技</a></li>
<li><a href="https://www.infobip.com/docs/agentos">AgentOS : Enterprise customer engagement platform | Infobip</a></li>
<li><a href="https://www.agent-os.net/homepage/en">AgentOS - The next-generation operating system for AI Agents</a></li>

</ul>
</details>

**标签**: `#Huawei`, `#AgentOS`, `#enterprise AI`, `#open source`, `#AI agents`

---