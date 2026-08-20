---
layout: default
title: "AI行业热点: 2026-08-20 (ZH)"
date: 2026-08-20
lang: zh
briefing: ainews
---

> 从 87 条内容中筛选出 11 条重要资讯。

---

1. [恶意 Rust crate arrayref 在构建时运行载荷](#item-1) ⭐️ 9.0/10
2. [GitHub 8 月 17 日宕机：VS Code 重试漏洞放大流量](#item-2) ⭐️ 8.0/10
3. [AliExpress 静默 WebAudio 指纹识别干扰蓝牙多点连接](#item-3) ⭐️ 8.0/10
4. [关于生物学与教育的文章引发热议](#item-4) ⭐️ 8.0/10
5. [智谱 CEO 唐杰谈 GLM 5.3 与新的后训练缩放定律](#item-5) ⭐️ 8.0/10
6. [Liquid AI 的 LFM2.5-DSpark 将推理速度提升 3.2 倍](#item-6) ⭐️ 8.0/10
7. [Simon Willison 测试 smolvm 作为不可信代码的沙箱](#item-7) ⭐️ 7.0/10
8. [LLM 与沙箱技术开启可扩展 Web 软件的新时代](#item-8) ⭐️ 7.0/10
9. [阿里 AI 答卷亮眼：云增速升至 45%，模型矩阵跻身全球一流](#item-9) ⭐️ 7.0/10
10. [AI 公司从 Claude 转向 DeepSeek，年省数百万美元](#item-10) ⭐️ 7.0/10
11. [阿里 CEO：平头哥二代芯片预计下半年流片](#item-11) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [恶意 Rust crate arrayref 在构建时运行载荷](https://safedep.io/arrayref-proc-macro1-rust-build-time-malware/) ⭐️ 9.0/10

2026 年 8 月 20 日，流行的 Rust crate arrayref 的 0.3.10 版本在 crates.io 上发布，该版本添加了一个名为 proc-macro1 的仿冒依赖，其构建脚本在 cargo build 期间下载并执行远程二进制文件。Rust 安全响应团队确认了此次攻击，并删除了 arrayref、internment 和 append-only-vec 的恶意版本。 这一事件凸显了 Rust 生态系统中供应链攻击日益增长的威胁，一个拥有数百万下载量的广泛使用的 crate 可能在构建过程中被攻破并传递恶意软件。它强调了采取更好安全措施的必要性，例如对构建脚本进行沙箱隔离，以及更健全的 crates.io 事件响应机制。 proc-macro1 中的恶意构建脚本会下载并运行远程二进制文件，使其成为一个构建时投放器。受影响的 crate 包括 arrayref 0.3.10、internment 0.8.7 和 append-only-vec 0.1.9，每个都添加了一个仿冒依赖（proc-macro1 或 proc-macro-en）。恶意版本已从 crates.io 中删除，但尚未为 arrayref 发布安全公告。

hackernews · abhisek · 8月20日 13:23 · [社区讨论](https://news.ycombinator.com/item?id=49374269)

**背景**: Rust 是一种系统编程语言，使用 crates.io 作为其包注册表。Cargo 是 Rust 的构建工具，会自动编译构建脚本（build.rs），这些脚本可以执行任意代码，这是供应链攻击的一个已知途径。仿冒（Typosquatting）是指创建与流行包名称相似的包，以诱骗开发者安装恶意代码。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.rust-lang.org/2026/08/20/supply-chain-attack-on-arrayref/">Supply chain attack on arrayref | Rust Blog</a></li>
<li><a href="https://www.stepsecurity.io/blog/arrayref-rust-crate-supply-chain-attack">Rust Supply-Chain Attack: arrayref, internment, and append-only-vec Poisoned by the proc-macro1 Build-Time Dropper - StepSecurity</a></li>
<li><a href="https://thehackernews.com/2026/08/rust-supply-chain-attack-puts-build.html">Rust Supply Chain Attack Puts Build-Time Malware in Crates ...</a></li>

</ul>
</details>

**社区讨论**: 社区评论对事件响应表示不满，指出恶意版本从 crates.io 消失时没有明确的撤回指示，也没有发布安全公告。一些人呼吁在 Cargo 中对构建脚本进行沙箱隔离，而另一些人则主张采用更“内置电池”的方法来减少依赖数量。还有人担心 Rust 项目中传递依赖数量过多，类似于 JavaScript 生态系统。

**标签**: `#security`, `#rust`, `#supply-chain`, `#malware`, `#crates.io`

---

<a id="item-2"></a>
## [GitHub 8 月 17 日宕机：VS Code 重试漏洞放大流量](https://github.blog/news-insights/company-news/the-august-17-outage-and-the-work-ahead/) ⭐️ 8.0/10

GitHub 发布了 8 月 17 日宕机的复盘报告，揭示 VS Code 中一个潜在的重试漏洞将流量放大了约 10 倍，并延迟了 Copilot Token Service 的恢复。此次事件还突显了月度提交量的显著增长，从 4 月的 14 亿增加到 29 亿。 此次宕机凸显了分布式系统在重试风暴下的脆弱性，尤其是像 GitHub Copilot 这样广泛使用的开发者工具。事件对数百万开发者的影响以及对重试策略的讨论，凸显了在客户端-服务器交互中需要更健壮的错误处理。 宕机最初由 GitHub 美国中部数据中心负载均衡器的网络饱和引发，但被 VS Code 中的一个潜在重试漏洞延长。该漏洞导致客户端重试循环，将流量放大约 10 倍，延迟了 Copilot Token Service 的恢复。

hackernews · 0xedb · 8月20日 19:22 · [社区讨论](https://news.ycombinator.com/item?id=49378957)

**背景**: 重试风暴是指客户端自动重试失败的请求，可能使服务器不堪重负。在此案例中，VS Code 的重试漏洞将小延迟变成了级联故障。GitHub 的复盘还指出月度提交量显著增加，反映了行业的“生产力焦虑”以及对 AI 辅助编码工具的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theregister.com/saas/2026/08/19/github-blames-8-hour-outage-on-autoscaling-fail-and-vs-code-retry-storm/5289547">GitHub blames 8-hour outage on autoscaling fail and VS Code retry ...</a></li>
<li><a href="https://juniortoexpert.com/en/what-is-retry-storm/">What is Retry Storm? Causes, Consequences, and Examples</a></li>
<li><a href="https://www.computing.co.uk/news/2026/security/github-outage-exposes-flaws-in-autoscaling-and-retry-systems">GitHub outage exposes flaws in autoscaling and retry systems</a></li>

</ul>
</details>

**社区讨论**: 社区评论对隐藏错误给用户的趋势表示担忧，一位用户指出重试可能会掩盖真正的故障。另一位用户强调提交量的急剧增长是行业“生产力焦虑”的证据，而其他人则就重试机制的利弊以及微软推动 AI 采用的动机展开了辩论。

**标签**: `#outage`, `#postmortem`, `#GitHub`, `#retry`, `#reliability`

---

<a id="item-3"></a>
## [AliExpress 静默 WebAudio 指纹识别干扰蓝牙多点连接](https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html) ⭐️ 8.0/10

安全研究人员发现，AliExpress 首页运行静默的 WebAudio 指纹识别脚本，使蓝牙音频路径保持活动状态，阻止多点连接耳机切换到其他设备。该技术使用混淆的阿里巴巴安全脚本生成并分析波形，且不产生可听输出。 这突显了一种新颖的隐私侵犯技术，它无形中运行并可能对硬件产生实际副作用。它强调了浏览器指纹识别日益复杂化及其干扰用户体验的潜力，引发了对用户同意和透明度的担忧。 这些脚本创建两个 WebAudio 图，通过零增益节点连接到系统音频目标，在保持音频路径活动的同时避免可听声音。这似乎使 PC 的蓝牙音频路径保持活动，阻止多点连接耳机切换回手机。该技术即使在启用“不跟踪”的情况下也能工作，且不留任何用户可检查的痕迹。

hackernews · emctech · 8月20日 10:08 · [社区讨论](https://news.ycombinator.com/item?id=49372583)

**背景**: WebAudio 指纹识别是一种浏览器指纹识别技术，利用 Web Audio API 根据音频处理特性识别设备。与 cookie 不同，它不可见且难以阻止。蓝牙多点连接允许耳机同时保持与多个设备的连接，但活动音频流会阻止切换。AliExpress 案例表明指纹识别脚本可能无意中干扰此功能。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.laserphile.com/2026/08/aliexpress-webpage-keeping-multipoint.html">laserphile: AliExpress webpage keeping multipoint Bluetooth headphones active with WebAudio fingerprinting</a></li>
<li><a href="https://news.ycombinator.com/item?id=49372583">AliExpress runs silent WebAudio fingerprinting that breaks Bluetooth multipoint | Hacker News</a></li>
<li><a href="https://bscan.info/blog/audioFingerprinting">Audio Fingerprinting: The Sound of Tracking | bscan.info</a></li>

</ul>
</details>

**社区讨论**: 评论者分享了使用 AliExpress 和阿里巴巴应用时遇到的蓝牙问题个人经历，指出卸载应用后问题得到解决。一些人讨论了 Firefox 中的缓解措施，以及激进的指纹识别破坏硬件功能的讽刺性。总体情绪批评这种侵犯隐私的做法及其意外副作用。

**标签**: `#privacy`, `#web security`, `#fingerprinting`, `#bluetooth`, `#web audio`

---

<a id="item-4"></a>
## [关于生物学与教育的文章引发热议](https://jsomers.net/i-should-have-loved-biology/) ⭐️ 8.0/10

一篇题为《我本应热爱生物学》（2020 年）的反思性文章在 Hacker News 上重新引起广泛关注，获得 8.0/10 的评分，163 个点赞和 63 条评论。文章批评传统教育扼杀了对生物学的好奇心，并将其与学科本身的美感进行对比。 这篇文章引起了技术受众的共鸣，反映了对死记硬背式学习的共同不满，以及对以探索为导向的教育方式的渴望。它引发了关于教学法、对科学研究的浪漫主义与现实主义看法，以及从事生命科学职业所面临挑战的更广泛讨论。 这篇文章是一篇个人反思性文章，而非技术性文章，其影响力在于其叙事性和引发的讨论。社区评论揭示了浪漫化生物学与强调研究现实（如成为更大机器中的“齿轮”）之间的分歧。

hackernews · tyre · 8月20日 17:50 · [社区讨论](https://news.ycombinator.com/item?id=49377853)

**背景**: 这篇文章触及了对 STEM 教育的常见批评，即学科常常被当作记忆而非探索来教授。它引用了 Seymour Papert 和 Jean Piaget 的教学哲学，该哲学认为知识是通过与环境的互动构建的。这一背景有助于解释为什么这篇文章能引起那些觉得好奇心在传统课堂中被压抑的人的共鸣。

**社区讨论**: 社区评论表达了赞同和反驳的混合观点。一些人称赞文章的浪漫主义视角，但提醒说实际研究并不那么光鲜，另一些人则分享个人经历，说明尽管教学不佳，他们仍然热爱生物学。一个反复出现的主题是对教学法的批评，引用了 Piaget 和 Papert，并指出这篇文章是“HN 上的常青最爱”。

**标签**: `#biology`, `#education`, `#pedagogy`, `#science`, `#personal reflection`

---

<a id="item-5"></a>
## [智谱 CEO 唐杰谈 GLM 5.3 与新的后训练缩放定律](https://www.latent.space/p/ainews-death-of-params-zai-ceo-jie) ⭐️ 8.0/10

智谱 CEO 唐杰讨论了 GLM 5.3，该模型复用了 GLM-5.2 的基础模型，所有性能提升均通过后训练实现，标志着从以参数为中心的缩放转向后训练缩放。在 Terminal-Bench 3.0 上，得分从 4.6 大幅跃升至 28.3。 这标志着 AI 缩放定律可能发生范式转变，强调数据质量、推理计算和后训练，而非单纯的参数数量。这可能影响行业资源分配和模型进展评估方式，尤其是在编码和智能体任务方面。 GLM-5.3 复用了 GLM-5.2 的基础模型，智谱表示所有提升均来自后训练。后训练技术栈包括用于高效长上下文处理的 IndexShare、用于长周期任务强化学习的 SAO，以及用于大规模异步训练的 slime，并承诺稍后发布权重。

rss · Latent Space · 8月20日 05:17

**背景**: 传统的神经缩放定律认为，性能会随着模型参数、数据集规模和计算量的增加而可预测地提升。然而，最近的研究和发展正在探索训练之外的缩放，例如测试时计算和后训练强化学习。GLM-5.3 体现了这一趋势，它仅专注于后训练改进，而不改变基础模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.digitalapplied.com/blog/glm-5-3-launch-post-training-scaling-coding-agents">GLM-5.3: Post-Training Alone Rebuilt the Coding Ladder</a></li>
<li><a href="https://z.ai/blog/glm-5.3">GLM-5.3: Frontier Coding with Emergent Cyber Capabilities</a></li>
<li><a href="https://en.wikipedia.org/wiki/Neural_scaling_law">Neural scaling law - Wikipedia</a></li>

</ul>
</details>

**标签**: `#AI`, `#scaling laws`, `#GLM`, `#post-training`, `#LLM`

---

<a id="item-6"></a>
## [Liquid AI 的 LFM2.5-DSpark 将推理速度提升 3.2 倍](https://huggingface.co/blog/LiquidAI/lfm25-dspark) ⭐️ 8.0/10

Liquid AI 为其 LFM2.5 系列中的三个模型发布了投机解码草稿检查点，在单个 H100 GPU 上实现了高达 3.18 倍的吞吐量提升，在 Apple 芯片设备上实现了高达 2.87 倍的提升。新的 DSpark 模型已在 Hugging Face 上提供。 这一进展显著降低了推理延迟和成本，使大型语言模型在实时和端侧应用中更加实用。它凸显了将模型架构与投机方法协同设计以优化实际推理的重要性日益增加。 DSpark 草稿模型适用于 LFM2.5-1.2B-Instruct、LFM2.5-2.6B 和 LFM2.5-8B-A1B，增加了一条投机解码路径，以最小的内存增加换取大幅解码加速，且不改变输出质量。报告显示，GPU 上性能提升高达 3.18 倍，端侧提升高达 2.87 倍。

rss · Hugging Face Blog · 8月20日 16:52

**背景**: 投机解码是一种推理优化技术，使用较小的草稿模型生成候选 token，然后由较大的目标模型进行验证，从而减少顺序解码步骤的数量。Liquid AI 的 LFM2.5 模型基于液体神经网络原理，允许在推理过程中动态调整。此次发布展示了将模型架构与投机方法协同设计以提高推理效率的有效性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/LiquidAI/lfm25-dspark">Up to 3.2x Faster Inference with LFM2.5-DSpark - Hugging Face</a></li>
<li><a href="https://www.liquid.ai/blog/lfm2.5-dspark">LFM2.5-DSpark: Up to 3.2x Faster Inference from H100 to ...</a></li>
<li><a href="https://www.unite.ai/liquid-ai-ships-lfm2-5-dspark-for-up-to-3-2x-faster-inference/">Liquid AI Ships LFM2.5-DSpark for Up to 3.2X Faster Inference</a></li>

</ul>
</details>

**标签**: `#inference`, `#performance`, `#LLM`, `#model optimization`, `#Hugging Face`

---

<a id="item-7"></a>
## [Simon Willison 测试 smolvm 作为不可信代码的沙箱](https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/) ⭐️ 7.0/10

Simon Willison 发布了一篇研究笔记，探索使用 smolvm 作为沙箱来运行不可信的 Python 和 JavaScript 代码，并设置资源限制。他在 Claude Code for web 环境中遇到了限制，转而使用带有 /dev/kvm 的 GitHub Actions 运行器来执行测试。 这项探索与安全和沙箱相关，因为 smolvm 提供硬件隔离的虚拟机来运行不可信代码，比共享内核的容器更安全。它为使用微虚拟机进行数据转换提供了实用见解，并展示了应对环境限制的创造性解决方案。 测试使用了 smolvm 1.8.3，重点包括 CPU/RAM 限制、无网络执行以及仅对指定文件的文件系统访问。Claude Code 容器缺少 /dev/kvm 和 vmx/svm CPU 标志，无法进行嵌套虚拟化，因此测试在暴露 /dev/kvm 的 GitHub Actions ubuntu 运行器上执行。

rss · Simon Willison · 8月19日 23:16

**背景**: smolvm 是一个便携、轻量、自包含的虚拟机，启动时间不到 200 毫秒，专为在硬件隔离的虚拟机中沙箱运行不可信代码而设计。它是 Celesto AI 的 smol-machines 项目的一部分，提供用于代码执行、浏览器操作和 AI 代理的微虚拟机环境。传统容器共享宿主内核，对不可信代码存在风险，而虚拟机提供了更强的隔离性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/smol-machines/smolvm">GitHub - smol-machines/smolvm: Portable, lightweight, self-contained virtual machine. · GitHub</a></li>
<li><a href="https://simonwillison.net/2026/Aug/19/smolmachines-untrusted-sandbox/">Research: smolmachines / smolvm as a sandbox for untrusted Python & JavaScript</a></li>
<li><a href="https://note.com/snake_dragon/n/n1a2666024bf3?hl=en">A Complete Guide to smolVM: A Technical Deep Dive into the Next-Generation Micro-VM That Boots in Under 200ms｜スネドラ</a></li>

</ul>
</details>

**标签**: `#sandboxing`, `#security`, `#Python`, `#JavaScript`, `#research`

---

<a id="item-8"></a>
## [LLM 与沙箱技术开启可扩展 Web 软件的新时代](https://simonwillison.net/2026/Aug/19/jeremy-morrell/) ⭐️ 7.0/10

Jeremy Morrell 提出，LLM 和现代沙箱技术为可扩展的 Web 软件创造了新的机会，允许用户使用 AI 生成的代码安全地扩展应用。他建议构建一个坚实的核心，并让 LLM 填补缺失的部分，从而赋予用户“超能力”。 这一假设可能重塑 Web 应用的设计方式，催生一类兼顾安全性与灵活性的用户可扩展软件。它可能促使开发者采用 LLM 驱动的扩展机制，从而降低开发成本并增强用户能力。 该引言出自 Morrell 的博客文章《Extensible Software in the age of LLMs》，由 Simon Willison 分享。这一想法依赖于现代沙箱原语提供安全边界，同时 LLM 降低了编写扩展的成本。引言中未详细说明具体的技术实现。

rss · Simon Willison · 8月19日 22:56

**背景**: 可扩展软件允许用户添加功能或修改行为，传统上通过插件或 API 实现。LLM 可以从自然语言生成代码，降低了创建扩展的门槛。沙箱技术隔离代码执行以防止恶意行为，对于安全运行 AI 生成的代码至关重要。现代 Web 沙箱技术，如 iframe 沙箱和 WebAssembly，提供了强大的隔离能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/alexgriss/the-architecture-of-browser-sandboxes-a-deep-dive-into-javascript-code-isolation-1dnj">The Architecture of Browser Sandboxes: A Deep Dive into ...</a></li>
<li><a href="https://testsigma.com/blog/browser-sandbox/">Browser Sandbox Guide: Architecture, Types & Security List of coding agent sandboxes 2026-05 · GitHub Principles and Applications of Browser Sandbox Technology Sandbox Environments for Testing and Website Development Browser Sandboxing for Coding Agents: 2026 Security Guide</a></li>
<li><a href="https://arxiv.org/abs/2502.01853">[2502.01853] Security and Quality in LLM-Generated Code: A Multi-Language, Multi-Model Analysis</a></li>

</ul>
</details>

**标签**: `#LLMs`, `#extensible software`, `#sandboxing`, `#AI`, `#web development`

---

<a id="item-9"></a>
## [阿里 AI 答卷亮眼：云增速升至 45%，模型矩阵跻身全球一流](https://news.google.com/rss/articles/CBMieEFVX3lxTE1rR20xZjF6M1lhd0tZQm9zT0xHUnE2Z3BzOTRPYmpGWExfS0k3R3VaTmQ3ZEk2T2p2TXdrdWluaDdHVVE0S193cVJDa3VHek4tb1lyUk54TnRfTnhWSVVTOXNtc1pIdzlNREpVR1NPYmVHQzFkajIyLQ?oc=5) ⭐️ 7.0/10

阿里巴巴集团公布，截至 2026 年 6 月的季度，其云外部商业化收入增速提升至 45%，创 22 个季度新高。公司还宣布，其五大 AI 模型类别——语言、图像、语音、视频和音乐——均完成重要版本迭代，全部跻身全球一流水平。 这一里程碑凸显了阿里巴巴在全球 AI 和云计算市场的强劲地位，表明其 AI 商业化正从技术叙事转向财务兑现。加速增长和一流模型地位可能加剧与微软 Azure 和亚马逊 AWS 等全球云巨头的竞争，并预示着中国 AI 驱动云增长的大趋势。 本季度，阿里云 AI 相关产品收入达 123.76 亿元，AI 云及算力服务分部收入为 484.37 亿元，经调整 EBITA 为 56.28 亿元，同比暴增 133%，利润率升至 12%。公司以 Qwen 为核心的开源模型生态已成为全球广泛的 AI 模型生态。

google_news · 新浪财经 · 8月20日 14:40

**背景**: 阿里云是阿里巴巴集团的云计算部门，提供全栈 AI 能力，包括通义千问（Qwen）大语言模型、人工智能平台 PAI 以及各类 AI 服务。公司一直在大力投资 AI 和云基础设施，其 Qwen 模型在开源社区中被广泛使用。最近的财报反映了这些投资带来的财务回报，AI 正推动云业务的新一轮增长。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://stock.10jqka.com.cn/20260820/c679147405.shtml">阿里AI答卷亮眼:云增速升至45%,模型矩阵全部跻身全球一流</a></li>
<li><a href="https://finance.sina.com.cn/jjxw/2026-08-20/doc-ininysmk1870751.shtml">阿里AI答卷亮眼：云增速升至45%，模型矩阵全部跻身全球一流</a></li>
<li><a href="https://www.jiemian.com/article/14956690.html">阿里云增速45%创22个季度新高|界面新闻 · 快讯</a></li>
<li><a href="https://k.sina.cn/article_7879922977_1d5ae152106801ijie.html">阿里云二季度营收484.37亿元增45% 增速为何时隔6年反超微软和亚马逊？...</a></li>
<li><a href="https://www.sfccn.com/2026/8-20/zNMDE1MThfMjIxNTIzNg.html">阿里财报：云收入增长45%创新高，全栈AI商业化提速</a></li>

</ul>
</details>

**标签**: `#Alibaba`, `#AI`, `#cloud computing`, `#business news`

---

<a id="item-10"></a>
## [AI 公司从 Claude 转向 DeepSeek，年省数百万美元](https://news.google.com/rss/articles/CBMiZ0FVX3lxTE9aLWNGYkd6a0VfNm9zdGU0YnRoQmVCOU9BWHNzZ0hZSkRJN0RjU1hONi1Ha0dlQV91OHZlT1B2RzNFWHplR1FuajhXM2NQcnloSWNHa0ViVTV2RmlXRk13RTRjRVJwMVU?oc=5) ⭐️ 7.0/10

一家 AI 公司的 CEO 详细介绍了从 Anthropic 的 Claude 迁移到 DeepSeek 的 9 个月过程，报告称迁移工作量增加了 100 倍，但每年节省了数百万美元。 这一案例研究凸显了领先 AI 模型之间的显著成本差异，以及切换供应商所涉及的实际权衡。它为考虑迁移模型以优化成本而不牺牲性能的工程团队提供了宝贵的见解。 迁移耗时 9 个月，由于提示词更改、评估流程和性能调优，工作量增加了 100 倍。该公司每年节省了数百万美元，表明在其用例中，DeepSeek 的定价远低于 Claude。

google_news · blog.csdn.net · 8月20日 10:13

**背景**: Anthropic 的 Claude 和 DeepSeek 都是用于 AI 应用的大型语言模型。Claude 提供分层计划和 API 定价，而 DeepSeek 提供开源模型，如 DeepSeek-V3 和 DeepSeek-R1，这些模型以成本效益高而闻名。在 AI 供应商之间迁移涉及调整提示词、评估输出和确保性能对等，这可能非常耗费人力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://claude.com/pricing">Plans & Pricing | Claude by Anthropic</a></li>
<li><a href="https://huggingface.co/deepseek-ai/DeepSeek-V3">deepseek-ai/DeepSeek-V3 · Hugging Face</a></li>
<li><a href="https://www.lindy.ai/blog/migrating-from-claude-to-deepseek">Migrating from Claude to DeepSeek - lindy.ai</a></li>

</ul>
</details>

**标签**: `#AI`, `#cost optimization`, `#model migration`, `#DeepSeek`, `#Claude`

---

<a id="item-11"></a>
## [阿里 CEO：平头哥二代芯片预计下半年流片](https://news.google.com/rss/articles/CBMiUEFVX3lxTFBzQ1lhYW9YaVZnb3RsaUw1bjExNWpjbEJOSEt4RTRPRUdHay1SeUdRMTlZYko1a2ZwaDZqQW5kN0YySDdDSGFBY292b19Pc2tU?oc=5) ⭐️ 7.0/10

阿里巴巴 CEO 吴泳铭在分析师电话会上宣布，平头哥第二代芯片将于今年下半年开始流片和产出，该芯片具备强大的算力和互联带宽。 这标志着中国半导体自给自足的重要一步，阿里巴巴旨在用自研芯片替代大规模模型训练。同时，在全球供应链限制下，这也表明国内芯片研发取得进展。 新芯片基于下一代平头哥架构，基于真武 M890 的超节点实例已在阿里云上线并规模化销售。平头哥已建立覆盖 GPU、CPU、网络芯片的全栈自研芯片组合，截至 8 月初已服务超过 650 家客户。

google_news · 虎嗅 · 8月20日 20:25

**背景**: 流片是芯片设计的最后一步，将设计发送给代工厂进行制造。阿里巴巴的平头哥半导体部门专注于为云计算和 AI 工作负载开发芯片，旨在减少对外国供应商的依赖。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.msn.cn/zh-cn/技术/硬件和设备/阿里-ceo-吴泳铭-平头哥二代芯片预计今年下半年流片-产出/ar-AA2ayuCY">阿里 CEO 吴泳铭：平头哥二代芯片预计今年下半年流片、产出</a></li>
<li><a href="https://tech.ifeng.com/c/8vkiGOeK8Kk">阿里CEO吴泳铭：平头哥二代芯片预计今年下半年流片、产出</a></li>
<li><a href="https://guba.eastmoney.com/news,usbaba,1762179293.html">阿里CEO吴泳铭：平头哥二代芯片预计今年下半年开始流片_阿里巴巴 (usb...</a></li>

</ul>
</details>

**标签**: `#semiconductor`, `#chip`, `#Alibaba`, `#Pingtouge`, `#tape-out`

---