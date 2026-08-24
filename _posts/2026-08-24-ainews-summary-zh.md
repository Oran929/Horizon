---
layout: default
title: "AI行业热点: 2026-08-24 (ZH)"
date: 2026-08-24
lang: zh
briefing: ainews
---

> 从 71 条内容中筛选出 7 条重要资讯。

---

1. [微软画图和照片应用在 AI 图像中嵌入隐形 GUID 水印](#item-1) ⭐️ 8.0/10
2. [IPFS 维护者在 Shipyard 落幕，项目继续](#item-2) ⭐️ 8.0/10
3. [seL4 在 AArch64 上的安全证明完成](#item-3) ⭐️ 8.0/10
4. [你的可执行文件就是一个 SQLite 数据库](#item-4) ⭐️ 8.0/10
5. [英伟达 60 亿美元打造开源 AI 模型](#item-5) ⭐️ 7.0/10
6. [小米 AI Cube 原型机：三颗自研芯片本地运行大模型](#item-6) ⭐️ 7.0/10
7. [小米发布三款自研 AI 芯片，构建全生态算力底座](#item-7) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [微软画图和照片应用在 AI 图像中嵌入隐形 GUID 水印](https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/) ⭐️ 8.0/10

微软画图和照片应用现在会在经过 AI 处理的图像中静默嵌入一个不可见的 GUID 水印，即使 AI 处理是在设备本地进行的。该水印在用户不知情的情况下添加，且无法禁用。 这引发了严重的隐私担忧，因为 GUID 可能关联到用户的微软账户，使公司或当局能够追溯图像的来源。这破坏了用户对本地处理和匿名性的期望，并可能被用于监控或版权执法。 水印嵌入在图像数据本身，而不仅仅是元数据，因此难以在不降低图像质量的情况下移除。它适用于 AI 处理的图像，包括在 Copilot+ PC 上使用本地模型的图像，但提示词审核仍然是远程的，这意味着某些数据可能仍会发送到微软服务器。

hackernews · ComputerGuru · 8月24日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=49421158)

**背景**: 隐形水印是一种将隐藏信息嵌入数字媒体的技术，常用于版权保护或内容认证。微软一直在将 AI 功能集成到其内置应用（如画图和照片）中，而这个水印似乎是更广泛的 AI 生成内容标识趋势的一部分。其他公司，如 Anthropic，也开始为 AI 生成的文本和图像添加隐形水印，表明这正成为行业惯例。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://xusheng.dev/posts/reversing/mspaint_invisible_watermark/main/">Microsoft Paint and Photos Embed Server-Issued GUIDs ... :: Xusheng Li</a></li>
<li><a href="https://www.forbes.com/sites/anishasircar/2026/08/13/claude-will-now-leave-a-watermark-on-everything-it-writes-what-does-that-mean/">Anthropic’s Claude Adds Invisible Watermarks To AI-Generated Text</a></li>
<li><a href="https://www.forbes.com/sites/maryroeloffs/2026/08/11/claude-will-put-invisible-watermarks-on-ai-text-and-images-and-the-internet-isnt-happy/">Claude Will Put Invisible Watermarks On AI Text And Images—And The Internet Isn’t Happy</a></li>

</ul>
</details>

**社区讨论**: 社区主要担心隐私影响，一位评论者指出 AI 方面是转移注意力，真正的问题是秘密地在每张图像中添加唯一标识符，这可能导致微软被传唤提供用户数据。另一位评论者提到微软过去在类似实现上很草率，例如错误地在 Azure DevOps 提交上标记 Copilot 水印，并建议避免使用画图和其他启用 LLM 的应用。一些用户还对画图应用已超越简单像素编辑器表示惊讶。

**标签**: `#privacy`, `#watermarking`, `#Microsoft`, `#AI`, `#security`

---

<a id="item-2"></a>
## [IPFS 维护者在 Shipyard 落幕，项目继续](https://ipshipyard.com/blog/2026-the-end-of-ipfs-at-shipyard/) ⭐️ 8.0/10

Shipyard 的 IPFS 维护者团队正在逐步解散，这一消息在 ipshipyard.com 的博客文章中宣布。这标志着 Shipyard 内集中式实施支持的结束，但 IPFS 项目本身通过个人维护者资助继续运行。 这一转变对去中心化网络社区意义重大，因为它标志着 IPFS 维护方式的改变，可能影响开发速度和方向。它也凸显了开源基础设施项目可持续性的挑战，并可能影响社区的信任和采用。 公告澄清这不是 IPFS 的终结，而是向个人维护者资助的过渡。社区讨论指出 Protocol Labs 正在转移重点，并建议像 Iroh 这样的替代项目作为更可持续的选择。

hackernews · iand · 8月24日 15:48 · [社区讨论](https://news.ycombinator.com/item?id=49421489)

**背景**: IPFS（星际文件系统）是一种点对点超媒体协议，旨在通过使用内容寻址而非基于位置的寻址，使网络更快、更安全、更开放。Shipyard 是多个为 IPFS 实现提供维护者的组织之一。该项目已用于去中心化应用和 Web3 项目，包括 NFT 平台，因其分布式存储能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/InterPlanetary_File_System">InterPlanetary File System - Wikipedia</a></li>
<li><a href="https://github.com/ipfs">IPFS Project · GitHub</a></li>

</ul>
</details>

**社区讨论**: 社区评论对公告的措辞表示困惑，一些人最初以为 IPFS 本身要关闭了。对落幕感到悲伤，一些用户批评 Protocol Labs 的方向，建议使用 Iroh 等替代方案。还有人指出对 IPNS 的投入可能阻碍了 webapp 支持，并对在去中心化背景下使用 Google 表单收集反馈进行了幽默批评。

**标签**: `#IPFS`, `#decentralized web`, `#open source`, `#maintenance`, `#community`

---

<a id="item-3"></a>
## [seL4 在 AArch64 上的安全证明完成](https://proofcraft.systems/news-2026/#2026-08-21) ⭐️ 8.0/10

seL4 微内核的安全证明现已在 AArch64 架构上完成，标志着形式化验证的一个重要里程碑。这一成就将 seL4 的已验证安全属性扩展到了广泛使用的 64 位 ARM 架构。 这很重要，因为 AArch64 是移动、嵌入式和服务器市场的主导架构，因此在此平台上验证安全可以增强基于 seL4 构建的系统的信任度。它可能影响依赖高可信操作系统的汽车、航空航天和国防等行业。 这些证明涵盖非 MCS（混合关键性系统）配置，并仅限于单核系统。这意味着已验证的安全属性尚未扩展到多核或混合关键性配置。

hackernews · snvzz · 8月24日 11:32 · [社区讨论](https://news.ycombinator.com/item?id=49418255)

**背景**: seL4 是一个微内核操作系统内核，以其形式化验证而闻名，即其正确性在数学上得到证明。AArch64，也称为 ARM64，是 ARM 架构的 64 位执行状态，于 2011 年随 ARMv8-A 引入。操作系统内核的形式化验证涉及证明实现满足其规范，通常使用 Isabelle/HOL 等工具。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://sel4.systems/Research/pdfs/comprehensive-formal-verification-os-microkernel.pdf">Comprehensive Formal Verification of an OS Microkernel</a></li>
<li><a href="https://en.wikipedia.org/wiki/AArch64">AArch64 - Wikipedia</a></li>
<li><a href="https://dl.acm.org/doi/10.1145/1629575.1629596">seL4 | Proceedings of the ACM SIGOPS 22nd symposium on Operating systems principles</a></li>

</ul>
</details>

**社区讨论**: 社区评论对实际影响表示怀疑，一位用户开玩笑说侧信道时序攻击会使结果失效。另一位指出非 MCS 和单核的限制，其他人则讨论 seL4 的采用情况，并质疑如果没有原生 seL4/Linux，它能否真正提高系统安全性。

**标签**: `#seL4`, `#formal verification`, `#AArch64`, `#security`, `#operating systems`

---

<a id="item-4"></a>
## [你的可执行文件就是一个 SQLite 数据库](https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database) ⭐️ 8.0/10

Farid Zakaria 的博客文章展示了一种技术，可以创建一个 SQLite 数据库文件，该文件可以直接作为二进制文件执行，实际上将 ELF 可执行文件视为数据库。文章探讨了将 SQLite 虚拟表与 ELF 集成，展示了如何将可执行文件作为数据库进行查询和操作。 这一概念挑战了可执行格式和数据库的传统观念，可能开启新的工作流程，使二进制文件可以通过 SQL 查询进行内省和修改。它可能导致更高效的打包和自描述的可执行文件，影响开发者和系统工具。 文章提到将多个闭包打包到单个数据库中，并将自闭包指向系统 PATH 上的每个 ELF 二进制文件，最终在一个 SQLite 文件中包含 1,123 个对象、346,386 个符号和 3,808 个依赖边。该技术利用了 SQLite 的虚拟表机制和 ELF 的可扩展格式。

hackernews · setheron · 8月24日 04:48 · [社区讨论](https://news.ycombinator.com/item?id=49415271)

**背景**: ELF（可执行和可链接格式）是类 Unix 系统上可执行文件和共享库的标准二进制格式，设计灵活且可扩展。SQLite 是一个自包含、无服务器的 SQL 数据库引擎，将数据存储在单个文件中，其虚拟表机制允许外部数据源像表一样被查询。文章结合了这些概念，将可执行文件视为数据库。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/ELF_file_format">ELF file format</a></li>
<li><a href="https://www.sqlite.org/fileformat.html">Database File Format</a></li>
<li><a href="https://fzakaria.com/2026/08/23/your-executable-is-a-sqlite-database">Your executable is a SQLite database | Farid Zakaria’s Blog</a></li>

</ul>
</details>

**社区讨论**: 社区反应热烈，评论称赞虚拟表概念，并讨论潜在应用，如用更高效的格式取代 AppImage。作者指出学术界的反馈不太友好，但评论者认为这个想法新颖且有用。一些评论者还指出，从更广泛的意义上讲，ELF 已经是一个数据库，并建议集成 Lisp 镜像或虚拟文件系统。

**标签**: `#SQLite`, `#ELF`, `#executables`, `#databases`, `#systems`

---

<a id="item-5"></a>
## [英伟达 60 亿美元打造开源 AI 模型](https://news.google.com/rss/articles/CBMif0FVX3lxTE5LaEROUFh6WUtfZl94d1BuV1QxaUYwVEk0Z19IbVlxN1RHakFHT0RrLWMtZ0JVS19IWkNMYkhfVmZwaWhibkxsd0lmeUhKc3gwYkRicC1PRmFVaFFWUFV3aFQ3anQ3b2E2V3FHQ1lKaXZQT0xkc3JNaU1wQ1NrU3c?oc=5) ⭐️ 7.0/10

英伟达 CEO 黄仁勋正投资约 60 亿美元与 AI 初创公司 Poolside 达成协议，开发领先的美国开源权重 AI 模型，旨在与中国的 DeepSeek、Kimi K3 和 Qwen 竞争。这标志着英伟达大举进军开源 AI 模型领域。 这项投资凸显了全球 AI 竞赛的升级，尤其是开源权重模型的战略重要性。它可能通过提供美国对中国的开源模型的强大替代品，重塑竞争格局，影响全球开发者和企业。 该交易涉及英伟达支付 60 亿美元获得 Poolside 的 AI 模型开发软件许可并聘用其团队。黄仁勋还公开倡导开源权重 AI，警告不要过度监管，并指出出口管制在很大程度上适得其反，促使中国发展自己的开源生态系统。

google_news · 手机新浪网 · 8月24日 10:47

**背景**: 开源权重 AI 模型，如 DeepSeek 和 Qwen 的模型，因其可访问性和可定制性而受到重视，允许开发者针对特定任务进行微调。英伟达传统上是硬件领导者，现在正扩展到软件和模型开发，以加强其在 AI 生态系统中的地位。美国政府一直在考虑对 AI 技术实施出口管制，这引发了关于其对创新和竞争力影响的辩论。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://techstartups.com/2026/08/24/nvidia-to-invest-6-billion-to-build-u-s-open-weight-ai-model-alternative-to-chinas-deepseek-kimi-k3-and-qwen/">Nvidia to invest $6 billion to build U.S. open-weight AI model alternative to China’s DeepSeek, Kimi K3, and Qwen - Tech Startups</a></li>
<li><a href="https://www.pymnts.com/news/artificial-intelligence/2026/nvidia-pays-6-billion-to-license-poolside-ai-model-development-software/">Nvidia Pays $6 Billion to License Poolside AI Model-Development Software | PYMNTS.com</a></li>
<li><a href="https://fortune.com/2026/07/24/jensen-huang-open-source-letter-nvidia-kimi/">Jensen Huang just used his first ever X post to warn the AI ... | Fortune</a></li>

</ul>
</details>

**标签**: `#AI`, `#Open Source`, `#Nvidia`, `#Investment`

---

<a id="item-6"></a>
## [小米 AI Cube 原型机：三颗自研芯片本地运行大模型](https://news.google.com/rss/articles/CBMif0FVX3lxTE0zVTNxemRMcEtpalRTNlhrbDg5NnZEeGdkWG9SMlZ2ZFRRblo3ZFVLSUVoNm50VUpxX3lDZ0ZHaHRONDBmTERza2ZaNjIwNHZKNGZfTl9UbnhibWpMM1JNYUV1YW1wZTNxcnY1WlZWRDVycGJfME11RHpXaHNEVUk?oc=5) ⭐️ 7.0/10

雷军宣布了 AI Cube 工程原型机，这是一款紧凑型迷你 PC，采用三颗自研 Xring 芯片（O3、O100 和 D100）在本地运行大语言模型。该设备目前仍是原型，尚未确认发布日期或定价。 这标志着边缘 AI 的重要一步，因为在自研芯片上本地运行大语言模型可以减少对云服务的依赖，并改善隐私和延迟。这也反映了大型科技公司为 AI 推理开发定制芯片的更广泛行业趋势。 AI Cube 结合了 Xring O3、O100 和 D100 芯片，据报道可实现 1.22 TB/s 的内存带宽和 330 TOPS 的 AI 性能。它是一款工程原型，因此可用性和商业可行性仍不确定。

google_news · 手机新浪网 · 8月24日 16:43

**背景**: 大语言模型通常需要强大的云服务器，但边缘 AI 旨在本地设备上运行它们，以获得更快的响应和更好的数据隐私。定制芯片越来越被视为优化 AI 工作负载的方式，正如 OpenAI 和 Anthropic 等公司开发自己的芯片一样。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://aicybr.com/blog/xiaomi-ai-cube-xring-o100-local-ai">Xiaomi AI Cube and Xring O100: 1.22 TB/s, 330... | AiCybr Blog</a></li>
<li><a href="https://www.gizmochina.com/2026/08/24/xiaomi-announces-ai-cube-mini-pc-with-xring-o3-o100-and-d100-to-run-llms-locally/">Xiaomi announces AI Cube mini-PC with XRING O3, O100, and D100...</a></li>
<li><a href="https://www.notebookcheck.net/Xiaomi-unveils-AI-Cube-mini-PC-with-three-Xring-chips-and-150-W-performance.1376717.0.html">Xiaomi unveils AI Cube mini PC with three... - Notebookcheck News</a></li>

</ul>
</details>

**标签**: `#AI hardware`, `#large language models`, `#self-developed chips`, `#prototype`, `#edge AI`

---

<a id="item-7"></a>
## [小米发布三款自研 AI 芯片，构建全生态算力底座](https://news.google.com/rss/articles/CBMiTkFVX3lxTE1kSFNQa0FDbndpZFpLTlZOVmMtMWZiZzJHQUhpWGc4YjZMcFgtMWM3T2xsalIzSFhIOXJiU3R4U2FsNHZCNUhkME9wQ0o4dw?oc=5) ⭐️ 7.0/10

8 月 24 日，小米在玄戒芯片技术沟通会上发布了三款自研 AI 芯片：AI 旗舰 SoC 玄戒 O3、高带宽 AI 加速芯片玄戒 O100 和智驾高算力 AI 芯片玄戒 D100。其中 O3 采用 3nm 工艺，拥有 240 亿晶体管，将首发于小米 18 Fold 折叠屏手机。 这标志着小米在 AI 硬件领域的重大布局，旨在为其人车家全生态构建统一的算力底座。此举使小米成为 AI 芯片领域的有力竞争者，有望减少对外部供应商的依赖，并实现跨设备的深度 AI 整合。 玄戒 O3 采用 10 核全大核 CPU、16 核 GPU，NPU 算力达 200 TOPS，安兔兔跑分首次突破 500 万。O100 是行业首颗 6nm 3D 晶圆级堆栈 AI 加速芯片，带宽达 1.22TB/s；D100 则采用 3nm 工艺，定位智驾高算力。小米还展示了搭载三颗芯片的 AI Cube 迷你主机，支持大模型本地部署。

google_news · AIBase · 8月24日 07:16

**背景**: 小米一直在研发自研芯片，以提升产品差异化并强化其生态系统。玄戒系列是小米整体 AI 战略的一部分，旨在为智能手机、汽车和智能家居设备中的 AI 应用提供物理算力基础。这些芯片设计用于高效处理 AI 工作负载，从设备端推理到自动驾驶。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ithome.com/0/993/498.htm">240 亿晶体管数量！ 小米首款 AI 旗舰 SoC 玄 戒 O 3 亮相，采用 3nm...</a></li>
<li><a href="https://m.ithome.com/html/993512.htm">行业首颗 6nm 3D 晶圆级堆栈的 AI 加速 芯 片 ：小米 玄 戒 O 100 官宣 - IT...</a></li>
<li><a href="https://m.21jingji.com/article/20260824/herald/209df8825050cbd5e41f4842a8ff7b22.html">“3000...”</a></li>

</ul>
</details>

**标签**: `#AI chips`, `#Xiaomi`, `#hardware`, `#ecosystem`

---