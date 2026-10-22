---
layout: default
title: "AI行业热点: 2026-10-22 (ZH)"
date: 2026-10-22
lang: zh
briefing: ainews
---

> 从 84 条内容中筛选出 9 条重要资讯。

---

1. [DuckDB 2.0.0 LTS“Cinnamon Teal”发布，带来客户端-服务器模式和触发器](#item-1) ⭐️ 9.0/10
2. [PHP 8.2.35 发布，修复 PHP2Shell 严重远程代码执行漏洞](#item-2) ⭐️ 9.0/10
3. [PHP 核心曝高危 RCE 漏洞，补丁定于 10 月 21 日发布](#item-3) ⭐️ 9.0/10
4. [SpaceX 首次在发射塔臂上成功捕获超重型助推器](#item-4) ⭐️ 9.0/10
5. [DeepSeek 开源 DeepInfer 推理引擎：日处理 155 万亿 token，毛利率约 80%](#item-5) ⭐️ 8.0/10
6. [NVIDIA Kumo Relational 无需训练即在关系数据上超越监督学习](#item-6) ⭐️ 8.0/10
7. [专业化 SLM 词汇表可将推理成本降低 77%](#item-7) ⭐️ 7.0/10
8. [Hugging Face 发布 TorchNeuron 在 AWS Trainium 上的系统级性能分析指南](#item-8) ⭐️ 7.0/10
9. [DeepSeek 推出 V4 系列模型并开放 Harness 开发者预览](#item-9) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [DuckDB 2.0.0 LTS“Cinnamon Teal”发布，带来客户端-服务器模式和触发器](https://duckdb.org/2026/10/21/announcing-duckdb-200) ⭐️ 9.0/10

DuckDB 发布了 2.0.0 LTS 版本，代号“Cinnamon Teal”，这是其迄今为止最大的功能版本，包含完善的 Quack 客户端-服务器协议、异步 I/O、触发器，以及可扩展至 128-192 个 vCPU 的显著性能提升。 此版本将 DuckDB 从进程内分析引擎转变为更完整的数据库系统，可能取代多服务器数据栈，并支持集中式分析服务器等新的生产用例。 Quack 协议支持完整的 DuckDB 功能和多并发写入者，稳定的 C API 现在允许扩展跨版本工作；然而，Quack 的客户端支持仍然有限，不过可以通过扩展使用 Postgres 线协议和 Arrow Flight。

hackernews · nnx · 10月21日 14:01 · [社区讨论](https://news.ycombinator.com/item?id=50181136)

**背景**: DuckDB 是一个进程内 SQL OLAP 数据库管理系统，以简单、快速和可移植著称，常用于分析工作负载。此前，它缺乏客户端-服务器模式，每个连接都是嵌入式的，并且扩展需要为每个版本重新编译。Quack 协议引入了客户端-服务器功能，允许 DuckDB 实例通过 HTTP 通信。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://duckdb.org/2026/10/21/announcing-duckdb-200">Announcing DuckDB 2 . 0 . 0 LTS “Cinnamon Teal” – DuckDB</a></li>
<li><a href="https://duckdb.org/2026/05/12/quack-remote-protocol?ref=bogdandeac.com">Quack: The DuckDB Client - Server Protocol – DuckDB</a></li>
<li><a href="https://www.infoworld.com/article/4210635/duckdb-2-0-coming-this-fall-with-client-server-mode.html">DuckDB 2 . 0 coming this fall with client/server mode | InfoWorld</a></li>

</ul>
</details>

**社区讨论**: 社区反馈非常积极，用户报告在高核心数 EC2 机器（最高 128-192 个 vCPU）上获得显著加速，并成功在生产环境中作为集中式分析服务器使用。许多人认为客户端-服务器支持是游戏规则改变者，可能取代现有数据栈，而触发器使 DuckDB 成为“开箱即用的数据仓库”。

**标签**: `#DuckDB`, `#database`, `#analytics`, `#release`, `#performance`

---

<a id="item-2"></a>
## [PHP 8.2.35 发布，修复 PHP2Shell 严重远程代码执行漏洞](https://github.com/php/php-src/releases/tag/php-8.2.35) ⭐️ 9.0/10

PHP 8.2.35 作为安全更新发布，修复了 PHP2Shell 漏洞（CVE-2026-109618 和 CVE-2026-109619），这是 PHP 核心中的两个严重远程代码执行漏洞，由 Wiz、Calif 和 OpenAI 协调披露。这些漏洞是在 AI 辅助下发现的，CVSS v4.0 评分为 9.2。 这些漏洞允许未经身份验证的攻击者在存在漏洞的 PHP 服务器上执行任意代码，可能泄露敏感数据或中断服务，影响互联网的很大一部分。协调披露和 AI 辅助发现既凸显了 AI 在安全研究中日益增长的作用，也强调了基础架构快速打补丁的迫切需求。 这些漏洞被归类为 CWE-824（访问未初始化的指针），源于 PHP 对异常请求终止的处理，可导致无需身份验证的远程代码执行。Cloudflare 已部署 WAF 防护，但用户应尽快升级到已修复的版本，如 8.2.35、8.3.x 和 8.4.x。

hackernews · tuyuri · 10月21日 13:45 · [社区讨论](https://news.ycombinator.com/item?id=50180873)

**背景**: PHP 是一种广泛使用的开源脚本语言，驱动着大量网站和 Web 应用。远程代码执行（RCE）漏洞是最严重的漏洞类型之一，因为它允许攻击者在服务器上运行任意命令，通常导致系统完全被攻陷。PHP2Shell 指的就是 PHP 核心中的这一系列严重漏洞，披露过程涉及 Wiz、Calif 和 OpenAI 等多个组织，据报道发现过程中使用了 AI 工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.php2shell.com/">PHP 2 Shell — AI uncovers critical vulnerabilities in the backbone of...</a></li>
<li><a href="https://www.tenable.com/blog/php2shell-cve-2026-109618-cve-2026-109619-frequently-asked-questions-about-critical-php-remote">php2shell (CVE-2026-109618, CVE-2026-109619): Critical PHP ...</a></li>
<li><a href="https://blog.cloudflare.com/php-vulnerabilities-waf-protection/">Cloudflare deploys protections against php 2 shell vulnerability</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（963 分，532 条评论）显示出强烈担忧，用户注意到协调披露的链接并猜测可能存在第二个漏洞。一些长期托管 PHP 的用户表示这是他们 20 年来见过的最严重的 PHP 安全事件，其他人则批评发布处理方式和时机，包括 Docker 镜像发布延迟。

**标签**: `#PHP`, `#security`, `#RCE`, `#vulnerability-disclosure`, `#AI-security`

---

<a id="item-3"></a>
## [PHP 核心曝高危 RCE 漏洞，补丁定于 10 月 21 日发布](https://sansec.io/research/php2shell) ⭐️ 9.0/10

PHP 官方团队宣布核心解释器存在两个高危远程代码执行漏洞（CVE-2026-109618 和 CVE-2026-109619，CVSS 9.2），影响自 PHP 5.4 起的所有版本，补丁定于 2026 年 10 月 21 日 22:00（UTC+8）发布。 这些漏洞可在业务框架代码执行前被触发，对几乎所有基于 PHP 的 Web 应用构成极大威胁；且官方仅为受支持分支（8.2-8.5）提供补丁，大量运行停更版本（EOL）的站点将面临持续风险。 漏洞 CVSS 评分为 9.2，属严重级别，影响 PHP 5.x、7.x 及 8.0 至 8.5 等分支；停更（EOL）版本无法获得官方修复，管理员需立即收敛公网访问或实施网络隔离。

telegram · zaihuapd · 10月21日 03:28

**背景**: 远程代码执行（RCE）漏洞允许攻击者在服务器上运行任意代码，通常导致系统被完全控制。CVSS 是一种标准化评分系统，9.0-10.0 分表示严重级别。PHP 是一种广泛使用的服务器端脚本语言，驱动大量网站和应用；当版本停止支持（EOL）后，将不再获得安全更新，已知漏洞无法修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.php.net/supported-versions.php">PHP : Supported Versions</a></li>
<li><a href="https://blog.csdn.net/C20220511/article/details/124747333">CVSS 评 分 策略 分 析及近年来满 分 漏洞盘点-CSDN博客</a></li>
<li><a href="https://www.cnblogs.com/xy586/p/13537137.html">RCE （ 远 程 命令/ 代 码 执 行 漏 洞 ） 原 理 及复现 - 行 云博客 - 博客园</a></li>

</ul>
</details>

**标签**: `#PHP`, `#security`, `#RCE`, `#vulnerability`, `#CVE`

---

<a id="item-4"></a>
## [SpaceX 首次在发射塔臂上成功捕获超重型助推器](https://t.me/zaihuapd/44587) ⭐️ 9.0/10

SpaceX 在得克萨斯州首次用发射塔臂成功捕获了超重型助推器，同时星舰第二级继续飞行，准备在印度洋进行受控溅落。 这是星舰系统实现快速可重复使用的重要里程碑，因为捕获助推器无需着陆腿，能加快飞行间的周转速度，有望大幅降低发射成本。 此次捕获由发射塔的“筷子”机械臂完成，在助推器下降过程中将其在空中夹住；第二级将在印度洋进行受控溅落，延续了逐步推进的测试进程。

telegram · zaihuapd · 10月21日 06:00

**背景**: 星舰是 SpaceX 研发的完全可重复使用两级火箭系统，旨在将人员和货物送往地球轨道、月球和火星。超重型助推器是第一级，用发射塔捕获它是实现快速重复使用的关键一步。此前的试飞中，上级已在印度洋进行过受控溅落。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.space.com/space-exploration/launches-spacecraft/spacex-catches-super-heavy-booster-on-starship-flight-7-test-but-loses-upper-stage-video-photos">SpaceX catches Super Heavy booster on Starship Flight... | Space</a></li>
<li><a href="https://en.wikipedia.org/wiki/SpaceX_Starship">SpaceX Starship - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/List_of_Starship_launches">List of Starship launches - Wikipedia</a></li>

</ul>
</details>

**标签**: `#SpaceX`, `#Starship`, `#spaceflight`, `#reusability`, `#milestone`

---

<a id="item-5"></a>
## [DeepSeek 开源 DeepInfer 推理引擎：日处理 155 万亿 token，毛利率约 80%](https://www.latent.space/p/ainews-deepseek-deepinfer-open-source) ⭐️ 8.0/10

DeepSeek 开源了其生产环境使用的推理框架 DeepInfer，并披露单个集群每天处理 155 万亿个 token，日收入约 2200 万美元，毛利率约 80%，对应约 81 天的回本周期。 这是大型 AI 实验室首次公开生产级推理栈的详细单位经济数据，而将引擎开源可能抬高整个行业的服务效率基准，并在成本上对闭源推理服务商形成压力。 该仓库提供离线推理能力，包含 5 个自定义内核并支持 384 专家的 MoE 模型，据称可达约 9 万 token/s/GPU；但部分观察者指出，155 万亿 token/天和每 GPU 小时 38 美元等头条数字出现在 DeepSeek 的文档中，并不能直接从代码中复现。

rss · Latent Space · 10月21日 06:54

**背景**: DeepInfer 是 DeepSeek API 背后的服务引擎，针对其混合专家（MoE）模型（如采用稀疏注意力降低推理成本的 V3.2）进行了优化。随着大模型服务商在价格上竞争，推理经济性——每 GPU 每小时服务的 token 数、毛利率和回本周期——已成为关键指标。将生产级推理栈开源，使其他团队能够对标并采用相同的技术。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/deepseek-ai/DeepInfer">GitHub - deepseek -ai/ DeepInfer : DeepInfer : High-performance...</a></li>
<li><a href="https://dev.to/976905690/deepseek-open-sources-deepinfer-the-engine-serving-155-trillion-tokens-a-day-13jg">DeepSeek Open-Sources DeepInfer, the Engine Serving 155 ...</a></li>
<li><a href="https://www.explainx.ai/blog/deepseek-deepinfer-open-source-inference-engine-v4-1-flash-155-trillion-tokens-claimed-vs-verified-2026">DeepSeek DeepInfer: Open Engine, 155T Tokens/Day Claim ...</a></li>

</ul>
</details>

**标签**: `#AI inference`, `#open source`, `#DeepSeek`, `#economics`, `#LLM infrastructure`

---

<a id="item-6"></a>
## [NVIDIA Kumo Relational 无需训练即在关系数据上超越监督学习](https://huggingface.co/blog/nvidia/kumo-relational) ⭐️ 8.0/10

NVIDIA 推出了 Kumo Relational，这是一个基于上下文学习的预训练基础模型，用于跨相关表的分类和回归任务，无需任何训练即可在关系数据上超越监督机器学习。该模型基于 KumoRFM-2，并以 NIM 微服务（1.0.0 版本）形式提供，通过结构化数据 API 接受 JSON 数组格式的关系数据负载。 这种零训练方法可能显著影响从业者处理表格和关系任务的方式，因为它消除了任务特定模型训练和微调的需要。来自 NVIDIA 这样的主要参与者的公告增加了可信度，并可能加速企业关系数据库基础模型的采用。 Kumo Relational 是一个预训练基础模型，使用上下文学习在相关表之间执行分类和回归，并作为 NIM 微服务提供，具有验证任务和模式的结构化数据 API。PyPI 上提供了轻量客户端库 kumo-relational-client，用于向模型分派类型化请求。

rss · Hugging Face Blog · 10月21日 18:26

**背景**: 关系数据（例如具有互连表的企业数据库）很常见，但对机器学习来说具有挑战性，因为必须捕获表之间的关系。传统的监督机器学习需要为每个任务训练单独的模型，这可能既耗时又耗费资源。零样本学习旨在无需任务特定训练的情况下泛化到新任务，而最近诸如 Relational Transformer 等进展已在该领域显示出前景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/nvidia/Kumo-Relational">nvidia / Kumo - Relational · Hugging Face</a></li>
<li><a href="https://build.nvidia.com/nvidia/kumo-relational.md">build. nvidia .com/ nvidia / kumo - relational .md</a></li>
<li><a href="https://pypi.org/project/kumo-relational-client/">Client for the NVIDIA Kumo Relational structured-data foundation...</a></li>

</ul>
</details>

**标签**: `#relational data`, `#machine learning`, `#NVIDIA`, `#zero-shot`, `#tabular data`

---

<a id="item-7"></a>
## [专业化 SLM 词汇表可将推理成本降低 77%](https://huggingface.co/blog/Dharma-AI/vocabx-vocabulary-specialization) ⭐️ 7.0/10

Dharma-AI 在 Hugging Face 博客中详细介绍了如何通过将小语言模型（SLM）的词汇表专业化到特定领域，在实际应用中将推理成本降低了 77%。 这展示了一种实用的 SLM 部署优化方法，表明词汇专业化可以显著降低推理成本，对于希望高效部署 SLM 的从业者来说很有价值。 该方法涉及将模型的词汇表定制到目标领域，从而减少所需的 token 数量，进而降低计算成本；然而，该案例研究是供应商特定的，可能不适用于所有领域。

rss · Hugging Face Blog · 10月21日 17:35

**背景**: 小语言模型（SLM）是参数比大语言模型（LLM）少的人工智能模型，旨在高效执行特定任务。词汇专业化是一种将模型的 token 词汇表适配到特定领域的技术，可以提高性能并降低成本。推理成本是指运行模型所需的计算资源，降低它对于大规模部署人工智能至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ibm.com/think/topics/small-language-models">What are Small Language Models ( SLM )? | IBM</a></li>
<li><a href="https://arxiv.org/pdf/2409.02060">OLMoE: Open Mixture-of-Experts Language Models</a></li>
<li><a href="https://www.morphllm.com/llm-inference-optimization">LLM Inference Optimization: Cut Cost & Latency at Every Layer ...</a></li>

</ul>
</details>

**标签**: `#small language models`, `#inference optimization`, `#vocabulary specialization`, `#cost reduction`, `#NLP`

---

<a id="item-8"></a>
## [Hugging Face 发布 TorchNeuron 在 AWS Trainium 上的系统级性能分析指南](https://huggingface.co/blog/amazon/profiling-torchneuron-part-1) ⭐️ 7.0/10

Hugging Face 发布了一篇博客文章（第一部分），详细介绍了 TorchNeuron（AWS Trainium 的 PyTorch 后端）的系统级性能分析技术，涵盖了相关工具和性能分析的最佳实践。 该指南通过提供结构化的性能分析方法，帮助从业者优化在 AWS Trainium（一种定制 AI 加速器）上的 PyTorch 工作负载，从而提升性能和成本效率。 文章聚焦于系统级性能分析，可能涵盖 Neuron SDK 工具（如 Neuron Explorer 和 TensorBoard 集成），并讨论如何识别 Trainium 的 NeuronCore-v2 架构中的瓶颈。

rss · Hugging Face Blog · 10月21日 16:04

**背景**: TorchNeuron 是一个开源的 PyTorch 后端，允许在不重写代码的情况下在 AWS Trainium 芯片上运行现有的 PyTorch 代码。Trainium 是 AWS 第二代专用机器学习加速器，每个 Trn1 实例包含 16 个芯片，每个芯片有两个 NeuronCore-v2。系统级性能分析对于理解此类定制硬件的性能特征和优化工作负载至关重要。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.aboutamazon.com/news/innovation-at-amazon/torchneuron-pytorch-aws-trainium-chips-ai">Amazon 's TorchNeuron runs PyTorch on AWS Trainium chips</a></li>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/latest/general/arch/neuron-hardware/trainium.html">Trainium Architecture — AWS Neuron Documentation</a></li>
<li><a href="https://awsdocs-neuron.readthedocs-hosted.com/en/latest/frameworks/torch/index.html?index.html=">PyTorch Support on Neuron — AWS Neuron Documentation</a></li>

</ul>
</details>

**标签**: `#profiling`, `#AWS Trainium`, `#TorchNeuron`, `#performance`, `#AI accelerators`

---

<a id="item-9"></a>
## [DeepSeek 推出 V4 系列模型并开放 Harness 开发者预览](https://news.google.com/rss/articles/CBMiSEFVX3lxTE4wd0JWNXNkT3NmUy1UV09ldm1iSXY3dTllQ1o1ZFg5MFZPS1BRY3RCTUJLc05UYWJTb1R6VHhoT0NXM3hJQU5xLQ?oc=5) ⭐️ 7.0/10

DeepSeek 已发布完整的 V4 系列模型，包括 V4-Pro 和 V4-Flash，并开放了 DeepSeek Harness 的开发者预览版，这是一个全新的插件优先本地智能体运行时。Harness 预览版最初于 8 月 13 日发布，采用 MIT 许可证开源，允许开发者测试其可组合的插件架构。 V4 系列凭借高效的混合专家设计和百万 token 上下文，提升了 DeepSeek 在大语言模型市场的地位；而 Harness 为开发者提供了一个灵活、开放的 AI 智能体工作流构建与扩展平台。这一组合有望加速 DeepSeek 模型在企业及开发者工具生态中的采用。 V4 系列包含两个模型：V4-Pro 总参数 1.6 万亿（激活 490 亿），V4-Flash 总参数 2840 亿（激活 130 亿），两者均支持 100 万 token 的上下文长度，并以 MIT 许可证开放权重。DeepSeek Harness 是一个本地插件运行时（版本 0.1.2-rc.1），提供模型、工具、技能、会话、沙箱、存储、循环、调度以及 Web 界面等插件。

google_news · 财联社 · 10月21日 11:42

**背景**: DeepSeek 是一家中国 AI 公司，以发布开放权重的大语言模型而闻名。V4 系列采用混合专家（MoE）架构，每个 token 仅激活部分参数以提高效率。DeepSeek Harness 是一款新的开发者工具，作为本地智能体运行时，让用户通过可组合插件处理文档、分析表格、编写代码和调度任务。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.sitepoint.com/deepseek-harness-developer-preview/">DeepSeek Harness : Everything-is-a-Plugin Developer Preview</a></li>
<li><a href="https://deepseek.ai/deepseek-v4">DeepSeek V4 Explained: V4-Pro 1.6T vs V4-Flash 284B (2026)</a></li>
<li><a href="https://arxiv.org/abs/2606.19348">[2606.19348] DeepSeek-V4: Towards Highly Efficient Million ...</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#LLM`, `#AI models`, `#developer tools`, `#model release`

---