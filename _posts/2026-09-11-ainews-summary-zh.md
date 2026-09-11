---
layout: default
title: "AI行业热点: 2026-09-11 (ZH)"
date: 2026-09-11
lang: zh
briefing: ainews
---

> 从 80 条内容中筛选出 7 条重要资讯。

---

1. [OpenAI 发布 Navier-Stokes 问题的 Lean 4 形式化证明](#item-1) ⭐️ 9.0/10
2. [微软将 Rust 提升为一级语言](#item-2) ⭐️ 9.0/10
3. [DeepSeek 发布 V4.1 Flash，缓存定价极低](#item-3) ⭐️ 9.0/10
4. [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](#item-4) ⭐️ 9.0/10
5. [DeepSeek 发布 MIT 协议 Harness 应用并开放 V4-Pro-0813 权重](#item-5) ⭐️ 9.0/10
6. [trynix.dev 通过 qemu-wasm 在浏览器中运行任意 Nix 包](#item-6) ⭐️ 8.0/10
7. [Sand.ai 开源全球首个千亿参数 MoE 视频生成模型](#item-7) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [OpenAI 发布 Navier-Stokes 问题的 Lean 4 形式化证明](https://www.johndcook.com/blog/2026/09/09/formal-method-revolution/) ⭐️ 9.0/10

2026 年 9 月 8 日，OpenAI 声称证明了 Navier-Stokes 方程在三维欧几里得空间中解会爆破，并附带了在 Lean 4 证明助手中完成的形式化验证。该反例由一个约 10,000 个 AI 智能体组成的集群运行内部前沿模型生成，目前尚未经过外部数学家或克莱数学研究所的验证。 这标志着自动定理证明和形式化方法领域的重大里程碑，因为 AI 系统攻克了七大千禧年大奖难题之一。如果得到验证，它可能重塑数学研究的方式，并引发关于 AI 在解决开放问题中角色的紧迫问题。 该方法建立在 Diego Córdoba 和 Luis Martínez-Zoroa 于 2023 年开发的用于在相关流体方程中寻找爆破现象的技术之上，OpenAI 表示不会申领 100 万美元的克莱千禧年大奖。与此同时，与受雇于 Anthropic 的 Levent Alpöge 和 Tristan Buckmaster 之间出现了优先权争议，后者曾推导出与欧拉方程密切相关的成果。

hackernews · ibobev · 9月10日 21:22 · [社区讨论](https://news.ycombinator.com/item?id=49650326)

**背景**: Navier-Stokes 存在性与光滑性问题探讨描述流体运动的方程在三维空间中是否总有光滑解，它是克莱数学研究所七大千禧年大奖难题之一。Lean 4 是一种基于归纳构造演算的证明助手和函数式编程语言，用于机械验证数学证明。自动定理证明是自动推理的一个子领域，利用计算机程序生成形式化证明。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Navier-Stokes_problem">Navier-Stokes problem</a></li>
<li><a href="https://en.wikipedia.org/wiki/Lean_(proof_assistant)">Lean (proof assistant) - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Automated_theorem_proving">Automated theorem proving</a></li>

</ul>
</details>

**社区讨论**: 评论者对通用计算机程序能解决如此重大的问题表示震惊，同时讨论了 Lean 的验证速度（例如费马大定理验证耗时 15 小时、占用 230GB 内存）以及 AI 智能体与人类劳动之间的真实成本对比。一些人担心如果证明需要超人智能，人类可能无法独立验证 AI 生成的证明；另一些人则指出，自“每页四十小时”等旧估计以来，Lean 的证明自动化已有显著改进。

**标签**: `#AI`, `#formal-verification`, `#Lean4`, `#Navier-Stokes`, `#theorem-proving`

---

<a id="item-2"></a>
## [微软将 Rust 提升为一级语言](https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/) ⭐️ 9.0/10

微软已正式将 Rust 列为一级编程语言，为内部团队提供从本地开发到生产环境的顺畅路径，包括安全的工具链构建、高效的开发者工具、质量工作流、深度平台集成和合规性。值得注意的是，这包括用 MSVC 后端替换 LLVM 来编译 Rust。 这标志着微软在其产品和工具链中对内存安全系统编程的重大战略承诺，并表明 Rust 现已成为 C++ 和 C# 等成熟语言的严肃竞争对手。这也意味着所有在 C 和 C++ 工具链中扮演角色的主要操作系统供应商，如今都已为全新开发多元化了自己的系统编程语言选择。 微软设定了到 2030 年通过自动化工具将 10 亿行代码转换为 Rust 的目标，目标是“1 名工程师、1 个月、100 万行代码”。DARPA 也在资助使用六支不同团队、不同方法来自动化 C 到 Rust 转换的工作。

hackernews · mmastrac · 9月10日 13:39 · [社区讨论](https://news.ycombinator.com/item?id=49643546)

**背景**: Rust 是一种通用系统编程语言，强调性能、类型安全、并发和内存安全，能消除 C 和 C++ 中常见的缓冲区溢出和释放后使用等错误。微软的一级语言认定意味着 Rust 现被视为微软项目的核心语言，反映了其在安全关键应用中日益增长的重要性。据 Azure CTO Mark Russinovich 称，微软产品中约 70% 的 CVE 是内存安全问题，而 Rust 正是为防止这些问题而设计的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://rustfoundation.org/media/guest-post-rust-is-tier-1-language-at-microsoft/">Guest Post: Rust Is Tier-1 Language at Microsoft</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rust_(programming_language)">Rust ( programming language ) - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论（585 分，323 条评论）总体积极，评论者指出 Rust 相比 Zig 和 Odin 等较新语言更为成熟，并强调 MSVC 后端集成取代 LLVM 的重要意义。一些人还提到微软的 10 亿行代码转换目标和 DARPA 资助的 C 到 Rust 自动化，作为行业向内存安全更广泛转变的证据。

**标签**: `#Rust`, `#Microsoft`, `#Systems Programming`, `#Memory Safety`, `#Programming Languages`

---

<a id="item-3"></a>
## [DeepSeek 发布 V4.1 Flash，缓存定价极低](https://twitter.com/deepseek_ai/status/2097930608790167907) ⭐️ 9.0/10

DeepSeek 发布了 DeepSeek-V4.1-Flash，这是一款新的前沿规模模型，附带详细技术报告，缓存命中价格低至每百万 token 0.003 美元。该模型已在 Hugging Face 上线，旧的 deepseek-v4-flash 和 deepseek-v4-flash-vision-exp 接口为兼容性暂时路由到 V4.1-Flash。 此次发布表明 DeepSeek 在持续推进前沿规模训练的同时，以极具侵略性的低价压制竞争对手，这可能对其他实验室的 API 经济模型造成压力。其缓存价格之低，让一些开发者认为网络传输成本可能很快会主导任务总成本，从而可能改变聊天补全 API 的使用方式。 该模型拥有 5520 亿参数，几乎是原版 V4 Flash 2840 亿参数的两倍，因此基准测试成绩的提升伴随着更大的模型体积，本地运行难度显著增加。据报道，在一个临时测试版本中其处理速度可达每秒 400 个 token，而 DeepSeek V4-Pro 将于 9 月 14 日停止服务。

hackernews · Liwink · 9月10日 06:11 · [社区讨论](https://news.ycombinator.com/item?id=49639090)

**背景**: 前沿 AI 模型是指在特定时间点上最先进的大规模通用系统，通常基于海量数据训练，具备推理、多模态理解和编程能力。提示缓存让服务商能以折扣价复用此前处理过的输入 token，而 DeepSeek 此次的缓存命中价格远低于 Anthropic 等厂商常见的 0.1 倍基础输入价格折扣。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/en/news/deepseek-v4-1-flash/">DeepSeek | Introducing DeepSeek-V4.1-Flash: smarter, faster ...</a></li>
<li><a href="https://www.digitalapplied.com/blog/deepseek-v4-1-flash-pro-routing-prices-early-tests">DeepSeek V4.1 Flash: Benchmarks, Prices and Pro Cutoff</a></li>
<li><a href="https://redis.io/blog/what-is-prompt-caching/">What Is Prompt Caching? LLM Speed & Cost Guide</a></li>

</ul>
</details>

**社区讨论**: Hacker News 的评论者称赞 DeepSeek 的技术报告细节丰富，并赞赏其以近乎前沿的规模不断推出巧妙想法的大胆节奏，并将其与其他实验室偏重安全的系统卡进行对比。不少人关注每百万 token 0.003 美元的缓存命中价格，猜测网络传输成本是否很快会超过计算成本，也有人指出 5520 亿参数让它在本地使用上远不再“轻量”。

**标签**: `#AI`, `#DeepSeek`, `#LLM`, `#model release`, `#pricing`

---

<a id="item-4"></a>
## [Calif Research 发布 WeWorm：首个通过微信通话传播的零点击蠕虫](https://simonwillison.net/2026/Sep/10/calif-research/) ⭐️ 9.0/10

Calif Research 发布了 WeWorm 的演示，这是首个通过微信通话在 iOS 和 Android 上传播的零点击蠕虫，完全不需要用户交互。该团队利用 AI 在大约两天内找到了内存破坏漏洞并编写了远程代码执行（RCE）利用程序，随后又用一周时间构建了蠕虫。 这标志着 AI 辅助漏洞发现与武器化的重大转变，表明小团队如今能在数天内而非数月内构建大规模蠕虫。它为移动安全、AI 安全以及数十亿微信用户敲响警钟——一个未接来电就可能导致账号被劫持。 受害者无需接听电话或对手机进行任何操作；即使接听，也听不到任何声音，漏洞利用依然成功。Calif Research 已将该严重漏洞私下报告给腾讯，该利用程序针对的是微信通话栈中的内存破坏漏洞。

rss · Simon Willison · 9月10日 00:56

**背景**: 零点击蠕虫无需用户任何操作即可自动传播，不同于需要点击或下载的传统恶意软件。微信是中国极受欢迎的通讯与通话应用，用户超过十亿，因此其通话处理中的任何缺陷都尤为危险。远程代码执行（RCE）是一类允许攻击者在受害者设备上运行自己代码的漏洞，常被用于部署恶意软件或窃取数据。AI 辅助安全研究正在迅速降低发现和武器化此类漏洞所需的时间与技能门槛。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.helpnetsecurity.com/2026/09/08/wechat-weworm-vulnerability-exploit-account-hijacking/">"Zero-click" WeChat worm could hijack accounts and spread via a single call - Help Net Security</a></li>
<li><a href="https://www.martincid.com/technology-sv/wechat-weworm-zero-click-worm-account-hijack/">A missed WeChat call hijacks your account — AI wrote the exploit in two days</a></li>
<li><a href="https://www.cloudflare.com/learning/security/what-is-remote-code-execution/">What is remote code execution?</a></li>

</ul>
</details>

**标签**: `#security`, `#ai-security-research`, `#mobile-exploit`, `#zero-click`, `#wechat`

---

<a id="item-5"></a>
## [DeepSeek 发布 MIT 协议 Harness 应用并开放 V4-Pro-0813 权重](https://t.me/zaihuapd/43738) ⭐️ 9.0/10

DeepSeek 发布了以 MIT 协议开源的 DeepSeek Harness 智能体框架，同时在 Hugging Face 上开放了 DeepSeek-V4-Pro-0813 的模型权重。该 Harness 将模型、工具、技能、会话、沙箱、存储、调度和 UI 等能力设计为可替换插件，并内置标准、PTC、极简和创造四种运行模式。 通过将宽松许可的插件化智能体框架与开放模型权重相结合，DeepSeek 降低了开发者构建和定制智能体工作流的门槛，避免了供应商锁定。这一组合有望加速智能体工具生态的实验进程，并促使竞争对手提供同样开放、模块化的技术栈。 该 Harness 基于 Cordis 插件系统构建，采用“一切皆插件”的架构；其四种模式的区别在于组合方式与信任边界，而非底层模型或操作系统隔离边界——PTC 通过生成代码来编排工具以节省 token，极简模式仅提供 bash 和编辑器用于基准测试。DeepSeek-V4-Pro-0813 是一个大规模混合专家模型，拥有 1,048,576 token 的上下文窗口和 DSpark 推测解码模块，在 OpenRouter 上的定价约为每百万输入 token 0.58 美元、每百万输出 token 1.74 美元。

telegram · zaihuapd · 9月10日 07:28

**背景**: 智能体框架（agent harness）是连接语言模型与工具、记忆、沙箱和用户界面的软件层，实际上把原始模型变成了可工作的智能体。DeepSeek Harness 是 DeepSeek 在这一领域的官方产品，基于 Cordis 插件框架构建，因此每个组件都可以被替换。DeepSeek-V4-Pro-0813 是 DeepSeek V4-Pro 模型的正式版本，取代了此前的预览版，面向文本生成、推理、编程和智能体工具调用等场景。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.deepseek.com/harness/en/">DeepSeek Harness developer preview: Everything is a plugin</a></li>
<li><a href="https://github.com/deepseek-ai/deepseek-harness">GitHub - deepseek -ai/ deepseek - harness : DeepSeek Harness ...</a></li>
<li><a href="https://build.nvidia.com/deepseek-ai/deepseek-v4-pro-0813/modelcard">deepseek-v4-pro-0813 Model by Deepseek-ai | NVIDIA NIM</a></li>

</ul>
</details>

**标签**: `#DeepSeek`, `#open-source`, `#LLM`, `#agent-harness`, `#model-release`

---

<a id="item-6"></a>
## [trynix.dev 通过 qemu-wasm 在浏览器中运行任意 Nix 包](https://simonwillison.net/2026/Sep/10/trynix/) ⭐️ 8.0/10

Farid Zakaria 发布了 trynix.dev，它利用 qemu-wasm 在浏览器中完全启动一个 x86_64 Linux 虚拟机，并能加载过去 13 年间的任意 Nix 包，每个环境都可以通过 URL 直接访问（例如 https://trynix.dev/?pkg=python3%403.6.2）。他还推出了 trynix-preview，这是一个 GitHub Action，会在拉取请求下评论一个链接，让审查者无需服务器即可在浏览器中启动该 PR 的构建。 这让可复现的 Nix 环境可以像普通 URL 一样即时分享，无需安装 Nix 或配置服务器就能查看某个特定版本的包。trynix-preview 则指向一种新的代码审查流程：审查者直接在浏览器中启动拉取请求的真实构建，这可能显著改善可复现构建的验证方式。 该虚拟机由 ktock/qemu-wasm 驱动，它把 QEMU 的 TCG 中间表示翻译成 WebAssembly 模块，并借助 WebAssembly.Module 和 WebAssembly.Instance 等浏览器 API 来执行。由于环境可通过 URL 寻址，像 2017 年的 Python 3.6.2 这样的特定历史版本包只需点击一次即可加载并作为交互式 shell 使用。

rss · Simon Willison · 9月10日 23:44

**背景**: Nix 是一个纯函数式包管理器，它把每个包存放在包含所有输入哈希的不可变路径中，从而保证构建可复现，并让多个版本可以共存而不冲突。QEMU 是通用的机器模拟器，而 qemu-wasm 是一个将其编译为 WebAssembly 的项目，使完整的系统模拟器能够在浏览器标签页内运行。trynix.dev 将两者结合，让 Nix 可复现、按内容寻址的包能够直接从 URL 启动为实时 Linux 虚拟机。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/ktock/qemu-wasm">GitHub - ktock/qemu-wasm: QEMU on browser · GitHub</a></li>
<li><a href="https://nixos.org/">Nix & NixOS | Declarative builds and deployments</a></li>
<li><a href="https://github.com/NixOS/nix">GitHub - NixOS/ nix : Nix , the purely functional package manager</a></li>

</ul>
</details>

**标签**: `#Nix`, `#WebAssembly`, `#Virtualization`, `#Reproducible Builds`, `#Browser`

---

<a id="item-7"></a>
## [Sand.ai 开源全球首个千亿参数 MoE 视频生成模型](https://news.google.com/rss/articles/CBMihAFBVV95cUxOTlQxSlpVUDJCTlctd3V2Vk5MWFpYSFNwMC15V2d4RzVzY0s5eVVSZTJERGlpMXpHNDB3REhrZjFydUNZOHFCX2l0Wm03NE5ORkdPclhkb1lCOGp3NlBrSHFsV1lSZFBiWVdpcV90X3R1YnlteTM1dXdLOXNRdi1sUEdhZjU?oc=5) ⭐️ 8.0/10

Sand.ai 开源了全球首个千亿参数级别的混合专家（MoE）视频生成模型，总参数量达 1140 亿，而每次推理仅激活 60 亿参数。这一发布标志着开源 AI 视频生成领域在规模上的重大里程碑。 这一事件意义重大，因为它证明此前主要在大语言模型中验证的 MoE 架构，可以有效地扩展到视频生成领域，在保持高容量的同时有望降低推理成本。开源发布使更广泛的 AI 研究社区能够研究和基于这一规模的模型进行开发，而此前这种规模的模型只有资源雄厚的实验室才能实现。 该模型采用混合专家设计，每个 token 仅激活部分专家（1140 亿参数中的 60 亿），激活参数量决定推理速度和计算成本，而总参数量决定内存占用。这是 Sand.ai 继此前 Magi-1 自回归视频模型之后的最新发布。

google_news · 新浪网 · 9月10日 01:33

**背景**: 混合专家（MoE）是一种神经网络架构，由多个专门的子网络（称为专家）组成，路由器（门控网络）会为每个输入仅选择最相关的专家。这样模型可以拥有非常大的总参数量，同时保持较低的每 token 计算成本，因为未被选中的专家会被跳过。Sand.ai 是一家以 Magi-1 自回归视频生成模型闻名的 AI 公司，将 MoE 应用于视频生成相比其在大语言模型中的广泛使用是一个相对较新的方向。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mixture_of_experts">Mixture of experts - Wikipedia</a></li>
<li><a href="https://huggingface.co/blog/moe">Mixture of Experts Explained</a></li>
<li><a href="https://sand.ai/">Sand.ai - Advance AI to benefit everyone</a></li>

</ul>
</details>

**标签**: `#MoE`, `#video-generation`, `#open-source`, `#large-scale-models`, `#AI`

---