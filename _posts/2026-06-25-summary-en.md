---
layout: default
title: "Horizon Summary: 2026-06-25 (EN)"
date: 2026-06-25
lang: en
---

> From 56 items, 14 important content pieces were selected

---

1. [Anthropic accuses Alibaba of stealing Claude AI capabilities](#item-1) ⭐️ 9.0/10
2. [OpenAI Unveils First Custom AI Chip 'Jalapeno'](#item-2) ⭐️ 9.0/10
3. [Krea 2: Open-weights 12B image model achieves SOTA among local models](#item-3) ⭐️ 9.0/10
4. [Gefen Optimizer Claims 8x Memory Reduction Over AdamW](#item-4) ⭐️ 9.0/10
5. [Qualcomm Acquires Modular, Owner of Mojo Language](#item-5) ⭐️ 8.0/10
6. [NVIDIA's 45°C Liquid Cooling Cuts Data Center Water Use Near Zero](#item-6) ⭐️ 8.0/10
7. [PR spam in open source mirrors early email spam problem](#item-7) ⭐️ 8.0/10
8. [Nub: A Bun-like toolkit for Node.js](#item-8) ⭐️ 8.0/10
9. [Datasette 1.0a35 Adds Create/Alter Table APIs](#item-9) ⭐️ 8.0/10
10. [KASAN Support for JIT-Compiled BPF Code](#item-10) ⭐️ 8.0/10
11. [SDXL runs locally in browser via WebGPU](#item-11) ⭐️ 8.0/10
12. [AMD Strix Halo NPU Now Usable for Hybrid LLM Inference](#item-12) ⭐️ 8.0/10
13. [20x speedup on GLM5.2 via AWQ/FP8 merge and vLLM patch](#item-13) ⭐️ 8.0/10
14. [Google Play to Launch External Billing in US, UK, EEA](#item-14) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Anthropic accuses Alibaba of stealing Claude AI capabilities](https://www.reuters.com/world/china/anthropic-says-alibaba-illicitly-extracted-claude-ai-model-capabilities-2026-06-24/) ⭐️ 9.0/10

Anthropic has publicly accused Alibaba of illicitly extracting capabilities from its Claude AI model, likely through model distillation techniques, raising concerns about intellectual property theft. This case highlights growing tensions over AI model security and IP theft between US and Chinese tech firms, potentially leading to stricter regulations and enforcement in the AI industry. Model distillation is a technique where a smaller 'student' model learns from a larger 'teacher' model's outputs, and Chinese labs may be using this to replicate Claude's capabilities without authorization.

hackernews · htrp · Jun 24, 19:48 · [Discussion](https://news.ycombinator.com/item?id=48664814)

**Background**: Model distillation, or knowledge distillation, is a machine learning technique where a smaller model is trained to mimic a larger, more capable model. It is commonly used for model compression and deployment on resource-constrained devices, but it can also be used to replicate proprietary models without permission.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Knowledge_distillation">Knowledge distillation - Wikipedia</a></li>

</ul>
</details>

**Discussion**: Commenters debate the ethics, with some noting the irony of Anthropic complaining about copying given that large models are trained on scraped internet data. Others point out that Chinese resellers are offering discounted Claude tokens and selling reasoning traces as training data, enabling distillation.

**Tags**: `#AI`, `#Model Distillation`, `#Intellectual Property`, `#Anthropic`, `#Alibaba`

---

<a id="item-2"></a>
## [OpenAI Unveils First Custom AI Chip 'Jalapeno'](https://techcrunch.com/2026/06/24/openai-unveils-its-first-custom-chip-built-by-broadcom/) ⭐️ 9.0/10

OpenAI announced its first custom AI inference chip named 'Jalapeno,' developed in collaboration with Broadcom and manufactured by TSMC, claiming it can reduce inference costs by up to 50%. This marks a significant shift for OpenAI from relying solely on general-purpose GPUs to custom hardware, potentially lowering operational costs and improving performance for its AI services, and could spur similar moves by other tech giants. The chip is optimized specifically for inference workloads, not training, and was developed from design to production in just nine months, with OpenAI's own models used to accelerate the design process.

hackernews · jamdesk · Jun 24, 17:47 · [Discussion](https://news.ycombinator.com/item?id=48663324)

**Background**: AI inference chips are specialized processors designed to run trained AI models efficiently, focusing on speed and cost-per-query rather than raw compute power used in training. General-purpose GPUs like NVIDIA's are commonly used for both training and inference, but custom chips can offer better efficiency for specific tasks.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techtimes.com/articles/319012/20260624/openais-first-custom-ai-chip-targets-50-cheaper-inference-jalapeno-unveiled.htm">OpenAI's First Custom AI Chip Targets 50% Cheaper Inference...</a></li>
<li><a href="https://naddod.medium.com/inference-chip-guide-the-foundation-of-scalable-ai-applications-d18f2c22b36c">Inference Chip Guide: The Foundation of Scalable AI Applications | by NADDOD | Medium</a></li>

</ul>
</details>

**Discussion**: Commenters expressed curiosity about the role of OpenAI's models in chip design, with some skepticism that it might be marketing fluff. Others noted the chip is manufactured by TSMC and discussed the potential of fully hardcoded weight chips for even greater efficiency.

**Tags**: `#AI hardware`, `#OpenAI`, `#custom chip`, `#inference`, `#Broadcom`

---

<a id="item-3"></a>
## [Krea 2: Open-weights 12B image model achieves SOTA among local models](https://www.krea.ai/blog/krea-2-technical-report) ⭐️ 9.0/10

Krea has released the open-weights Krea 2 image model with a 12B parameter architecture, along with a comprehensive technical report detailing its training and data curation pipeline. The release includes two variants: Krea 2 RAW for fine-tuning and Krea 2 Turbo for fast text-to-image inference. Krea 2 achieves state-of-the-art performance among locally hostable image generation models, scoring just below the proprietary Ideogram 4 but with much faster inference. This opens up high-quality image synthesis to a wider audience and benchmarks as the best open-weights model in its class. The Turbo model uses both guidance and timestep distillation, enabling high-quality outputs in as few as 8 sampling steps. Community benchmarks show Krea 2 outperforming all other locally hostable models, with Ideogram 4 being the only exception, but taking minutes compared to seconds for Krea 2.

hackernews · mattnewton · Jun 23, 15:31 · [Discussion](https://news.ycombinator.com/item?id=48646659)

**Background**: Open-weights models make the trained parameters publicly available, enabling developers to fine-tune and deploy them locally without relying on closed APIs. Krea 2 is an image foundation model trained from scratch by Krea AI, focusing on stylistic diversity and creative control. The model is designed to be run on consumer hardware, making advanced AI image generation more accessible.

<details><summary>References</summary>
<ul>
<li><a href="https://www.krea.ai/krea-2-open-source">Krea 2 Open-Source: RAW and Turbo Image Models</a></li>
<li><a href="https://github.com/krea-ai/krea-2">GitHub - krea-ai/krea-2: Official inference code for Krea 2 · GitHub</a></li>
<li><a href="https://opensource.org/ai/open-weights">Open Weights: not quite what you’ve been told</a></li>

</ul>
</details>

**Discussion**: Community reactions are highly positive, with praise for the detailed technical report and the model's performance. Some commenters note that while Krea 2 excels in text-to-image, it may be 'fighting the past war' as advanced image-to-image and agentic composition models emerge. Others highlight the Turbo variant's speed and quality trade-off.

**Tags**: `#AI`, `#image generation`, `#open weights`, `#text-to-image`, `#machine learning`

---

<a id="item-4"></a>
## [Gefen Optimizer Claims 8x Memory Reduction Over AdamW](https://www.reddit.com/r/LocalLLaMA/comments/1uep96s/gefen_is_a_dropin_replacement_for_the_adamw/) ⭐️ 9.0/10

A new optimizer called Gefen has been released as a drop-in replacement for AdamW, claiming an 8x reduction in training memory by sharing second-moment estimates and quantizing the first moment. If validated, Gefen could significantly lower the hardware barrier for training large deep learning models, as AdamW is widely used and its memory overhead is a key bottleneck. Gefen automatically shares second-moment estimates across parameter blocks and uses a learned codebook to quantize the first moment, achieving memory savings with minimal accuracy loss.

reddit · r/LocalLLaMA · /u/indicava · Jun 24, 20:39

**Background**: AdamW is a default optimizer in modern deep learning that stores two momentum buffers per parameter, each the size of the model weights, doubling memory usage for optimizer states. Gefen reduces this overhead by sharing and quantizing these buffers.

<details><summary>References</summary>
<ul>
<li><a href="https://pypi.org/project/gefen/">Gefen optimizer for memory-efficient PyTorch training</a></li>
<li><a href="https://arxiv.org/abs/2606.13894">[2606.13894] Gefen : Optimized Stochastic Optimizer</a></li>
<li><a href="https://nefut.com/article/996-csai-gefen-optimized-stochastic-optimizer-with-8x-memory-reduction">[CS.AI] Gefen : Optimized Stochastic Optimizer with 8x Mem... - Nefut</a></li>

</ul>
</details>

**Tags**: `#optimizer`, `#memory reduction`, `#deep learning`, `#training efficiency`, `#AdamW`

---

<a id="item-5"></a>
## [Qualcomm Acquires Modular, Owner of Mojo Language](https://www.reuters.com/business/qualcomm-buy-ai-startup-modular-2026-06-24/) ⭐️ 8.0/10

Qualcomm announced its acquisition of Modular, the AI startup behind the Mojo programming language, on June 24, 2026, to bolster its AI and hardware capabilities. This acquisition strengthens Qualcomm's position in AI computing by gaining Modular's compiler technology, which enables high-performance kernels across diverse hardware, potentially challenging Nvidia's CUDA dominance. The deal is reportedly valued at $4 billion, according to Reuters. Modular's Mojo language combines Python-like syntax with system-level performance using the MLIR compiler framework, targeting CPUs, GPUs, and ASICs.

hackernews · timmyd · Jun 24, 13:49 · [Discussion](https://news.ycombinator.com/item?id=48659798)

**Background**: Mojo is a proprietary programming language developed by Modular that builds on MLIR (Multi-Level Intermediate Representation), a compiler framework that allows optimization for various hardware accelerators. It aims to provide a Python-like experience with performance comparable to C++ or CUDA. Modular also offers the MAX inference platform for deploying AI agents across NVIDIA, AMD, and Apple Silicon.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_(programming_language)">Mojo (programming language)</a></li>
<li><a href="https://www.modular.com/">Modular: Inference from Kernel to Cloud</a></li>
<li><a href="https://www.reuters.com/business/ai-startup-modular-raises-250-million-seeks-challenge-nvidia-dominance-2025-09-24/">AI startup Modular raises $250 million, seeks to challenge Nvidia dominance | Reuters</a></li>

</ul>
</details>

**Discussion**: Community reactions are mixed: some express disappointment that Mojo may not become a truly cross-platform language, while others see strategic value for Qualcomm in assembling AI and RISC-V capabilities. The acquisition is also viewed as a potential alternative to Nvidia's CUDA ecosystem.

**Tags**: `#Qualcomm`, `#Modular`, `#Mojo`, `#AI`, `#acquisition`

---

<a id="item-6"></a>
## [NVIDIA's 45°C Liquid Cooling Cuts Data Center Water Use Near Zero](https://blogs.nvidia.com/blog/liquid-cooling-ai-factories/) ⭐️ 8.0/10

NVIDIA has introduced a liquid cooling architecture that operates at 45°C, enabling near-zero water usage in data centers. This design challenges traditional cooling methods by using higher coolant temperatures. This innovation significantly reduces water consumption in AI factories, addressing environmental concerns. It also opens up possibilities for waste heat reuse in district heating, adding economic value to local communities. The architecture uses direct-to-chip liquid cooling with coolant temperatures up to 45°C (113°F). In favorable climates, it can achieve near-zero water usage, though the exact correlation with outside temperatures is not detailed.

hackernews · nitin_flanker · Jun 24, 14:10 · [Discussion](https://news.ycombinator.com/item?id=48660178)

**Background**: Traditional data centers rely on air conditioning or lower-temperature liquid cooling, consuming large amounts of water for heat rejection. Liquid cooling at higher temperatures reduces the need for energy-intensive chillers and water evaporation. Direct-to-chip cooling circulates coolant directly over hot components for efficient heat removal.

<details><summary>References</summary>
<ul>
<li><a href="https://www.techbuzz.ai/articles/nvidia-s-45-c-liquid-cooling-redefines-ai-data-center-energy">NVIDIA's 45 ° C Liquid Cooling Redefines AI Data Center Energy</a></li>
<li><a href="https://www.guru3d.com/story/nvidia-unveils-liquid-cooling-design-for-ai-data-centers/">NVIDIA Unveils 45 ° C Liquid Cooling Design for AI Data Centers</a></li>

</ul>
</details>

**Discussion**: Commenters noted the potential for district heating synergy, with waste heat at 45°C being usable for community heating. Some questioned the innovation compared to existing liquid cooling, while others shared practical experiences with similar approaches at 40°C. The discussion also raised questions about climate dependency and efficiency details.

**Tags**: `#data centers`, `#cooling`, `#energy efficiency`, `#NVIDIA`, `#water conservation`

---

<a id="item-7"></a>
## [PR spam in open source mirrors early email spam problem](https://www.greptile.com/blog/prs-on-openclaw) ⭐️ 8.0/10

A blog post by Greptile compares the rise of pull request (PR) spam in open source repositories to the early days of email spam, highlighting the challenges for maintainers and potential solutions. PR spam threatens the productivity and quality of open source projects. As maintainers are overwhelmed, it could discourage contributions and degrade project health, making effective mitigation strategies essential. The article specifically mentions AI-generated 'slop' PRs and spam related to events like Hacktoberfest. Tools like Fossier use multi-signal scoring to estimate spam probability, and GitHub recently added configurable PR limits for maintainers.

hackernews · dakshgupta · Jun 24, 14:32 · [Discussion](https://news.ycombinator.com/item?id=48660579)

**Background**: In the early 2000s, email spam overwhelmed inboxes with unsolicited messages, leading to technologies like filters. Similarly, open source repos receive unsolicited PRs that waste maintainers' time. The problem is exacerbated by AI-generated content and events encouraging contributions. Project maintainers seek reputation-based or algorithmic solutions to filter spam.

<details><summary>References</summary>
<ul>
<li><a href="https://dev.to/ryan_m_823cbee9f96a9dee29/pr-spam-the-modern-echo-of-early-2000s-email-spam-l1h">PR Spam : The Modern Echo of Early 2000s Email... - DEV Community</a></li>
<li><a href="https://socket.dev/blog/express-js-spam-prs-commoditization-of-open-source">Express.js Spam PRs Incident Highlights the Commoditization ..</a></li>
<li><a href="https://github.com/PThorpe92/fossier">GitHub - PThorpe92/fossier: Vouch-compatible PR - spam reduction...</a></li>

</ul>
</details>

**Discussion**: Comments highlight differences from email spam (reputation based on servers vs. individual users), point to GitHub's new PR limits, and share experiences like requiring non-textual meetings before merging. One commenter suggests that if maintainers are tired of AI slop PRs, they should update their tools to prevent them.

**Tags**: `#open source`, `#spam`, `#software engineering`, `#GitHub`, `#maintainer challenges`

---

<a id="item-8"></a>
## [Nub: A Bun-like toolkit for Node.js](https://github.com/nubjs/nub) ⭐️ 8.0/10

Nub provides a Bun-like developer experience for Node.js by adding a transpiler (based on oxc), a module resolution hook, and polyfills for modern APIs via a --require preload hook, all without replacing the Node.js runtime. It bridges the gap between Node.js and the all-in-one developer experience of Bun, making modern JavaScript and TypeScript development in Node.js faster and smoother. This could reduce the incentive to switch runtimes and improve productivity for existing Node.js projects. The transpiler is powered by oxc, packaged as a Node-API add-on for high performance. It registers a module resolution hook and injects polyfills for APIs like Worker and Temporal, keeping the execution on stock Node.js.

hackernews · colinmcd · Jun 24, 14:14 · [Discussion](https://news.ycombinator.com/item?id=48660267)

**Background**: Node.js is the standard JavaScript runtime but lacks built-in TypeScript support and modern bundling, requiring separate tools like ts-node or esbuild. Bun is a newer runtime that integrates these features natively, but switching runtimes can be risky. Nub adds similar capabilities to Node.js without changing the underlying runtime, leveraging Node's --require and module hooks for extensibility.

<details><summary>References</summary>
<ul>
<li><a href="https://github.com/oxc-project/oxc">GitHub - oxc-project/oxc: ⚓ A collection of high-performance JavaScript tools.</a></li>
<li><a href="https://github.com/nodejs/node-addon-api">GitHub - nodejs/node-addon-api: Module for using Node-API from C++ · GitHub</a></li>
<li><a href="https://bun.sh/">Bun — A fast all-in-one JavaScript runtime</a></li>

</ul>
</details>

**Discussion**: Comments were generally positive: pier25 praised the concept and noted the author's background (creator of Zod, ex-Bun). ssalbdivad reported immediate success migrating a monorepo. eyelidlessness raised concerns about using --require vs --import for ESM support, while vmsp asked why a transpiler is needed given Node's recent TypeScript support. zarzavat suggested wrapping pnpm for package management.

**Tags**: `#nodejs`, `#toolkit`, `#bun`, `#typescript`, `#developer-experience`

---

<a id="item-9"></a>
## [Datasette 1.0a35 Adds Create/Alter Table APIs](https://simonwillison.net/2026/Jun/23/datasette/#atom-everything) ⭐️ 8.0/10

Datasette 1.0a35 introduces new 'Create table' and 'Alter table' interfaces backed by JSON APIs, enabling programmatic database management. It also adds comprehensive template context documentation. This release significantly extends Datasette's capabilities from a read-only tool to a full database management platform. The new JSON APIs and stable template context documentation open the door for powerful automation and custom integrations. The create table API supports defining columns, primary keys, custom column types, NOT NULL constraints, defaults, expression defaults, and single-column foreign keys. The alter table API allows adding, renaming, reordering, and dropping columns, as well as changing column types, constraints, and primary keys.

rss · Simon Willison · Jun 23, 21:34

**Background**: Datasette is an open-source tool for exploring and publishing relational databases, especially SQLite, through a web interface. Previously, Datasette mainly focused on read-only access and querying. This release adds write capabilities through JSON APIs, making it more like a database management system.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.datasette.io/en/1.0a10/json_api.html">JSON API - Datasette documentation</a></li>

</ul>
</details>

**Tags**: `#datasette`, `#database`, `#json-api`, `#release`, `#open-source`

---

<a id="item-10"></a>
## [KASAN Support for JIT-Compiled BPF Code](https://lwn.net/Articles/1077740/) ⭐️ 8.0/10

Alexis Lothoré presented a patch at the 2026 LSFMM+BPF Summit to extend the Linux kernel's KASAN memory access checker to JIT-compiled BPF code, initially targeting x86 and focusing on LDX and STX instructions. The work aims to detect memory bugs in the BPF JIT compiler itself. This enhancement is significant because it enables KASAN to catch use-after-free and out-of-bounds bugs in the BPF JIT compiler, improving kernel security and reliability. As BPF is widely used for networking, tracing, and security, better debugging tools help prevent critical vulnerabilities. The current patch turns each memory access instruction into about twelve instructions due to register save/restore overhead, though Lothoré believes this can be simplified. Stack accesses are temporarily ignored, and the patch only covers LDX (load) and STX (store) instructions, not other memory-accessing BPF operations.

rss · LWN.net · Jun 23, 15:53

**Background**: KASAN (Kernel Address Sanitizer) is a dynamic memory error detector for the Linux kernel that detects out-of-bounds and use-after-free bugs using compile-time instrumentation or hardware tagging. BPF (Berkeley Packet Filter) programs are often JIT-compiled to native machine code for performance, but this bypasses KASAN instrumentation because the JIT emits direct pointer dereferences without the necessary checks. Lothoré's work modifies the JIT to insert those checks.

<details><summary>References</summary>
<ul>
<li><a href="https://docs.kernel.org/dev-tools/kasan.html">Kernel Address Sanitizer ( KASAN ) — The Linux Kernel documentation</a></li>
<li><a href="https://google.github.io/kernel-sanitizers/KASAN">Kernel Address Sanitizer ( KASAN ) | kernel -sanitizers</a></li>
<li><a href="https://oneuptime.com/blog/post/2026-01-07-ebpf-kernel-parameter-tuning/view">How to Tune Kernel Parameters for eBPF Performance</a></li>

</ul>
</details>

**Tags**: `#KASAN`, `#BPF`, `#Linux kernel`, `#JIT compilation`, `#memory debugging`

---

<a id="item-11"></a>
## [SDXL runs locally in browser via WebGPU](https://www.reddit.com/r/LocalLLaMA/comments/1uemzsb/sdxl_running_locally_in_the_browser_on_webgpu/) ⭐️ 8.0/10

A browser extension enables local SDXL image generation using WebGPU and ONNX models, requiring no virtual environments or complex setup. This dramatically lowers the barrier for users to run powerful diffusion models locally, making AI image generation more accessible and private. Currently supports SDXL-Lighting fp16 (~7 GB VRAM) and a 4-bit version (~3.6 GB VRAM). Generation on a MacBook M4 takes about 50-60 seconds per image.

reddit · r/LocalLLaMA · /u/xoqq · Jun 24, 19:15

**Background**: WebGPU is a modern browser API for accessing the GPU, intended to replace WebGL. ONNX is an open format for machine learning models. SDXL uses a UNet architecture for denoising, with text encoders and a VAE.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/WebGPU">WebGPU</a></li>
<li><a href="https://en.wikipedia.org/wiki/ONNX">ONNX</a></li>

</ul>
</details>

**Tags**: `#WebGPU`, `#SDXL`, `#browser extension`, `#local inference`, `#ONNX`

---

<a id="item-12"></a>
## [AMD Strix Halo NPU Now Usable for Hybrid LLM Inference](https://www.reddit.com/r/LocalLLaMA/comments/1uegdu0/big_news_for_amd_strix_halo_owners/) ⭐️ 8.0/10

The AMD Strix Halo NPU now supports hybrid LLM inference using ROCm, enabling prompt processing on the NPU while the GPU handles other tasks. This allows faster overall inference by parallelizing work. This development finally utilizes the NPU hardware in Strix Halo devices, which had been largely idle for LLM inference. It opens up significant performance improvements for local LLM users on AMD platforms. Hybrid mode requires models specifically built for the NPU, such as FastFlowLM NPU models. Tools like Lemonade provide a GUI for easy testing, but are not recommended for production chat or agent usage.

reddit · r/LocalLLaMA · /u/CSEliot · Jun 24, 15:16

**Background**: The Strix Halo series integrates both an iGPU and a powerful NPU. Traditionally, LLM inference on AMD hardware had poor software support, leading users to rely on GGUF and Vulkan. ROCm is AMD's open-source software stack for GPU and NPU compute, similar to CUDA for NVIDIA.

<details><summary>References</summary>
<ul>
<li><a href="https://www.amd.com/en/products/software/rocm.html">AMD ROCm ™ software empowers developers to optimize AI and...</a></li>
<li><a href="https://github.com/ROCm/ROCm">GitHub - ROCm / ROCm : AMD ROCm ™ Software - GitHub Home</a></li>
<li><a href="https://github.com/FastFlowLM/FastFlowLM">FastFlowLM / FastFlowLM : Run LLMs on AMD Ryzen™ AI NPUs in...</a></li>

</ul>
</details>

**Tags**: `#AMD`, `#NPU`, `#LLM`, `#ROCm`, `#hybrid inference`

---

<a id="item-13"></a>
## [20x speedup on GLM5.2 via AWQ/FP8 merge and vLLM patch](https://www.reddit.com/r/LocalLLaMA/comments/1uedlas/i_did_some_model_hacks_and_got_glm52_from_about/) ⭐️ 8.0/10

A Reddit user achieved over 50 tokens per second inference on the GLM5.2 model, up from 2.5 tok/s, by merging the multi-token prediction (MTP) head from the FP8 version with the AWQ quantized weights and patching vLLM to handle the changes. This demonstrates a practical method to dramatically accelerate large open-weight models on high-end hardware, potentially reducing inference costs and latency for deployments. The merge uses CyanKiwi's AWQ quantized GLM5.2 weights and the MTP head from the official FP8 repository, requiring only a few file swaps. The patched vLLM achieves ~55 tok/s at 4x concurrency and ~45 tok/s for single streaming inference.

reddit · r/LocalLLaMA · /u/Reddactor · Jun 24, 13:30

**Background**: GLM5.2 is the latest open-weight model from Zhipu AI, known for strong reasoning performance. AWQ is a hardware-friendly quantization method that reduces model size while preserving accuracy. Multi-token prediction heads, like the MTP head used here, allow a model to predict multiple future tokens per step, improving throughput when combined with techniques like speculative decoding.

<details><summary>References</summary>
<ul>
<li><a href="https://www.reddit.com/r/ZaiGLM/comments/1uao4dq/12hour_usage_review_of_glm52_and_a_comparison/">12-Hour Usage Review of GLM5.2, and a Comparison with DeepSeek ...</a></li>
<li><a href="https://en.wikipedia.org/wiki/AI_quantization">AI quantization</a></li>
<li><a href="https://ai.plainenglish.io/medusa-and-tree-attention-accelerating-llms-part-4-0ae0a1dabf31">Medusa and Tree Attention • Accelerating LLMs , Part 4 | by Xavier Fang</a></li>

</ul>
</details>

**Tags**: `#LLM`, `#model optimization`, `#inference speedup`, `#vLLM`, `#GLM`

---

<a id="item-14"></a>
## [Google Play to Launch External Billing in US, UK, EEA](https://android-developers.googleblog.com/2026/06/play-expanded-billing.html) ⭐️ 8.0/10

Starting June 30, Google Play will allow developers in the US, UK, and European Economic Area to offer third-party in-app billing or external web links for purchases, with a new fee structure that separates service fees from billing fees. This policy change significantly impacts developer economics and app store competition by giving developers more billing options and potentially lower fees, which could lead to reduced prices for consumers and increased pressure on other app stores to adopt similar policies. Under the new structure, the first $1 million in annual revenue and auto-renewing subscriptions have a 10% service fee, while other transactions are classified as 'new install' or 'existing install' with different rates; additionally, transactions using Google Play Billing incur a 5% surcharge, which is waived for alternative billing or external links.

telegram · zaihuapd · Jun 25, 02:33

**Background**: Google Play's billing policy has been a contentious issue, with developers criticizing the 30% commission. This change follows regulatory pressure and pilot programs in select regions. The new 'Level Up' and 'Apps Experience' programs offer reduced rates for eligible game and app developers starting September.

<details><summary>References</summary>
<ul>
<li><a href="https://play.google.com/console/about/levelup/">Google Play Games Level Up | Google Play Console</a></li>
<li><a href="https://play.google.com/console/about/">Google Play for business | Launch & monetize your apps</a></li>

</ul>
</details>

**Tags**: `#Android`, `#Google Play`, `#app store billing`, `#developer policy`, `#platform competition`

---