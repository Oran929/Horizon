---
layout: default
title: "Horizon Summary: 2026-06-25 (ZH)"
date: 2026-06-25
lang: zh
---

> 从 56 条内容中筛选出 14 条重要资讯。

---

1. [Anthropic 指控阿里巴巴窃取 Claude AI 能力](#item-1) ⭐️ 9.0/10
2. [OpenAI 发布首款定制 AI 芯片 'Jalapeno'](#item-2) ⭐️ 9.0/10
3. [Krea 2 开源 120 亿参数图像模型达本地最优性能](#item-3) ⭐️ 9.0/10
4. [Gefen 优化器声称比 AdamW 减少 8 倍内存](#item-4) ⭐️ 9.0/10
5. [高通收购 Modular，Mojo 语言所属公司](#item-5) ⭐️ 8.0/10
6. [NVIDIA 45°C 液冷架构实现数据中心近乎零水耗](#item-6) ⭐️ 8.0/10
7. [开源项目中的 PR 垃圾邮件如同早期电子邮件垃圾邮件](#item-7) ⭐️ 8.0/10
8. [Nub：类似 Bun 的 Node.js 工具包](#item-8) ⭐️ 8.0/10
9. [Datasette 1.0a35 新增创建/修改表 API](#item-9) ⭐️ 8.0/10
10. [为 JIT 编译的 BPF 代码添加 KASAN 支持](#item-10) ⭐️ 8.0/10
11. [SDXL 通过 WebGPU 在浏览器本地运行](#item-11) ⭐️ 8.0/10
12. [AMD Strix Halo NPU 现可用于混合 LLM 推理](#item-12) ⭐️ 8.0/10
13. [通过合并 AWQ 与 FP8 模型并修补 vLLM，GLM5.2 推理速度提升 20 倍](#item-13) ⭐️ 8.0/10
14. [谷歌 Play 在美国、英国、欧洲经济区启用外部计费](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic 指控阿里巴巴窃取 Claude AI 能力](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 9.0/10

Anthropic 公开指控阿里巴巴通过模型蒸馏等技术非法提取其 Claude AI 模型的能力，引发了对知识产权盗窃的担忧。 此案凸显了中美科技公司在 AI 模型安全和知识产权盗窃方面日益紧张的关系，可能导致 AI 行业更严格的监管和执法。 模型蒸馏是一种让小模型从大模型输出中学习的技术，中国实验室可能正在利用这种方法未经授权复制 Claude 的能力。

hackernews · htrp · 6月24日 19:48 · [社区讨论](https://news.ycombinator.com/item?id=48664814)

**背景**: 模型蒸馏（知识蒸馏）是一种机器学习技术，通过训练较小的模型来模仿更大、更强大的模型。它常用于模型压缩和在资源受限设备上部署，但也可能被用来未经许可复制专有模型。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**社区讨论**: 评论者就伦理问题展开辩论，一些人指出 Anthropic 抱怨被抄袭具有讽刺意味，因为大模型本身就是基于抓取的互联网数据训练的。其他人则指出，中国经销商正在提供打折的 Claude 代币，并将推理轨迹作为训练数据出售，从而实现了蒸馏。

**标签**: `#AI`, `#Model Distillation`, `#Intellectual Property`, `#Anthropic`, `#Alibaba`

---

<a id="item-2"></a>
## [OpenAI 发布首款定制 AI 芯片 'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI 宣布了其首款定制 AI 推理芯片 'Jalapeno'，与 Broadcom 合作开发并由 TSMC 制造，声称可将推理成本降低多达 50%。 这标志着 OpenAI 从完全依赖通用 GPU 转向定制硬件的重要转变，有望降低运营成本并提升 AI 服务性能，可能促使其他科技巨头采取类似举措。 该芯片专门针对推理工作负载优化，而非训练，从设计到生产仅用九个月，OpenAI 使用其自身模型加速了设计流程。

hackernews · jamdesk · 6月24日 17:47 · [社区讨论](https://news.ycombinator.com/item?id=48663324)

**背景**: AI 推理芯片是专用处理器，旨在高效运行已训练的 AI 模型，关注速度和每次查询成本，而非训练中使用的原始计算能力。像 NVIDIA 的通用 GPU 通常同时用于训练和推理，但定制芯片可为特定任务提供更高效率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/319012/20260624/openais-first-custom-ai-chip-targets-50-cheaper-inference-jalapeno-unveiled.htm">OpenAI's First Custom AI Chip Targets 50% Cheaper Inference...</a></li>
<li><a href="https://naddod.medium.com/inference-chip-guide-the-foundation-of-scalable-ai-applications-d18f2c22b36c">Inference Chip Guide: The Foundation of Scalable AI Applications | by NADDOD | Medium</a></li>

</ul>
</details>

**社区讨论**: 评论者对 OpenAI 的模型在芯片设计中的作用表示好奇，部分人怀疑这可能是营销噱头。其他人指出该芯片由 TSMC 制造，并讨论了完全硬编码权重芯片实现更高效率的潜力。

**标签**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-3"></a>
## [Krea 2 开源 120 亿参数图像模型达本地最优性能](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 9.0/10

Krea 发布了开源权重的 Krea 2 图像模型，拥有 120 亿参数架构，并附有详细技术报告，描述了训练和数据筛选流程。此次发布包括两个版本：Krea 2 RAW 用于微调，Krea 2 Turbo 用于快速文本到图像推理。 Krea 2 在本地可部署的图像生成模型中实现了最先进的性能，得分仅次于闭源的 Ideogram 4，但推理速度更快。这为更广泛的用户提供了高质量图像合成能力，并成为同类中最优秀的开源权重模型。 Turbo 版本采用了引导和时间步蒸馏技术，仅需 8 步采样即可生成高质量输出。社区基准测试显示 Krea 2 优于所有其他本地可部署模型，唯一的例外是 Ideogram 4，但后者需要几分钟而 Krea 2 只需几秒。

hackernews · mattnewton · 6月23日 15:31 · [社区讨论](https://news.ycombinator.com/item?id=48646659)

**背景**: 开源权重模型将训练好的参数公开，使开发者能够微调并在本地部署，无需依赖封闭的 API。Krea 2 是 Krea AI 从零开始训练的图像基础模型，注重风格多样性和创意控制。该模型设计为可在消费级硬件上运行，使先进的 AI 图像生成更加普及。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.krea.ai/krea-2-open-source">Krea 2 Open-Source: RAW and Turbo Image Models</a></li>
<li><a href="https://github.com/krea-ai/krea-2">GitHub - krea-ai/krea-2: Official inference code for Krea 2 · GitHub</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**社区讨论**: 社区反应非常积极，对详细的技术报告和模型性能表示赞赏。一些评论者指出，虽然 Krea 2 在文生图方面表现出色，但随着先进的图生图和组合模型的出现，它可能是在“打过去的仗”。其他人则强调了 Turbo 版本在速度和质量之间的权衡。

**标签**: `#AI`, `#image generation`, `#open weights`, `#text-to-image`, `#machine learning`

---

<a id="item-4"></a>
## [Gefen 优化器声称比 AdamW 减少 8 倍内存](https://www.reddit.com/r/LocalLLaMA/comments/1uep96s/gefen_is_a_dropin_replacement_for_the_adamw/) ⭐️ 9.0/10

一种名为 Gefen 的新优化器作为 AdamW 的即插即用替代品发布，声称通过共享二阶矩估计并量化一阶矩，将训练内存降低 8 倍。 如果得到验证，Gefen 可能大幅降低训练大型深度学习模型的硬件门槛，因为 AdamW 被广泛使用，其内存开销是一个关键瓶颈。 Gefen 自动跨参数块共享二阶矩估计，并使用学习到的码本量化一阶矩，以最小的精度损失实现内存节省。

reddit · r/LocalLLaMA · /u/indicava · 6月24日 20:39

**背景**: AdamW 是现代深度学习的默认优化器，它为每个参数存储两个动量缓冲区，每个缓冲区与模型权重大小相同，使得优化器状态的内存使用翻倍。Gefen 通过共享和量化这些缓冲区来减少开销。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://pypi.org/project/gefen/">Gefen optimizer for memory-efficient PyTorch training</a></li>
<li><a href="https://arxiv.org/abs/2606.13894">[2606.13894] Gefen : Optimized Stochastic Optimizer</a></li>
<li><a href="https://nefut.com/article/996-csai-gefen-optimized-stochastic-optimizer-with-8x-memory-reduction">[CS.AI] Gefen : Optimized Stochastic Optimizer with 8x Mem... - Nefut</a></li>

</ul>
</details>

**标签**: `#optimizer`, `#memory reduction`, `#deep learning`, `#training efficiency`, `#AdamW`

---

<a id="item-5"></a>
## [高通收购 Modular，Mojo 语言所属公司](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

高通于 2026 年 6 月 24 日宣布收购 AI 初创公司 Modular（Mojo 编程语言的开发者），以增强其人工智能和硬件能力。 此次收购通过获得 Modular 的编译器技术，使高通在 AI 计算领域的地位得到加强——该技术可跨多种硬件实现高性能内核，可能挑战英伟达 CUDA 的主导地位。 据路透社报道，该交易估值约 40 亿美元。Modular 的 Mojo 语言结合了类似 Python 的语法和基于 MLIR 编译器框架的系统级性能，可针对 CPU、GPU 和 ASIC 进行优化。

hackernews · timmyd · 6月24日 13:49 · [社区讨论](https://news.ycombinator.com/item?id=48659798)

**背景**: Mojo 是 Modular 开发的专有编程语言，基于 MLIR（多层中间表示）编译器框架，可针对多种硬件加速器进行优化。它旨在提供类似 Python 的编码体验，同时达到 C++或 CUDA 级别的性能。Modular 还提供 MAX 推理平台，可在英伟达、AMD 和苹果 Silicon 上部署 AI 智能体。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://www.modular.com/">Modular: Inference from Kernel to Cloud</a></li>
<li><a href="https://www.reuters.com/business/ai-startup-modular-raises-250-million-seeks-challenge-nvidia-dominance-2025-09-24/">AI startup Modular raises $250 million, seeks to challenge Nvidia dominance | Reuters</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：有人对 Mojo 可能无法成为真正的跨平台语言感到失望，也有人认为高通在整合 AI 和 RISC-V 能力方面具有战略价值。此次收购也被视为对英伟达 CUDA 生态系统的潜在替代。

**标签**: `#Qualcomm`, `#Modular`, `#Mojo`, `#AI`, `#acquisition`

---

<a id="item-6"></a>
## [NVIDIA 45°C 液冷架构实现数据中心近乎零水耗](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA 推出了一种运行在 45°C 的液冷架构，使数据中心的用水量降至接近零。该设计通过使用更高的冷却液温度，挑战了传统的冷却方式。 这一创新显著降低了 AI 工厂的水资源消耗，解决了环境问题。它还开启了废热再利用于区域供暖的可能性，为当地社区带来经济价值。 该架构采用直接到芯片的液冷，冷却液温度高达 45°C（113°F）。在适宜气候下，它可实现近乎零用水，但具体与外部温度的关联尚未详细说明。

hackernews · nitin_flanker · 6月24日 14:10 · [社区讨论](https://news.ycombinator.com/item?id=48660178)

**背景**: 传统数据中心依赖空调或较低温度的液冷，消耗大量水用于排热。更高温度的液冷减少了对高耗能冷却器和水蒸发的需求。直接到芯片冷却将冷却液直接循环在热组件上，实现高效散热。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45 ° C Liquid Cooling Redefines AI Data Center Energy</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45 ° C Liquid Cooling Design for AI Data Centers</a></li>

</ul>
</details>

**社区讨论**: 评论者指出了与区域供暖协同的潜力，45°C 的废热可用于社区供暖。有人质疑与现有液冷相比的创新性，而其他人分享了在 40°C 下类似方法的实际经验。讨论还提出了对气候依赖性和效率细节的疑问。

**标签**: `#data centers`, `#cooling`, `#energy efficiency`, `#NVIDIA`, `#water conservation`

---

<a id="item-7"></a>
## [开源项目中的 PR 垃圾邮件如同早期电子邮件垃圾邮件](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 8.0/10

Greptile 的一篇博文将开源仓库中拉取请求（PR）垃圾邮件的兴起比作早期电子邮件垃圾邮件，强调了维护者面临的挑战及潜在的解决方案。 PR 垃圾邮件威胁开源项目的生产力和质量。维护者不堪重负可能抑制贡献并损害项目健康，因此有效的缓解策略至关重要。 文章特别提到 AI 生成的'低质'PR 和与 Hacktoberfest 等活动相关的垃圾邮件。工具如 Fossier 使用多信号评分估算垃圾邮件概率，GitHub 最近增加了可配置的 PR 限制。

hackernews · dakshgupta · 6月24日 14:32 · [社区讨论](https://news.ycombinator.com/item?id=48660579)

**背景**: 在 2000 年代初期，电子邮件垃圾邮件充斥收件箱，催生了过滤等技术。类似地，开源仓库收到无关 PR，浪费维护者时间。AI 生成内容和鼓励贡献的活动加剧了问题。项目维护者寻求基于声誉或算法的解决方案来过滤垃圾邮件。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://dev.to/ryan_m_823cbee9f96a9dee29/pr-spam-the-modern-echo-of-early-2000s-email-spam-l1h">PR Spam : The Modern Echo of Early 2000s Email... - DEV Community</a></li>
<li><a href="https://socket.dev/blog/express-js-spam-prs-commoditization-of-open-source">Express.js Spam PRs Incident Highlights the Commoditization ..</a></li>
<li><a href="https://github.com/PThorpe92/fossier">GitHub - PThorpe92/fossier: Vouch-compatible PR - spam reduction...</a></li>

</ul>
</details>

**社区讨论**: 评论指出与电子邮件垃圾邮件的差异（声誉基于服务器而非个人用户），提到 GitHub 新的 PR 限制，并分享经验如要求非文本会议。有评论者建议，如果维护者厌倦 AI 低质 PR，应更新工具以防止提交。

**标签**: `#open source`, `#spam`, `#software engineering`, `#GitHub`, `#maintainer challenges`

---

<a id="item-8"></a>
## [Nub：类似 Bun 的 Node.js 工具包](https://github.com/nubjs/nub) ⭐️ 8.0/10

Nub 通过 --require 预加载钩子集成了基于 oxc 的转译器、模块解析钩子以及现代 API 的 polyfill，在不替换 Node.js 运行时的前提下提供类似 Bun 的开发者体验。 它弥合了 Node.js 与 Bun 的全能开发者体验之间的差距，使 Node.js 中的现代 JavaScript 和 TypeScript 开发更加快速顺畅。这可能会减少切换运行时的动力，并提高现有 Node.js 项目的生产力。 转译器基于 oxc，打包为 Node-API 附加组件以实现高性能。它注册了模块解析钩子，并为 Worker、Temporal 等 API 注入 polyfill，确保代码仍在原生 Node.js 上执行。

hackernews · colinmcd · 6月24日 14:14 · [社区讨论](https://news.ycombinator.com/item?id=48660267)

**背景**: Node.js 是标准的 JavaScript 运行时，但缺乏内置的 TypeScript 支持和现代打包功能，需要借助 ts-node 或 esbuild 等独立工具。Bun 是一种较新的运行时，原生集成了这些特性，但切换运行时可能有风险。Nub 在不改变底层运行时的前提下，利用 Node 的 --require 和模块钩子扩展性，为 Node.js 添加了类似的能力。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://github.com/nodejs/node-addon-api">GitHub - nodejs/node-addon-api: Module for using Node-API from C++ · GitHub</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**社区讨论**: 评论总体积极：pier25 称赞了这个概念，并指出作者背景（Zod 创建者、前 Bun 员工）。ssalbdivad 报告成功无问题地迁移了整个 monorepo。eyelidlessness 对使用 --require 而非 --import 以支持 ESM 提出了担忧，vmsp 则询问鉴于 Node 最近支持 TypeScript 为何还需要转译器。zarzavat 建议用 pnpm 包装来做包管理。

**标签**: `#nodejs`, `#toolkit`, `#bun`, `#typescript`, `#developer-experience`

---

<a id="item-9"></a>
## [Datasette 1.0a35 新增创建/修改表 API](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 8.0/10

Datasette 1.0a35 引入了由 JSON API 支持的“创建表”和“修改表”界面，实现了可编程的数据库管理。还增加了全面的模板上下文文档。 此版本将 Datasette 从只读工具扩展为完整的数据库管理平台。新的 JSON API 和稳定的模板上下文文档为强大的自动化和自定义集成打开了大门。 创建表 API 支持定义列、主键、自定义列类型、NOT NULL 约束、默认值、表达式默认值和单列外键。修改表 API 允许添加、重命名、重新排序和删除列，以及更改列类型、约束和主键。

rss · Simon Willison · 6月23日 21:34

**背景**: Datasette 是一个开源工具，用于通过 Web 界面探索和发布关系数据库，尤其是 SQLite。之前，Datasette 主要专注于只读访问和查询。此版本通过 JSON API 增加了写入能力，使其更像一个数据库管理系统。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.datasette.io/en/1.0a10/json_api.html">JSON API - Datasette documentation</a></li>

</ul>
</details>

**标签**: `#datasette`, `#database`, `#json-api`, `#release`, `#open-source`

---

<a id="item-10"></a>
## [为 JIT 编译的 BPF 代码添加 KASAN 支持](https://lwn.net/Articles/1077740/) ⭐️ 8.0/10

Alexis Lothoré在 2026 年 LSFMM+BPF 峰会上展示了一个补丁，旨在将 Linux 内核的 KASAN 内存访问检查器扩展到 JIT 编译的 BPF 代码，最初针对 x86 架构，专注于 LDX 和 STX 指令。该工作旨在检测 BPF JIT 编译器本身的内存错误。 这项增强意义重大，因为它使 KASAN 能够捕获 BPF JIT 编译器中的释放后使用和越界错误，从而提升内核的安全性和可靠性。由于 BPF 广泛应用于网络、跟踪和安全领域，更好的调试工具有助于防止关键漏洞。 当前补丁因寄存器保存/恢复开销，将每个内存访问指令转变为大约十二条指令，但 Lothoré认为可以简化。栈访问暂时被忽略，且补丁仅覆盖 LDX（加载）和 STX（存储）指令，不包括其他访问内存的 BPF 操作。

rss · LWN.net · 6月23日 15:53

**背景**: KASAN（内核地址消毒剂）是 Linux 内核的动态内存错误检测器，通过编译时插桩或硬件标签检测越界和释放后使用错误。BPF（伯克利包过滤器）程序通常被 JIT 编译为本地机器代码以提高性能，但这绕过了 KASAN 插桩，因为 JIT 直接生成指针解引用而不进行必要检查。Lothoré的工作修改了 JIT 以插入这些检查。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.kernel.org/dev-tools/kasan.html">Kernel Address Sanitizer ( KASAN ) — The Linux Kernel documentation</a></li>
<li><a href="https://google.github.io/kernel-sanitizers/KASAN">Kernel Address Sanitizer ( KASAN ) | kernel -sanitizers</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-07-ebpf-kernel-parameter-tuning/view">How to Tune Kernel Parameters for eBPF Performance</a></li>

</ul>
</details>

**标签**: `#KASAN`, `#BPF`, `#Linux kernel`, `#JIT compilation`, `#memory debugging`

---

<a id="item-11"></a>
## [SDXL 通过 WebGPU 在浏览器本地运行](https://www.reddit.com/r/LocalLLaMA/comments/1uemzsb/sdxl_running_locally_in_the_browser_on_webgpu/) ⭐️ 8.0/10

一个浏览器扩展通过 WebGPU 和 ONNX 模型实现了本地 SDXL 图像生成，无需虚拟环境或复杂配置。 这极大地降低了用户在本地运行强大扩散模型的门槛，使 AI 图像生成更加普及和隐私安全。 目前支持 SDXL-Lighting fp16（约 7 GB 显存）和 4 位版本（约 3.6 GB 显存）。在 MacBook M4 上每张图像生成约需 50-60 秒。

reddit · r/LocalLLaMA · /u/xoqq · 6月24日 19:15

**背景**: WebGPU 是一种用于访问 GPU 的现代浏览器 API，旨在取代 WebGL。ONNX 是一种开放格式，用于表示机器学习模型。SDXL 使用 UNet 架构进行去噪，并包含文本编码器和 VAE。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>
<li><a href="https://en.wikipedia.org/wiki/ONNX">ONNX</a></li>

</ul>
</details>

**标签**: `#WebGPU`, `#SDXL`, `#browser extension`, `#local inference`, `#ONNX`

---

<a id="item-12"></a>
## [AMD Strix Halo NPU 现可用于混合 LLM 推理](https://www.reddit.com/r/LocalLLaMA/comments/1uegdu0/big_news_for_amd_strix_halo_owners/) ⭐️ 8.0/10

AMD Strix Halo NPU 现在支持通过 ROCm 进行混合 LLM 推理，可以在 NPU 上进行提示处理，同时 GPU 处理其他任务，从而通过并行工作实现更快的整体推理。 这一进展终于利用了 Strix Halo 设备中的 NPU 硬件，此前该硬件在 LLM 推理中大多闲置。它为 AMD 平台上的本地 LLM 用户带来了显著的性能提升。 混合模式需要专为 NPU 构建的模型，例如 FastFlowLM NPU 模型。Lemonade 等工具提供了易于测试的 GUI，但不建议用于生产环境中的聊天或代理使用。

reddit · r/LocalLLaMA · /u/CSEliot · 6月24日 15:16

**背景**: Strix Halo 系列集成了 iGPU 和强大的 NPU。传统上，AMD 硬件上的 LLM 推理软件支持较差，用户只能依赖 GGUF 和 Vulkan。ROCm 是 AMD 为 GPU 和 NPU 计算提供的开源软件栈，类似于 NVIDIA 的 CUDA。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/rocm.html">AMD ROCm ™ software empowers developers to optimize AI and...</a></li>
<li><a href="https://github.com/ROCm/ROCm">GitHub - ROCm / ROCm : AMD ROCm ™ Software - GitHub Home</a></li>
<li><a href="https://github.com/FastFlowLM/FastFlowLM">FastFlowLM / FastFlowLM : Run LLMs on AMD Ryzen™ AI NPUs in...</a></li>

</ul>
</details>

**标签**: `#AMD`, `#NPU`, `#LLM`, `#ROCm`, `#hybrid inference`

---

<a id="item-13"></a>
## [通过合并 AWQ 与 FP8 模型并修补 vLLM，GLM5.2 推理速度提升 20 倍](https://www.reddit.com/r/LocalLLaMA/comments/1uedlas/i_did_some_model_hacks_and_got_glm52_from_about/) ⭐️ 8.0/10

一位 Reddit 用户通过将 FP8 版本的多 token 预测头与 AWQ 量化权重合并，并修补 vLLM 以处理这些改动，使得 GLM5.2 模型的推理速度从 2.5 tok/s 提升至超过 50 tok/s。 这展示了一种在高性能硬件上大幅加速大型开放权重模型的实用方法，有望降低部署中的推理成本和延迟。 合并过程使用了 CyanKiwi 的 AWQ 量化 GLM5.2 权重和官方 FP8 仓库中的 MTP 头，只需替换少量文件。修补后的 vLLM 在 4 并发下达到约 55 tok/s，单流推理约 45 tok/s。

reddit · r/LocalLLaMA · /u/Reddactor · 6月24日 13:30

**背景**: GLM5.2 是智谱 AI 最新的开放权重模型，以其强大的推理能力著称。AWQ 是一种对硬件友好的量化方法，能在保持精度的同时减小模型体积。多 token 预测头（如这里使用的 MTP 头）允许模型每步预测多个未来 token，结合推测解码等技术可提升吞吐量。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.reddit.com/r/ZaiGLM/comments/1uao4dq/12hour_usage_review_of_glm52_and_a_comparison/">12-Hour Usage Review of GLM5.2, and a Comparison with DeepSeek ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_quantization">AI quantization</a></li>
<li><a href="https://ai.plainenglish.io/medusa-and-tree-attention-accelerating-llms-part-4-0ae0a1dabf31">Medusa and Tree Attention • Accelerating LLMs , Part 4 | by Xavier Fang</a></li>

</ul>
</details>

**标签**: `#LLM`, `#model optimization`, `#inference speedup`, `#vLLM`, `#GLM`

---

<a id="item-14"></a>
## [谷歌 Play 在美国、英国、欧洲经济区启用外部计费](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

从 6 月 30 日起，谷歌 Play 将允许美国、英国和欧洲经济区的开发者提供第三方应用内计费或外部网页链接用于购买，并采用新的费率结构，将服务费与结算费分开。 这一政策变化显著影响开发者的经济状况和应用商店竞争，赋予开发者更多计费选择并可能降低费用，从而可能导致消费者价格下降，并给其他应用商店带来采用类似政策的压力。 根据新结构，年收入首 100 万美元和自动续订订阅的服务费为 10%，其他交易按'新安装'和'现有安装'分类收取不同费率；此外，使用 Google Play 结算的交易需额外支付 5%的附加费，而使用替代计费或外部链接则无需支付该费用。

telegram · zaihuapd · 6月25日 02:33

**背景**: 谷歌 Play 的计费政策一直存在争议，开发者曾批评 30%的佣金比例。此次变更是在部分地区的试点项目以及监管压力之后推出的。新的'Level Up'和'Apps Experience'计划将从 9 月起为符合条件的游戏和应用开发者提供更低费率。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://play.google.com/console/about/levelup/">Google Play Games Level Up | Google Play Console</a></li>
<li><a href="https://play.google.com/console/about/">Google Play for business | Launch & monetize your apps</a></li>

</ul>
</details>

**标签**: `#Android`, `#Google Play`, `#app store billing`, `#developer policy`, `#platform competition`

---