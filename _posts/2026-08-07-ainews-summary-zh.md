---
layout: default
title: "AI行业热点: 2026-08-07 (ZH)"
date: 2026-08-07
lang: zh
briefing: ainews
---

> 从 41 条内容中筛选出 8 条重要资讯。

---

1. [Postgres 扩展 pgrust 通过 SIMD 实现 300 倍分析加速](#item-1) ⭐️ 9.0/10
2. [DeepSeek V4 Flash 0731：更快、更便宜、能力更强](#item-2) ⭐️ 8.0/10
3. [汇编耻辱堂：故意变慢的 x86 指令](#item-3) ⭐️ 8.0/10
4. [科技从业者普遍悲伤引发行业文化讨论](#item-4) ⭐️ 8.0/10
5. [Codex + GPT-5.6 Sol Ultra 在游戏构建测试中胜过 Claude Fable 5](#item-5) ⭐️ 7.0/10
6. [Token 末日：企业争相削减 AI 开支](#item-6) ⭐️ 7.0/10
7. [AMD 收购 Taalas 以增强 AI 推理硬件](#item-7) ⭐️ 7.0/10
8. [TutorMoments：懂得何时帮助或退后的 AI 导师](#item-8) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [Postgres 扩展 pgrust 通过 SIMD 实现 300 倍分析加速](https://malisper.me/how-we-made-postgres-hundreds-of-times-faster-the-query-engine/) ⭐️ 9.0/10

pgrust（一个用 Rust 编写的 Postgres 扩展）的作者发布了一篇技术文章，详细介绍了如何通过批处理、算子融合和 SIMD 使分析查询速度提升高达 300 倍。该项目已通过完整的 PostgreSQL 回归测试套件（46,066/46,066 个查询），并已在 GitHub 上发布。 这展示了 Postgres 分析性能的巨大飞跃，可能使其与专门的分析型数据库竞争。同时，它也证明了 Rust 扩展和现代查询执行技术在 Postgres 生态系统中的可行性，可能影响未来的发展方向。 加速是通过批处理（向量化执行）、算子融合（组合算子以减少开销）和 SIMD（单指令多数据）指令实现的。该项目强调通过形式化验证和差分模糊测试来保证正确性，已有超过 1000 个面向用户的函数被证明与 Postgres 等价。然而，pgrust 尚未准备好用于生产环境，且缺乏稳定的扩展 ABI。

hackernews · poly2it · 8月7日 11:00 · [社区讨论](https://news.ycombinator.com/item?id=49208535)

**背景**: Postgres 是一种广泛使用的关系型数据库，但其传统的基于行的执行模型在处理分析型工作负载时通常比列式或向量化引擎慢。SIMD 允许 CPU 在单条指令中处理多个数据点，而算子融合减少了算子之间传递数据的开销。pgrust 是 Postgres 在 Rust 中的实验性重写，旨在提高性能的同时保持兼容性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/malisper/pgrust">GitHub - malisper/ pgrust : Postgres rewritten in Rust , now faster than...</a></li>
<li><a href="https://pgrust.com/">pgrust — postgres , rewritten in rust</a></li>
<li><a href="https://arxiv.org/pdf/1610.09166">Push vs. Pull-Based Loop Fusion in Query Engines - arXiv.org</a></li>

</ul>
</details>

**社区讨论**: 社区评论显示出高度的兴趣和参与度。作者回应了关于信任的担忧，强调了形式化验证和模糊测试。一些评论者对采用表示怀疑，因为缺乏 Postgres 核心团队的支持，而另一些人则称赞自适应规划方面，希望它能证明这些技术的可行性。还有关于 I/O 调度和线程管理的技术问题。

**标签**: `#Postgres`, `#database`, `#performance`, `#SIMD`, `#query-engine`

---

<a id="item-2"></a>
## [DeepSeek V4 Flash 0731：更快、更便宜、能力更强](https://arcprize.org/results/deepseek-v4-flash-0731) ⭐️ 8.0/10

DeepSeek 于 2025 年 7 月 31 日发布了 DeepSeek V4 Flash 0731，这是其稀疏混合专家模型的一个重新后训练版本。尽管激活参数远少于 DeepSeek V4 Pro（预览版），它在基准测试上表现更优，用户也报告速度和能力有显著提升。 这次更新使高性能 AI 更加普及且成本效益更高，用户报告大量使用每天仅需几美元。它巩固了 DeepSeek 在竞争激烈的 AI 模型市场中的地位，为编码、推理和智能体工作流提供了比专有模型更具吸引力的替代方案。 该模型总参数 284B，激活参数 13B，适用于编码、推理和智能体工作流。在 2x RTX Pro 6000 Blackwell 硬件上，用户观察到预填充速度约 8k tok/s，单流生成约 250 tok/s，某些情况下速度可达 1000 tok/s。

hackernews · tosh · 8月7日 17:56 · [社区讨论](https://news.ycombinator.com/item?id=49214008)

**背景**: DeepSeek V4 Flash 是一个稀疏混合专家（MoE）模型，每个 token 只激活部分参数，从而实现高效。0731 版本是重新后训练的更新，性能优于早期预览版，使其在成本效益更高的同时，与领先的专有模型具有竞争力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V4-Flash-0731">deepseek -ai/ DeepSeek - V 4 - Flash - 0731 · Hugging Face</a></li>
<li><a href="https://openrouter.ai/deepseek/deepseek-v4-flash-0731">DeepSeek V 4 Flash 0731 - API Pricing & Benchmarks | OpenRouter</a></li>
<li><a href="https://aistupidlevel.info/models/deepseek-v4-flash">DeepSeek V 4 Flash Benchmark & Performance ... | AI Stupid Level</a></li>

</ul>
</details>

**社区讨论**: 社区情绪总体积极，用户称赞模型的速度、成本效益以及调试和数据分析能力的提升。然而，一些用户报告了无限循环和无关话题切换等问题，还有一位用户提到可能因认证误用而导致账户被封。

**标签**: `#AI`, `#DeepSeek`, `#Machine Learning`, `#Model Release`, `#Performance`

---

<a id="item-3"></a>
## [汇编耻辱堂：故意变慢的 x86 指令](https://github.com/xoreaxeaxeax/asm-hall-of-shame) ⭐️ 8.0/10

一个名为“asm-hall-of-shame”的 GitHub 仓库被创建，用于展示故意变慢的 x86 指令，在 Hacker News 上引发了技术讨论，获得 206 分和 45 条评论。 该仓库突出了可用于性能分析、安全研究或纯粹娱乐的晦涩硬件特性，社区参与表明对底层编程和逆向工程的浓厚兴趣。 该仓库包含一个慢指令排行榜，其中一个显著例子是向 ACPI IO 端口写入 12 毫秒，可能陷入系统管理模式（SMM）。规则规定，被陷阱/模拟/虚拟化的指令只能计时陷阱，而不能计时处理程序。

hackernews · piotrgrabowski · 8月7日 18:01 · [社区讨论](https://news.ycombinator.com/item?id=49214098)

**背景**: 现代 CPU 在几个周期内执行大多数指令，但某些指令由于微码、硬件特性或与系统管理的交互而可能极其缓慢。该仓库由 xoreaxeaxeax 创建，还链接到相关项目，如“smiiiiiiiiiiiiiiii”，该项目利用慢指令来破坏 SMI 处理。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/xoreaxeaxeax/smiiiiiiiiiiiiiiii">GitHub - xoreaxeaxeax/smiiiiiiiiiiiiiiii: A very very very very very very...</a></li>
<li><a href="https://stackoverflow.com/questions/55871038/infinite-loop-assembly-x86/79989774">Infinite LOOP - Assembly x 86 - Stack Overflow</a></li>
<li><a href="https://gist.github.com/gfoidl/cf95138724aab9933f7aad315decea8c">Processor optimizations · GitHub</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论包括对 Core War（一种编程游戏）的引用，以及关于某些指令是否因陷入 SMM 而违反规则的讨论。用户还提到了作者的其他项目，例如一个只发出“mov”指令的编译器，以及另一个通过扰乱控制流在调试器中绘制符号的编译器。

**标签**: `#assembly`, `#x86`, `#hardware`, `#programming`, `#reverse engineering`

---

<a id="item-4"></a>
## [科技从业者普遍悲伤引发行业文化讨论](https://www.noemamag.com/why-is-everyone-in-tech-so-sad/) ⭐️ 8.0/10

《Noema》杂志的一篇文章探讨了科技从业者中普遍存在的悲伤和对职业失去信心的现象，质疑当整个职业群体对工作感到幻灭时会发生什么。这篇文章引起了广泛共鸣，在 Hacker News 上引发了热烈讨论，获得 315 个点赞和 449 条评论。 这个话题意义重大，因为它凸显了科技行业日益严重的倦怠和幻灭危机，这可能对创新、生产力和心理健康产生深远影响。讨论显示，许多从业者觉得工作失去了意义，可能导致人才流失或科技公司运营方式的转变。 文章和讨论涉及网络的毒性、人工智能对工作保障的影响，以及良好工作激励的削弱。评论者以印刷行业的衰落等历史类比，说明当从业者失去信心时，整个职业可能会消失。

hackernews · RickJWagner · 8月7日 12:42 · [社区讨论](https://news.ycombinator.com/item?id=49209539)

**背景**: 科技行业长期以来与高薪和声望联系在一起，但近年来，关于从业者倦怠、裁员和意义感缺失的报道越来越多。人工智能和自动化的兴起加剧了对工作保障的焦虑，而科技从业者所处的往往有毒的网络文化可能加剧心理健康问题。这篇文章触及了关于工作价值和技术型职业可持续性的更广泛社会讨论。

**社区讨论**: Hacker News 上的评论反映了对文章主题的深刻共鸣，许多人分享了个人幻灭的经历。一些人以印刷业的衰落等历史类比，另一些人则指出有毒的网络和缺乏激励是根本原因。评论中弥漫着集体悲伤和对意义的追寻，有些人甚至表达了完全离开这个行业的愿望。

**标签**: `#tech culture`, `#burnout`, `#career`, `#mental health`, `#software engineering`

---

<a id="item-5"></a>
## [Codex + GPT-5.6 Sol Ultra 在游戏构建测试中胜过 Claude Fable 5](https://simonwillison.net/2026/Aug/7/moonlight-mayhem/#atom-everything) ⭐️ 7.0/10

Simon Willison 使用 Codex Desktop 搭配 GPT-5.6 Sol Ultra 运行了相同的单次游戏构建提示，生成了名为“Moonlight & Mayhem”的游戏，明显优于他之前用 Claude Fable 5 的尝试。新游戏以博物馆抢劫和浣熊队友为特色，但最初有一个眼球过大的 bug，通过简单提示修复。 这一对比凸显了 AI 编码工具的快速进步，表明不同模型和模式在创造性任务上可能产生截然不同的结果。它为开发者在选择 AI 助手时提供了实用见解，可能影响工作流决策和对 AI 生成软件的期望。 Codex 在该项目上花费了 52 分钟，如果不使用订阅，按 API 价格估算成本为 23.28 美元（输入 700.7K tokens，缓存 32.5M tokens，输出 148K tokens）。完整记录可在仓库中获取，Willison 称赞了 Codex 的“复制为 Markdown”功能，他希望 Claude Code 也有此功能。

rss · Simon Willison · 8月7日 19:18

**背景**: 像 Claude Code 和 Codex 这样的 AI 编码助手使用大型语言模型根据自然语言提示生成代码。GPT-5.6 Sol Ultra 是一种积极使用子代理来处理复杂任务的模式，可能提高输出质量。这一实验延续了使用 AI 从简单描述创建完整游戏的趋势，展示了这些工具不断发展的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://developers.openai.com/codex/subagents">Subagents | ChatGPT Learn</a></li>
<li><a href="https://betterstack.com/community/guides/ai/gpt-56-sol-ultra-mode/">GPT-5.6 Sol and Ultra Mode: What You Need to Know</a></li>
<li><a href="https://openai.com/index/gpt-5-6/">GPT‑5.6: Frontier intelligence that scales with your ambition</a></li>

</ul>
</details>

**标签**: `#AI coding`, `#Codex`, `#GPT-5.6`, `#game development`, `#comparison`

---

<a id="item-6"></a>
## [Token 末日：企业争相削减 AI 开支](https://simonwillison.net/2026/Aug/7/pdfs-are-terrible/#atom-everything) ⭐️ 7.0/10

6 月 24 日 404 Media 的报道揭示，随着 token 消耗激增，企业正争相削减 AI 开支。埃森哲内部数据显示，非工程师是 token 消耗的主要驱动力，尤其是通过将 PDF 转换为 markdown 文件。 这凸显了企业在采用 AI 时面临的日益增长的财务压力，token 成本已成为重要的运营开支。它强调了成本优化策略和更好的文档格式以减少 AI 支出的必要性。 埃森哲的 agentic AI 战略负责人 Justice Kwak 指出，非工程师推动了 token 消耗，而将 PDF 转换为 markdown 是主要的 token 消耗来源。文章认为 PDF 是一种糟糕的信息传播媒介，导致了效率低下。

rss · Simon Willison · 8月7日 16:18

**背景**: AI 中的 token 消耗指的是模型处理的文本单元数量，直接决定了 API 成本。Agentic AI 工作流的 token 消耗可能是简单查询的 5 到 30 倍，而将文件转换为 markdown 可以在不损失内容质量的情况下减少 65-90%的 token 使用。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://smartdev.com/glossary-token-consumption/">What Is Token Consumption in AI ? Definition, Costs & Management</a></li>
<li><a href="https://www.mindstudio.ai/blog/convert-files-markdown-reduce-ai-tokens">How to Convert Files to Markdown to Reduce AI Token Usage by Up to 90% | MindStudio</a></li>

</ul>
</details>

**标签**: `#AI costs`, `#token consumption`, `#enterprise AI`, `#cost optimization`

---

<a id="item-7"></a>
## [AMD 收购 Taalas 以增强 AI 推理硬件](https://www.latent.space/p/ainews-amd-buys-taalas) ⭐️ 7.0/10

AMD 已收购专注于模型专用芯片的 AI 芯片初创公司 Taalas，以加强其在 AI 推理市场的地位。该交易于 2026 年 8 月宣布，AMD 计划将 Taalas 的技术与其 Instinct GPU 集成。 此次收购标志着 AI 推理硬件领域竞争加剧，各公司寻求专用解决方案以克服性能和效率瓶颈。这可能挑战 NVIDIA 的主导地位，并加速行业向模型专用 ASIC 的转变。 Taalas 采用“模型即硬件”策略，可在短短两个月内将 AI 模型转化为定制芯片。AMD 将把 Taalas 的技术与其 Instinct GPU 集成，提供系统级解决方案，此前已收购 MK1、MEXT 和 FastFlowLM 等公司。

rss · Latent Space · 8月7日 05:13

**背景**: AI 推理硬件是一个快速增长的市场，传统 GPU（如 NVIDIA 的）可编程但未针对特定模型优化。Taalas 的方法是一种极端形式的专用集成电路（ASIC），将模型本身嵌入硬件中，可能在性能和效率上实现突破。AMD 的收购是其更广泛战略的一部分，旨在 AI 芯片市场竞争。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://ir.amd.com/news-events/press-releases/detail/1296/amd-acquires-taalas-to-advance-compute-solutions-for-rapidly-growing-ai-inference-market">AMD Acquires Taalas to Advance Compute Solutions for Rapidly...</a></li>
<li><a href="https://aiwiki.ai/wiki/taalas">Taalas | AI Wiki</a></li>
<li><a href="https://taalas.com/the-path-to-ubiquitous-ai/">The path to ubiquitous AI | Taalas</a></li>

</ul>
</details>

**标签**: `#AMD`, `#Taalas`, `#AI hardware`, `#acquisition`, `#inference`

---

<a id="item-8"></a>
## [TutorMoments：懂得何时帮助或退后的 AI 导师](https://huggingface.co/blog/allenai/tutormoments) ⭐️ 7.0/10

TutorMoments 由艾伦人工智能研究所在 Hugging Face 博客上推出，探索了一种设计 AI 导师的新方法，使其能够决定何时提供帮助、何时让学习者自行挣扎。该项目旨在通过优化干预时机来改善学习效果。 这项工作解决了教育 AI 中的一个关键挑战：导师干预的时机。如果成功，它可能带来更有效的 AI 辅导系统，更好地支持学生学习，减少对即时答案的依赖，从而影响更广泛的 EdTech 和教育 AI 生态系统。 该博客可能包含模型架构、训练数据和评估方法的技术细节，但摘要中未提供具体数字。该方法可能涉及强化学习或监督学习来建模何时干预，可能利用学生的参与度和表现信号。

rss · Hugging Face Blog · 8月7日 17:53

**背景**: AI 导师是为学习者提供个性化指导的智能系统，通常能适应个人需求。一个关键挑战是决定何时提供帮助：过多的帮助会阻碍独立解决问题，而过少则可能导致挫败感。这一概念与教育中的“脚手架”相关，即随着学习者能力的提升逐步撤除支持。自适应学习系统也旨在根据学生当前的知识水平定制教学。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://code.org/en-US/tools/ai-tutor">AI Tutor | CodeAI</a></li>
<li><a href="https://bostreet.com/innovation-in-education/adaptive-learning-systems/">Adaptive Learning Systems - Bo Street</a></li>
<li><a href="https://www.uopeople.edu/blog/what-is-scaffolding-in-education/">Essential Tips On What Is Scaffolding In Education</a></li>

</ul>
</details>

**标签**: `#AI in Education`, `#Tutoring Systems`, `#Human-AI Interaction`, `#Machine Learning`, `#EdTech`

---