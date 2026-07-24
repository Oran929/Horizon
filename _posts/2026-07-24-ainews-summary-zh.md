---
layout: default
title: "AI行业热点: 2026-07-24 (ZH)"
date: 2026-07-24
lang: zh
briefing: ainews
---

> 从 149 条内容中筛选出 13 条重要资讯。

---

1. [Anthropic 发布 Claude Opus 5 模型](#item-1) ⭐️ 9.0/10
2. [黑森林实验室发布 FLUX 3 多模态模型](#item-2) ⭐️ 9.0/10
3. [编译器将计算图转化为 Transformer 权重](#item-3) ⭐️ 9.0/10
4. [两位中国数学家获 2026 年菲尔兹奖](#item-4) ⭐️ 9.0/10
5. [Postgres LISTEN/NOTIFY 实际可扩展到每秒 6 万条](#item-5) ⭐️ 8.0/10
6. [Anthropic 发布 Opus 5，性能逼近 Fable 5，价格减半，刷新 ARC-AGI-3 纪录](#item-6) ⭐️ 8.0/10
7. [AMD 向 Anthropic 投资高达 50 亿美元，锁定 AI 硬件协议](#item-7) ⭐️ 8.0/10
8. [OpenAI 锁定佐治亚州 3.2 吉瓦数据中心，面临公众反对](#item-8) ⭐️ 7.0/10
9. [白宫 AI 审查截止日凸显从自愿到强制合规的转变](#item-9) ⭐️ 7.0/10
10. [Kimi K3 刷屏：全球 AI 产业的一次压力测试](#item-10) ⭐️ 7.0/10
11. [黄仁勋力挺中国开源 AI 模型](#item-11) ⭐️ 7.0/10
12. [华为：网络带宽成 AI 最大瓶颈，Token 调用量涨 6 倍](#item-12) ⭐️ 7.0/10
13. [AMD 发布面向智能体与物理 AI 的全栈算力战略](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Anthropic 发布 Claude Opus 5 模型](https://www.anthropic.com/news/claude-opus-5) ⭐️ 9.0/10

Anthropic 发布了 Claude Opus 5，这是一款新的旗舰 AI 模型，在所有平台上均可使用，价格为每百万输入 token 5 美元、每百万输出 token 25 美元，且通用访问无需数据保留要求。 Claude Opus 5 为组织提供了顶级模型，且没有 Anthropic 早期 Fable 模型的 30 天数据保留政策，使其适用于敏感数据场景。其在图像转 HTML 等视觉任务中的强劲表现，使其在多模态 AI 领域处于领先地位。 Claude Opus 5 的定价与 Opus 4.8 相同，并延续了前代许多风格特征，例如使用“carry the argument”和“worth stating plainly”等短语。该模型在正式发布前曾于 2026 年 7 月以“Honeycomb EAP”名称首次亮相。

hackernews · alvis · 7月24日 16:57 · [社区讨论](https://news.ycombinator.com/item?id=49038433)

**背景**: Anthropic 的 Claude 模型是专为安全性和有用性设计的大型语言模型。Opus 系列代表最高能力层级，而 Fable 是另一条具有更严格数据保留政策的模型线。数据保留要求会影响组织如何使用涉及敏感信息的 AI 模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www-cdn.anthropic.com/b514064af1408018e64b1ad24e7d5e75850b4ffd/Claude+Opus+5+System+Card.pdf">Claude Opus 5 System Card</a></li>
<li><a href="https://news.ycombinator.com/item?id=49038433">Claude Opus 5 | Hacker News</a></li>
<li><a href="https://kie.ai/blog/what-is-claude-opus-5">What Is Claude Opus 5 ? Anthropic's Honeycomb Flagship</a></li>

</ul>
</details>

**社区讨论**: 社区成员强调，无数据保留要求是一个关键区别，一位用户指出这使得组织可以使用“类似 Fable”的模型而无需遵守 Fable 的 30 天政策。另一位用户报告称，Opus 5 在图像转 HTML 转换中优于 Fable，结果更准确。一些用户还评论了模型的写作风格，观察到它保留了 Opus 4.8 中经典的“Claude 式”表达。

**标签**: `#AI`, `#LLM`, `#Anthropic`, `#Claude Opus 5`, `#machine learning`

---

<a id="item-2"></a>
## [黑森林实验室发布 FLUX 3 多模态模型](https://www.latent.space/p/ainews-black-forest-labs-flux-3-multimodal) ⭐️ 9.0/10

黑森林实验室发布了 FLUX 3，这是一个统一图像、视频、音频和动作预测的多模态流模型，性能超越了 Seedance 2.0、Gemini Omni 和 Grok Imagine。他们还推出了 FLUX-mimic，一个视频-动作机器人模型，能从视频模型中提取世界表征用于机器人控制。 FLUX 3 代表了向统一多模态 AI 迈出的重要一步，可能减少对不同模态单独模型的需求。FLUX-mimic 机器人应用表明，视频生成模型可以直接将世界理解迁移到物理机器人上，为具身 AI 开辟了新途径。 FLUX 3 基于 Self-Flow 构建，这是 BFL 在单一架构中对齐多模态生成与理解的方法。该模型处理图像、视频、音频和动作预测任务，其机器人变体在重新安装车窗饰条等真实世界操作任务中展示了有前景的结果。

rss · Latent Space · 7月24日 04:30

**背景**: 多模态 AI 模型旨在一个系统中处理和生成多种数据类型（如文本、图像、视频、音频）。流模型是一类生成模型，通过连续过程学习将噪声转化为数据。黑森林实验室以其早期的 FLUX 系列图像生成模型而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://bfl.ai/blog/flux-3">FLUX 3 - Real World Models : Towards Multimodal Flow Models as...</a></li>
<li><a href="https://korshunov.ai/en/article/13963-flux-3-introduces-a-multimodal-flow-model-for-image-video-audio-and-action/">FLUX 3 introduces a multimodal flow model for image, video, audio...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Seedance_2.0">Seedance 2.0</a></li>

</ul>
</details>

**社区讨论**: 评论者对机器人应用印象深刻，指出视频模型的内部世界表征可以被提取并有效部署到机器人上。一些人对解耦表征的复杂性表示担忧，而另一些人则感叹尽管 AI 取得了进步，现代电影往往缺乏高质量的叙事。

**标签**: `#AI`, `#multimodal`, `#machine learning`, `#robotics`, `#generative models`

---

<a id="item-3"></a>
## [编译器将计算图转化为 Transformer 权重](https://www.reddit.com/r/MachineLearning/comments/1v5fxbe/i_built_a_compiler_that_turns_computation_graphs/) ⭐️ 9.0/10

一个新的编译器 TorchWright 可以将任意用 Python 定义的计算图转化为标准 Phi-3 Transformer 的权重，生成一个无需训练即可在原生 Hugging Face 中加载的检查点。 这项工作通过将算法直接编译到标准 Transformer 架构中，连接了程序合成和机制可解释性，可能使研究人员能够精确研究 Transformer 能表达哪些计算。 该编译器针对 Phi-3 架构，输出标准的 Hugging Face 检查点，无需自定义代码或 trust_remote_code，仓库中包含 12 个可运行示例来演示该方法。

reddit · r/MachineLearning · /u/notforrob · 7月24日 16:15

**背景**: 先前的工作如 RASP 和 Tracr 将领域特定语言编译为 Transformer 权重，但需要自定义架构或非标准代码。TorchWright 通过使用普通 Python 并针对广泛使用的标准架构（Phi-3）改进了这一点，使编译后的 Transformer 可直接在标准推理流程中使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/docs/transformers/en/model_doc/phi3">Phi-3 · Hugging Face</a></li>
<li><a href="https://github.com/google-deepmind/tracr">GitHub - google-deepmind/tracr</a></li>
<li><a href="https://arxiv.org/abs/2106.06981">[2106.06981] Thinking Like Transformers</a></li>

</ul>
</details>

**社区讨论**: 社区讨论内容充实，用户称赞这项工作的新颖性和实用价值。一些评论者讨论了在机制可解释性和程序合成中的潜在应用，另一些人则提出了关于可扩展性和该方法表达力限制的问题。

**标签**: `#transformer`, `#compiler`, `#mechanistic interpretability`, `#machine learning`, `#program synthesis`

---

<a id="item-4"></a>
## [两位中国数学家获 2026 年菲尔兹奖](https://t.me/zaihuapd/42748) ⭐️ 9.0/10

国际数学联盟公布了 2026 年菲尔兹奖得主，中国数学家邓煜和 John Pardon 因其在偏微分方程和辛几何领域的突破性贡献获奖。 这是首次有两位中国籍数学家同时获得菲尔兹奖，对华人数学界具有里程碑意义，也彰显了中国在纯数学领域日益增长的全球影响力。 邓煜因从硬球动力学严格推导出玻尔兹曼方程以及在非线性薛定谔动力学中的概率方法而获奖；John Pardon 因在辛几何中提出虚拟基本循环的新方法和全纯曲线计数而获奖。

telegram · zaihuapd · 7月24日 12:51

**背景**: 菲尔兹奖被誉为数学界的诺贝尔奖，每四年颁发一次，授予 40 岁以下做出杰出贡献的数学家。玻尔兹曼方程描述气体的统计行为，从牛顿力学推导该方程是长期未解决的希尔伯特第六问题。辛几何是微分几何的一个分支，研究辛流形，与数学物理有深刻联系。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.com/zh-cn/科学/数学/125年难题-邓煜团队如何从微观牛顿力学推导出玻尔兹曼方程/ar-AA28njv3">125年难题：邓煜团队如何从微观牛顿力学推导出玻尔兹曼方程?</a></li>
<li><a href="https://www.alphaxiv.org/zh/overview/2408.07818">硬球动力学到玻尔兹曼方程的长期推导 | alphaXiv</a></li>
<li><a href="https://www.sohu.com/a/1050192016_348129">邓煜：证明了希尔伯特第六问题的核心部分——玻尔兹曼方程长期有效性_微...</a></li>

</ul>
</details>

**标签**: `#菲尔兹奖`, `#数学`, `#中国数学家`, `#偏微分方程`, `#辛几何`

---

<a id="item-5"></a>
## [Postgres LISTEN/NOTIFY 实际可扩展到每秒 6 万条](https://www.dbos.dev/blog/postgres-listen-notify-scalability) ⭐️ 8.0/10

DBOS 的新基准测试表明，Postgres LISTEN/NOTIFY 在单台服务器上每秒可处理 6 万条通知，延迟为毫秒级，这与之前声称其不可扩展的说法相矛盾。 这一发现纠正了普遍的误解，表明 LISTEN/NOTIFY 适用于许多实时应用，如聊天、实时更新和事件驱动的工作流，而无需外部消息代理。 该基准测试在单台 Postgres 服务器上实现了每秒 6 万次写入，延迟为毫秒级，优化涉及仔细的连接管理和批处理。

hackernews · KraftyOne · 7月24日 19:05 · [社区讨论](https://news.ycombinator.com/item?id=49040296)

**背景**: Postgres LISTEN/NOTIFY 是一个内置的发布/订阅机制，允许进程在数据库内发送和接收通知。它完全在内存中运行，不持久化消息，因此轻量，但历史上被认为不适合高吞吐场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.postgresql.org/docs/current/sql-notify.html">PostgreSQL: Documentation: 18: NOTIFY</a></li>
<li><a href="https://neon.com/guides/pub-sub-listen-notify">Using LISTEN and NOTIFY for Pub/Sub in PostgreSQL - Neon Guides</a></li>
<li><a href="https://www.dbos.dev/blog/postgres-listen-notify-scalability">Postgres LISTEN/NOTIFY Actually Scales | DBOS</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的社区讨论引用了一篇之前声称 LISTEN/NOTIFY 不可扩展的帖子，一些评论者指出，之前帖子的性能问题可能是由于旧版本或配置不当造成的。其他人强调可扩展性是一个连续体，每秒 6 万条对许多用例足够，但并非所有。

**标签**: `#PostgreSQL`, `#scalability`, `#database`, `#performance`, `#LISTEN/NOTIFY`

---

<a id="item-6"></a>
## [Anthropic 发布 Opus 5，性能逼近 Fable 5，价格减半，刷新 ARC-AGI-3 纪录](https://finance.sina.com.cn/world/2026-07-25/doc-iniiyimr4545772.shtml) ⭐️ 8.0/10

Anthropic 发布了 Claude Opus 5，该模型性能接近其旗舰产品 Fable 5，但价格仅为后者的一半，并在 ARC-AGI-3 基准测试中创下新纪录。 此次发布以显著更低的价格提供接近前沿的智能，加剧了 AI 模型市场的竞争，可能使更多用户和应用能够使用先进的 AI。 Opus 5 专为日常使用设计，在推理、编码和长期代理任务中表现出色，而 Fable 5 仍是编码和代理的最佳模型。ARC-AGI-3 基准测试是针对 AI 代理的交互式推理测试。

gdelt · finance.sina.com.cn · 7月24日 23:00

**背景**: Anthropic 的 Claude 模型系列包括 Opus 和 Fable 等层级，其中 Fable 是最智能的。ARC-AGI 基准测试通过视觉网格谜题衡量抽象推理和流体智能，ARC-AGI-3 是最新的交互式版本。AI 行业正经历快速的模型发布和价格竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/news/claude-opus-5">Introducing Claude Opus 5 \ Anthropic</a></li>
<li><a href="https://arcprize.org/arc-agi/3">ARC-AGI-3</a></li>
<li><a href="https://www.anthropic.com/claude/fable">Claude Fable \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AI`, `#Anthropic`, `#Opus 5`, `#ARC-AGI`, `#model performance`

---

<a id="item-7"></a>
## [AMD 向 Anthropic 投资高达 50 亿美元，锁定 AI 硬件协议](http://www.saltlakecitysun.com/news/279203585/amd-invests-up-to-usd5-billion-in-anthropic-secures-ai-deal) ⭐️ 8.0/10

AMD 宣布向 Anthropic 投资高达 50 亿美元，并达成协议，通过 Helios AI 机架系统提供高达 2 吉瓦的 Instinct MI450 AI 芯片。 此次合作使 AMD 成为领先 AI 安全公司的关键硬件供应商，挑战英伟达在 AI 芯片市场的主导地位，并可能重塑 AI 硬件格局。 该协议包括高达 2 吉瓦的 Instinct MI450 算力，这笔投资是 AI 公司通过股权投资锁定硬件资源的更广泛趋势的一部分。

gdelt · saltlakecitysun.com · 7月24日 23:00

**背景**: Anthropic 是一家由前 OpenAI 员工创立的 AI 安全公司，以其 Claude 大语言模型闻名。AMD 是一家主要的半导体公司，在 AI 加速器市场与英伟达竞争。Instinct MI450 是 AMD 最新的 AI 芯片，专为大规模训练和推理设计。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://wccftech.com/amd-lands-anthropic-in-2gw-instinct-mi450-deal-backing-it-with-a-5-billion-equity-bet/">AMD Lands Anthropic In 2GW Instinct MI450 Deal , Backing It With...</a></li>
<li><a href="https://en.wikipedia.org/wiki/Anthropic">Anthropic - Wikipedia</a></li>
<li><a href="https://www.anthropic.com/">Home \ Anthropic</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Anthropic`, `#AI`, `#investment`, `#hardware`

---

<a id="item-8"></a>
## [OpenAI 锁定佐治亚州 3.2 吉瓦数据中心，面临公众反对](https://www.techtimes.com/articles/321460/20260724/openai-locks-32-gigawatts-georgia-data-center-despite-public-backlash.htm) ⭐️ 7.0/10

2026 年 7 月 22 日，OpenAI 宣布了“Project Camellia”，一个位于佐治亚州萨凡纳附近、耗资 300 亿美元、功率达 3.2 吉瓦的数据中心，标志着其从主要云客户转变为美国最大 AI 园区之一的牵头开发商。 这一大规模基础设施投资表明 OpenAI 致力于扩展 AI 计算资源，但公众的反对凸显了 AI 扩张与当地对能源、水资源和环境影响担忧之间日益紧张的关系。 3.2 吉瓦的容量足以为超过 64 万户普通美国家庭供电，该项目采用闭环冷却系统以限制淡水使用，回应了此前佐治亚州和怀俄明州数据中心争议中的批评。

gdelt · techtimes.com · 7月24日 23:00

**背景**: 数据中心消耗大量电力；2023 年全球数据中心使用了 7.4 吉瓦，而美国数据中心目前占全部电力消耗的 4.4%。OpenAI 的 3.2 吉瓦设施本身就将占其中很大一部分，引发了对电网压力和环境影响的担忧。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://cybernews.com/ai-news/openais-georgia-facility-aims-avoid-backlash/">OpenAI 's Georgia facility aims to avoid the backlash hitting AI data ...</a></li>
<li><a href="https://thenextweb.com/news/openai-georgia-data-centre-30-billion-stargate">OpenAI plans a $30bn, 3.2GW data centre in Georgia</a></li>
<li><a href="https://www.remio.ai/post/openai-georgia-data-center-plan-raises-its-compute-bet-to-750-billion">OpenAI Georgia Data Center Plan Raises Its Compute Bet to $750...</a></li>

</ul>
</details>

**标签**: `#AI`, `#data center`, `#infrastructure`, `#OpenAI`, `#energy`

---

<a id="item-9"></a>
## [白宫 AI 审查截止日凸显从自愿到强制合规的转变](https://www.techtimes.com/articles/321497/20260724/voluntary-paper-mandatory-practice-white-house-ai-review-hits-august-1-deadline.htm) ⭐️ 7.0/10

白宫 AI 审查的 8 月 1 日截止日期临近，标志着 AI 开发者从自愿准则向强制合规的转变。 这一转变可能为全球 AI 监管树立先例，影响公司开发和部署 AI 系统的方式，并可能提高问责性和安全标准。 审查要求 AI 公司证明符合安全和透明度标准，不合规可能面临处罚，但具体执行机制尚不明确。

gdelt · techtimes.com · 7月24日 23:00

**背景**: 白宫一直在制定 AI 政策以平衡创新与风险缓解。主要 AI 公司早前的自愿承诺现在正被正式化为强制性要求，反映出对 AI 风险的日益关注。

**标签**: `#AI regulation`, `#White House`, `#policy`, `#compliance`

---

<a id="item-10"></a>
## [Kimi K3 刷屏：全球 AI 产业的一次压力测试](https://news.google.com/rss/articles/CBMif0FVX3lxTE1iZDdtQmRwUFJlS3Y4ZklIN0hmRkMycHdMQmNLbFV6czU2dGpHZnpwTnYxdWxZenp3Q05sVkxVZHRReHA5T0RGcGVlRDVNOGh0TVdfMjBOdDhnSGZyRUd1RWk1UjFQVTBSUnh2YVRRcTVSUGpBRGlQMGFHbVlQczQ?oc=5) ⭐️ 7.0/10

月之暗面（Moonshot AI）推出的 2.8 万亿参数多模态 AI 模型 Kimi K3 在网络上刷屏，引发广泛讨论，分析师认为这是对全球 AI 产业的一次压力测试。 这一事件凸显了 AI 领域的激烈竞争以及模型在真实场景中接受压力测试的必要性，可能影响企业开发和部署 AI 系统的方式。 Kimi K3 拥有 2.8 万亿参数、原生视觉能力、100 万 token 上下文窗口，并以开放权重形式发布，使其直接与顶级 AI 实验室的最强模型竞争。

google_news · 新浪网 · 7月24日 08:49

**背景**: Kimi K3 是由中国 AI 初创公司月之暗面（Moonshot AI）开发的大型语言模型。该模型的刷屏现象被解读为一次现实世界的压力测试，评估其在海量用户负载和多样化任务下的表现，超越了受控基准测试。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.kimi.com/blog/kimi-k3">Kimi K 3 Tech Blog: Open Frontier Intelligence</a></li>
<li><a href="https://openrouter.ai/moonshotai/kimi-k3">Kimi K 3 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://linas.substack.com/p/kimi-k3-ultimate-guide">The Ultimate Guide to Kimi K3: Benchmarks, Pricing, Prompts</a></li>

</ul>
</details>

**标签**: `#AI`, `#industry analysis`, `#stress test`, `#Kimi K3`

---

<a id="item-11"></a>
## [黄仁勋力挺中国开源 AI 模型](https://news.google.com/rss/articles/CBMiY0FVX3lxTFBVbWhjX0NFOVlfU090d0daZlNneGFlVVk1SDlscXhOZFFNRjlvNU5peG83Wk5RdUNZTzBEQldXdlhaTnlqNklIOEtqMER6NkJoVi1jcnAzNE1DQkZ6S0J2a1NtOA?oc=5) ⭐️ 7.0/10

英伟达 CEO 黄仁勋公开表示，美国不应害怕 DeepSeek、Kimi 等中国开源 AI 模型，他认为这些模型的广泛使用对整个 AI 行业都有好处。 这位行业关键人物的高调背书挑战了“中国 AI 模型构成威胁”的说法，并凸显了开源与专有 AI 商业模式之间日益加剧的紧张关系。 黄仁勋发表此番言论之际，OpenAI 和 Anthropic 等专有 AI 公司担心更便宜的开源模型会侵蚀其付费先进模型的市场。DeepSeek 和 Kimi 是知名的中国开源模型，具有大上下文窗口和强劲性能。

google_news · 新浪网 · 7月24日 14:34

**背景**: 开源 AI 模型是公开可用的，任何人都可以免费使用、修改和分发。这与 OpenAI 和 Anthropic 等公司的专有模型形成对比，后者通常通过付费 API 访问。DeepSeek 和 Kimi 是中国开发的开源模型，因其能力而获得了广泛关注。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Kimi_(chatbot)">Kimi (chatbot) - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#open-source`, `#industry debate`, `#Jensen Huang`

---

<a id="item-12"></a>
## [华为：网络带宽成 AI 最大瓶颈，Token 调用量涨 6 倍](https://news.google.com/rss/articles/CBMiiAFBVV95cUxNUDI5NFZEQUtVUnB4ZkNvalFJay04cHV5LW54blhzN2YwNkR3Zi0waG9ScjJCMjlYSlNfdjlxVkx4SXdzLUVpLVVJN2JtcjdHc1daZHZ4UEV1clc4aExxRjA4SGxOVkw4RnQ3VlJzRGNXMy0tT2UyaTlVekhtY1RZUTZ6RlVqcHZC?oc=5) ⭐️ 7.0/10

华为指出网络带宽已成为 AI 算力的最大瓶颈，并称 Token 调用量在过去半年内增长了 6 倍。 这一来自主要 AI 基础设施厂商的洞察凸显了一个关键的扩展挑战：随着 AI 推理需求爆发，网络容量必须同步提升，否则将制约性能。 华为的说法基于内部数据，显示 Token 调用量在半年内增长了 6 倍，而截至 2026 年 3 月，中国日均 Token 调用量已超过 140 万亿。

google_news · Sohu · 7月24日 09:31

**背景**: Token 调用量衡量 AI 模型在推理过程中处理的 Token（文本片段）数量。随着聊天机器人和编程助手等 AI 应用的普及，推理需求激增，瓶颈已从算力转向网络带宽。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://finance.biggo.com/news/fTiaY54BYH_ypPqO27EO">Daily Token Call Volume Hits 140 Trillion, China's AI Chip Titans Surpass $368 Billion in Combined Market Cap — BigGo Finance</a></li>
<li><a href="https://eu.36kr.com/en/p/3700980530851712">February Sees Surge in AI Usage: China's AI Call Volume Overtakes US for First Time, Four Large Models Dominate Global Top Five, Domestic Computing Power Demand Soars Exponentially</a></li>

</ul>
</details>

**标签**: `#AI infrastructure`, `#network bandwidth`, `#Huawei`, `#AI scaling`, `#token call volume`

---

<a id="item-13"></a>
## [AMD 发布面向智能体与物理 AI 的全栈算力战略](https://news.google.com/rss/articles/CBMi_gFBVV95cUxOc2w4dWdvZ0JiQ1dtY29RWllsdzhsVV80azcwcERQb1VjLWVCekpyNDBRMTBocTRnNlBEVkZjS3BYZ1ZPd3FOWUlvc0dzWTZMQTJUOW1XejR3RWVMRVFUOGJrQ0MyNUNpN2VEbU1SaE5yQjdGekVUelRnSWFXOF9vcVlJYzloYmZmRVR3ZlNmeTJkdU9CQ0VqODQ0MEJCMmI4MVMwUlpHSkkyQVhBNG9rWTRFLU04N3p0aC1NNmczUzE5empNbEZhVGJFQjhvRlJMY2FpRTBZSjdRNTE3cTJxMUdkR3Zka3hGY0NTeldPbXZnUExIaWpfaXhmRFRCdw?oc=5) ⭐️ 7.0/10

在 Advancing AI 2026 大会上，AMD 宣布了一项面向 AI 智能体和物理 AI 的全栈计算战略，推出了 Ryzen AI Embedded X100 系列芯片和 AMD 机器人合作伙伴网络等新产品。 此举使 AMD 能够在快速增长的 AI 加速器市场（AMD 预计 2030 年市场规模达 1.4 万亿美元）中直接与英伟达竞争，并标志着 AI 向机器人等物理系统集成的转变。 Ryzen AI Embedded X100 系列芯片已进入送样阶段，同时还推出了 Kria AI System-on-Module（120×120 毫米 COM-HPC）。AMD 预计 AI 加速器市场总规模到 2030 年将达到 1.4 万亿美元。

google_news · 新浪网 · 7月24日 00:00

**背景**: 物理 AI 是指能够感知、理解并在现实世界中行动的 AI 系统，使机器人等自主机器成为可能。全栈计算涵盖硬件、软件和平台，以支持从云端到边缘的 AI 工作负载。AMD 的此次发布旨在挑战英伟达在 AI 计算领域的主导地位。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.servethehome.com/amd-advancing-ai-2026-keynote-live-coverage/">AMD Advancing AI 2026 Keynote Live Coverage - ServeTheHome</a></li>
<li><a href="https://www.21ic.com/a/1009238.html">AAI 2026 ：全新 AMD ... - 21ic电子网</a></li>
<li><a href="https://ai.cnmo.com/news/814080.html">AMD AAI 2026 大会有哪些看点：四大自研芯片齐上阵 - CNMO科技</a></li>

</ul>
</details>

**标签**: `#AMD`, `#AI`, `#hardware`, `#computing`, `#strategy`

---