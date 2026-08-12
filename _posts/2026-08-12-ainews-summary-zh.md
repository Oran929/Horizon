---
layout: default
title: "AI行业热点: 2026-08-12 (ZH)"
date: 2026-08-12
lang: zh
briefing: ainews
---

> 从 89 条内容中筛选出 11 条重要资讯。

---

1. [Qwen3.8-2.4T-A95B：大规模 MoE 模型逼近前沿性能](#item-1) ⭐️ 9.0/10
2. [原国务院总理朱镕基在北京逝世，享年 98 岁](#item-2) ⭐️ 9.0/10
3. [OpenAI Python SDK v3.0.0 迁移至 HTTPX2](#item-3) ⭐️ 8.0/10
4. [DeepSeek V4 Pro 0813 发布，社区反响热烈](#item-4) ⭐️ 8.0/10
5. [新攻击通过投机解码窃取推理轨迹](#item-5) ⭐️ 8.0/10
6. [英伟达推出首款开源 AI 模型](#item-6) ⭐️ 8.0/10
7. [工程师警告：AI 编码工具侵蚀代码理解能力](#item-7) ⭐️ 7.0/10
8. [自然语言文本不存在无损转换](#item-8) ⭐️ 7.0/10
9. [AI2 推出 OlmoEarth 嵌入，支持自定义地理空间导出](#item-9) ⭐️ 7.0/10
10. [Liquid AI 推出面向边缘视觉的 LFM2.5-VL-3B](#item-10) ⭐️ 7.0/10
11. [UCSD 研究员 AI 创业：4 小时产出顶刊级成果](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Qwen3.8-2.4T-A95B：大规模 MoE 模型逼近前沿性能](https://huggingface.co/Qwen/Qwen3.8-2.4T-A95B) ⭐️ 9.0/10

Qwen 发布了 Qwen3.8-2.4T-A95B，这是一个开放权重的稀疏混合专家模型，总参数 2.4 万亿，活跃参数 950 亿，是 Qwen3.8-Max 的开放权重版本。该模型声称性能接近 Opus 4.5/5 水平，社区强调 397GB 的 1-bit 量化版本可在高端消费级机器上运行。 此次发布将接近前沿的能力带入开放生态系统，可能挑战 Opus 和 Fable 等顶级专有模型。1-bit 量化版本的可用性使得在消费级硬件上本地部署成为可能，使最先进的 AI 更加普及。 完整的 BF16 模型约 4.9TB，而 1-bit 量化版本为 397GB，每个 MoE 有 950 亿活跃参数。模型卡声称性能介于 Opus 4.8 和 Fable 5 之间，并支持最多一百万 token 的上下文。然而，开放权重模型默认缺少视觉输入和 1M 上下文，这些是官方 Qwen3.8-Max 的功能。

hackernews · Philpax · 8月12日 15:01 · [社区讨论](https://news.ycombinator.com/item?id=49273478)

**背景**: 混合专家（MoE）模型每个 token 只激活部分参数，从而在可控计算量下实现巨大参数量。量化通过降低数值精度来减小模型大小，1-bit 量化是一种极端形式，可以大幅缩小模型以便本地部署。Qwen 是领先的开放权重 LLM 系列，此次发布标志着 Qwen 首次开源 Max 级模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developer.nvidia.com/blog/serve-qwen3-8-2-4t-a95b-a-2-4t-parameter-model-with-configurable-reasoning-on-nvidia-gb300-nvl72/">Serve Qwen3.8-2.4T-A95B, a 2.4T-Parameter Model, with ...</a></li>
<li><a href="https://openrouter.ai/qwen/qwen3.8-2.4t-a95b">Qwen3.8 2.4T A95B - API Pricing & Providers | OpenRouter</a></li>

</ul>
</details>

**社区讨论**: 社区评论对 1-bit 量化版本能在消费级硬件上本地部署表示兴奋，有用户指出它使普通人也能获得 Opus 4.5 级别的性能。一些用户指出局限性，如开放权重版本缺少视觉支持和 1M 上下文，并指出由于发布时仅提供 BF16 和 FP8，该模型比竞争对手更难部署。

**标签**: `#AI/ML`, `#Large Language Models`, `#Open Source`, `#Quantization`, `#MoE`

---

<a id="item-2"></a>
## [原国务院总理朱镕基在北京逝世，享年 98 岁](https://www.news.cn/politics/20260812/4c2c72e299ef4561915d2e507393a81f/c.html) ⭐️ 9.0/10

原国务院总理朱镕基因病医治无效，于 2026 年 8 月 12 日在北京逝世，享年 98 岁。中共中央、全国人大常委会、国务院、全国政协发布了官方讣告。 朱镕基是中国经济改革的关键人物，尤其在亚洲金融危机和加入世贸组织谈判中发挥了重要作用。他的逝世标志着一个时代的结束，对中国乃至世界都具有重要的历史和政治意义。 朱镕基 1928 年 10 月生于湖南长沙，1949 年 10 月加入中国共产党。他于 1998 年 3 月出任国务院总理，在亚洲金融危机期间实施积极财政政策和稳健货币政策，并坚持人民币不贬值。

telegram · zaihuapd · 8月12日 10:11

**背景**: 朱镕基是中国著名领导人，以推动中国经济现代化而闻名。他主导了财税、金融、国企、住房和粮食流通等领域的重大改革，帮助建立了社会主义市场经济体制的基本框架。他的任期内还完成了中国加入世界贸易组织的谈判。

**标签**: `#politics`, `#obituary`, `#China`, `#historical figure`

---

<a id="item-3"></a>
## [OpenAI Python SDK v3.0.0 迁移至 HTTPX2](https://github.com/openai/openai-python/releases/tag/v3.0.0) ⭐️ 8.0/10

OpenAI 发布了其官方 Python SDK 的 3.0.0 版本，该版本现在默认使用 HTTPX2 作为 HTTP 客户端。这是一个破坏性变更，httpx 不再自动安装，开发者需要迁移其自定义的 HTTPX 配置。 此次迁移影响了大量依赖 OpenAI Python SDK 的开发者，他们必须更新代码以保持兼容。这也标志着更广泛的生态系统向 HTTPX2 的转变，HTTPX2 由 Pydantic Services Inc. 维护，并且已被 Starlette 采用。 此次更新为尚未准备好迁移的用户提供了一个临时的、仅运行时使用的旧版 HTTPX 逃生通道。迁移指南可在仓库中获取，新的默认客户端名为 DefaultHttpx2Client，支持自定义代理、传输和认证。

github · openai-sdks[bot] · 8月12日 01:54

**背景**: HTTPX 是一个流行的 Python HTTP 客户端，支持同步和异步 API，以及 HTTP/1.1 和 HTTP/2。HTTPX2 是 HTTPX 的继任者，由 Pydantic Services Inc. 维护，原作者为 Tom Christie，旨在满足 Python 生态系统不断变化的需求。OpenAI Python SDK 广泛用于与 OpenAI 的 API 交互，这一变更要求开发者调整其自定义的 HTTP 客户端配置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/openai/openai-python/issues/3375">Consider migrating from httpx to httpx2 · Issue #3375 · openai/openai-python</a></li>
<li><a href="https://github.com/openai/openai-python">GitHub - openai/openai-python: The official Python library for the OpenAI API · GitHub</a></li>
<li><a href="https://pypi.org/project/httpx2/2.10.0/">httpx 2 · PyPI</a></li>

</ul>
</details>

**社区讨论**: GitHub issue 中的社区讨论表明，生态系统正在向 HTTPX2 迁移，Starlette 已经完成迁移。PR 作者指出了迁移的好处，整体情绪似乎是积极的，但一些开发者可能对破坏性变更和迁移工作量有所担忧。

**标签**: `#OpenAI`, `#Python`, `#SDK`, `#HTTPX2`, `#Breaking Change`

---

<a id="item-4"></a>
## [DeepSeek V4 Pro 0813 发布，社区反响热烈](https://openrouter.ai/deepseek/deepseek-v4-pro-0813) ⭐️ 8.0/10

DeepSeek V4 Pro 0813 是 DeepSeek V4 Pro 模型的新快照版本，于 2026 年 8 月 12 日发布，现已通过 OpenRouter 和 DeepSeek API 提供。它拥有 1,048,576 token 的上下文窗口，最大输出 384,000 token，定价为每百万输入 token 0.435 美元，每百万输出 token 0.87 美元。 此次发布意义重大，因为该模型以远低于竞争对手的成本提供了高能力，社区测试显示 DeepSeek V4 Pro 0813 完成任务仅需 0.12 美元，而 Grok 4.6 需要 1.41 美元。这可能加速 DeepSeek 模型在成本敏感的开发与推理场景中的采用。 该模型采用混合专家架构，总参数 1.6 万亿，激活参数 490 亿，支持思考与非思考模式。OpenRouter 上提供了来自 Artificial Analysis 的独立基准测试，且该模型至少由六家提供商提供。

hackernews · explosion-s · 8月12日 16:04 · [社区讨论](https://news.ycombinator.com/item?id=49274600)

**背景**: DeepSeek 是一家以发布开源权重模型和具有竞争力的价格而闻名的中国 AI 公司。V4 Pro 系列是一个大规模混合专家模型家族，Flash 变体是更小、更快的版本。0813 快照是一个增量更新，可能包含性能改进或错误修复。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://lmmarketcap.com/model/deepseek-v4-pro-0813">DeepSeek V 4 Pro 0813 - Pricing & Benchmarks 2026 | LM Market Cap</a></li>
<li><a href="https://models.dev/models/deepseek/deepseek-v4-pro-0813/">DeepSeek V 4 Pro 0813 pricing, providers, and specs | Models .dev</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极但存在分歧。一位用户称赞其在繁重开发任务中的成本效益，另一位用户则发现它在特定任务中比 Grok 4.6 有更多 bug。一些人批评链接选择指向 OpenRouter，建议使用官方 API 或基准测试链接，还有用户提到测试中的视觉渲染问题。

**标签**: `#AI`, `#DeepSeek`, `#model release`, `#LLM`, `#benchmarks`

---

<a id="item-5"></a>
## [新攻击通过投机解码窃取推理轨迹](https://www.latent.space/p/ainews-how-to-steal-a-reasoning-trace) ⭐️ 8.0/10

最近发现了一种新的安全漏洞，攻击者可以利用投机解码从 AI 模型中提取推理轨迹。该技术在一篇最新文章中详细描述，揭示了一种窃取大型语言模型内部推理过程的新方法。 该漏洞对 AI 模型安全和知识产权构成重大威胁，因为推理轨迹可用于模型蒸馏和逆向工程。它凸显了在 AI 推理管道中加强安全防护的必要性，尤其是在投机解码日益普及的背景下。 该攻击利用投机解码中草稿模型与目标模型之间的交互来推断目标的推理轨迹。这种方法可能绕过现有的安全措施，实现未经授权的模型知识提取。

rss · Latent Space · 8月12日 07:11

**背景**: 投机解码是一种推理优化技术，使用较小的草稿模型提出候选令牌，然后由较大的目标模型进行验证，从而减少延迟同时保持输出质量。推理轨迹是模型在生成最终答案之前产生的内部思维链步骤，通常被视为专有和敏感信息。蒸馏攻击旨在通过提取此类信息来复制模型的能力，而这一新方法将攻击面扩展到了投机解码设置。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Speculative_decoding">Speculative decoding</a></li>
<li><a href="https://arxiv.org/pdf/2608.09867">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://www.anthropic.com/news/detecting-and-preventing-distillation-attacks">Detecting and preventing distillation attacks \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI security`, `#model distillation`, `#reasoning traces`, `#speculative decoding`, `#LLM`

---

<a id="item-6"></a>
## [英伟达推出首款开源 AI 模型](https://news.google.com/rss/articles/CBMinwJBVV95cUxNX1IzdDFiREd3eGxTdFVrRTBrOG1IYVBXS0g2U19vaWQtTW1henNGYWZLN09kUmFxX19VRFdXT0Q3SUtJblNITlNiRnU3WDdFaVU5TDF1V05iaTB2X1NTcHBicU9nOC16ZExYcHI1ZkZiaWtvemR3X2hrU2dXczliWjVNVnZrdU9GYWlRRzhnZUI1QWpYcVFqZmhWMzF1Vk5LVG92dGlzWHBSVVA2SGQtbXRJM19nYnM0Sk9RZlF4UTUycUt6UW1MQWNMY0pSeC1yMGhfRnFjbUJxelp0clhjLV80bVd5Uk94UXpzS3JPLWlQTDhmXzU0WG94NUtwNlh6TzhzRUR5bUw5Q1BSaEx1b1JLVVBacjRuMndDMGRRYw?oc=5) ⭐️ 8.0/10

英伟达宣布推出其首款开源 AI 模型，标志着其正式进入开源 AI 领域。该消息通过新浪财经的一篇文章发布，但简短的摘要中未提供模型的具体名称、架构和功能等细节。 此举意义重大，因为英伟达作为 AI 硬件领域的主导者，现在进军开源软件领域，可能通过提供专有模型的替代方案来重塑 AI 生态系统。这可能会影响依赖英伟达生态系统的开发者和研究人员，促进创新和开源 AI 的更广泛采用。 该新闻条目简短，缺乏具体的技术细节，如模型名称、参数数量或预期用途。目前尚不清楚该模型是大型语言模型、视觉模型还是其他类型，也未提及发布日期或许可条款。

google_news · 新浪财经 · 8月12日 04:10

**背景**: 英伟达以其 GPU 和 CUDA 平台而闻名，这些产品广泛应用于 AI 训练和推理。开源 AI 模型，如 Meta（Llama）和 Mistral 的模型，因其透明性和可定制性而受到欢迎，与 OpenAI 的 GPT-4 等专有模型形成对比。英伟达进入这一领域可能会利用其硬件专长，针对自家 GPU 优化模型，从而可能提供性能优势。

**标签**: `#NVIDIA`, `#open-source AI`, `#AI model`, `#industry news`

---

<a id="item-7"></a>
## [工程师警告：AI 编码工具侵蚀代码理解能力](https://simonwillison.net/2026/Aug/12/florian-herrengt/) ⭐️ 7.0/10

Florian Herrengt 的博客文章被 Simon Willison 引用，描绘了开发者使用 Claude 等 AI 助手时失去对代码工作原理的掌握，导致系统复杂到无人能理解的场景。这段引用凸显了人们对 AI 影响软件工程理解能力的日益担忧。 这很重要，因为它凸显了快速采用 AI 辅助开发的一个关键风险：深度代码理解能力可能被侵蚀，从而导致系统难以维护并增加技术债务。这与业界关于在 AI 生产力提升与保持人类理解之间取得平衡的讨论产生共鸣。 这段引用提到了 AI 编码工具“Fable”（可能指 Anthropic 的 Claude Fable），并描述了一个团队反复让 AI 修复 bug 却不理解底层数据流的情况。它强调了“认知债务”和“理解债务”的概念，这些在软件工程文献中越来越受关注。

rss · Simon Willison · 8月12日 15:08

**背景**: 像 Claude Code 和 Fable 这样的 AI 辅助开发工具能快速生成代码，但研究和文章指出了“理解债务”——过度依赖 AI 对人类理解造成的隐性成本。这段引用展示了一个实际场景，即这种债务表现为团队无法调试或维护自己的系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>
<li><a href="https://shekharyadav.com/blog/ai-code-generation-comprehension-debt">The Hidden Cost of AI-Assisted Development: Why Faster Code ...</a></li>
<li><a href="https://medium.com/@addyosmani/comprehension-debt-the-hidden-cost-of-ai-generated-code-285a25dac57e">Comprehension Debt — the hidden cost of AI generated code.</a></li>

</ul>
</details>

**标签**: `#AI`, `#software engineering`, `#code quality`, `#developer experience`, `#future of work`

---

<a id="item-8"></a>
## [自然语言文本不存在无损转换](https://simonwillison.net/2026/Aug/11/there-are-no-lossless-transformations-of-natural-language-text/) ⭐️ 7.0/10

Sophie Alpert 发布了一项针对工程师使用 AI 写作工具的内部政策，指出每一次重写或改写都会改变含义，作者必须对自己文档中的每一个观点和句子负责。 该政策为在 AI 辅助写作中保持作者责任和清晰度提供了实用指南，而 AI 辅助写作在工程和文档领域日益普遍。它解决了在缺乏仔细人工监督的情况下使用 LLM 导致信息丢失的风险，促进了技术沟通质量的提升和信任的建立。 该政策强调，如果审阅者询问某一行内容，不能以“这是 AI 写的”来搪塞。核心观点是自然语言文本不存在无损转换，因此任何由缺乏作者详细心理模型的实体进行的重写都会丢失信息。

rss · Simon Willison · 8月11日 23:48

**背景**: 大型语言模型（LLM）越来越多地被用于辅助写作，包括技术文档。然而，这些模型无法访问作者的原始意图，因此它们进行的任何转换都可能微妙地改变含义。该政策是专业环境中为 AI 使用建立治理和问责制的更广泛趋势的一部分。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=48980425">There are no lossless transformations of natural - language text</a></li>
<li><a href="https://www.linkedin.com/posts/katie-miserany_there-are-no-lossless-transformations-of-activity-7491169182865293312-hLj8">There are no lossless transformations of natural - language text</a></li>

</ul>
</details>

**社区讨论**: 未提供 Hacker News 的讨论内容，但该文章已在 LinkedIn 和 Hacker News 上分享，表明其受到关注。评论可能讨论 AI 辅助与作者责任之间的平衡，一些人同意转换的有损性，另一些人则讨论该政策的实用性。

**标签**: `#AI writing`, `#engineering culture`, `#documentation`, `#LLM`, `#ethics`

---

<a id="item-9"></a>
## [AI2 推出 OlmoEarth 嵌入，支持自定义地理空间导出](https://huggingface.co/blog/allenai/olmoearth-embeddings) ⭐️ 7.0/10

AI2 推出了 OlmoEarth 嵌入功能，这是 OlmoEarth Studio 中的一项新特性，允许用户使用开源的 OlmoEarth 基础模型为任意区域和时间段计算并导出嵌入向量。这支持自定义嵌入导出，用于下游地理空间分析。 这一发布对地理空间机器学习和遥感领域的研究人员和从业者意义重大，因为它提供了一种简化的方式来生成地球观测数据的紧凑数值表示。它降低了将基础模型应用于自定义地理空间任务的门槛，可能加速环境监测和土地利用分类等领域的创新。 OlmoEarth 嵌入基于季节性 Sentinel-2 影像计算，平台可以为任意区域和时间段导出嵌入。根据相关论文，在评估嵌入时，OlmoEarth 在 24 个任务中的 15 个上达到最佳性能，而在完全微调后，在 29 个任务中的 19 个上表现最佳。

rss · Hugging Face Blog · 8月12日 16:14

**背景**: OlmoEarth 是 AI2 开发的一套用于地球观测的开源基础模型。OlmoEarth Studio 是一个端到端平台，允许用户导入或标注训练数据、微调和部署模型，以及可视化或导出输出。嵌入是数据的紧凑数值表示，能够捕获语义特征，从而实现聚类、分类和相似性搜索等高效的下游分析。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://allenai.org/blog/olmoearth-embeddings">Introducing OlmoEarth embeddings: Custom embedding exports from OlmoEarth Studio for downstream analysis | Ai2</a></li>
<li><a href="https://docs.olmoearth.allenai.org/embeddings/">Embeddings | OlmoEarth</a></li>
<li><a href="https://arxiv.org/html/2511.13655">OlmoEarth : Stable Latent Image Modeling for Multimodal Earth ...</a></li>

</ul>
</details>

**标签**: `#embeddings`, `#geospatial`, `#AI2`, `#machine learning`, `#remote sensing`

---

<a id="item-10"></a>
## [Liquid AI 推出面向边缘视觉的 LFM2.5-VL-3B](https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b) ⭐️ 7.0/10

Liquid AI 发布了 LFM2.5-VL-3B，这是一个针对边缘设备优化的 30 亿参数视觉语言模型，声称具有更快更好的视觉能力。该模型已在 Hugging Face 上提供，可在本地硬件上运行。 此次发布对 AI 社区意义重大，因为它将先进的视觉语言能力带到了边缘设备，支持在设备端进行文档理解、物体定位和工具调用，无需依赖云端。它满足了边缘端对高效、保护隐私的 AI 推理日益增长的需求。 该模型基于 Liquid AI 的 LFM2-2.6B 稠密模型，并集成了 SigLIP2 400M NaFlex 编码器，支持原生分辨率图像处理和可变宽高比。其灵活的架构允许开发者通过调整每张图像的视觉 token 数量来平衡性能和速度。

rss · Hugging Face Blog · 8月12日 14:00

**背景**: 视觉语言模型（VLM）结合了视觉和文本理解，能够执行图像描述和视觉问答等任务。边缘 AI 是指在本地设备（如手机、物联网设备）上运行 AI 模型，而不是在云端，这样可以减少延迟、带宽使用和隐私问题。Liquid AI 是一家专注于构建高效、通用 AI 模型以用于边缘部署的公司。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/LiquidAI/lfm2-5-vl-3b">LFM2.5-VL-3B for Better and Faster Vision Capabilities for the Edge</a></li>
<li><a href="https://www.liquid.ai/blog/lfm2-vl-3b-a-new-efficient-vision-language-for-the-edge">LFM2-VL-3B: A New Efficient Vision-Language for the Edge — Blog</a></li>
<li><a href="https://docs.liquid.ai/lfm/models/lfm2-vl-3b">LFM2-VL-3B - Liquid Docs</a></li>

</ul>
</details>

**标签**: `#vision-language model`, `#edge AI`, `#efficient inference`, `#Hugging Face`, `#Liquid AI`

---

<a id="item-11"></a>
## [UCSD 研究员 AI 创业：4 小时产出顶刊级成果](https://news.google.com/rss/articles/CBMiigFBVV95cUxQUmtYaE1WS1MxREs4VE9ibE45a3U3RUdhLWJhel9oOERjNjJsbnkxOGVnYUhib3VzTEFRVG9MTFBKc2N0Rm5zZXFBTUVnckVfSXdxcjRkUWhuTVJnbXNfV3F5d2xsU3RiYlNBd1EtdFpBY20zNC1wWmZvT245QlYxLUNNcTlnbkQ1elE?oc=5) ⭐️ 7.0/10

加州大学圣地亚哥分校的研究员谢澎涛创立了一家 AI 驱动的科研初创公司，声称能在 4 小时内交付顶刊水平的成果。该公司已获得数百万美元融资。 这一进展凸显了利用 AI 加速科学发现的趋势，可能改变研究的开展方式。它有望大幅降低高质量研究的时间和成本，对学术界和工业界都将产生深远影响。 该初创公司利用生成式 AI 和大语言模型来自动化研究流程的部分环节，包括想法生成、实验设计和论文撰写。然而，关于“顶刊水平”成果的具体方法和验证细节尚未完全公开。

google_news · 新浪网 · 8月12日 07:07

**背景**: AI for Science 是一个新兴领域，机器学习模型在研究各阶段提供辅助，从假设生成到数据分析。近期，如 Sakana AI 的“AI 科学家”等自动化研究系统展示了 AI 独立开展研究的潜力，但完全自主仍面临挑战。谢澎涛在 AI 应用于医疗和制造业方面有丰富背景，其工作包括医学图像分割和低秩适应技术的贡献。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pengtaoxie.github.io/">Pengtao Xie</a></li>
<li><a href="https://jacobsschool.ucsd.edu/node/3657">Pengtao Xie | Jacobs School of Engineering</a></li>
<li><a href="https://sakana.ai/ai-scientist/">The AI Scientist: Towards Fully Automated Open-Ended Scientific Discovery</a></li>

</ul>
</details>

**标签**: `#AI`, `#scientific research`, `#startup`, `#funding`, `#UCSD`

---