---
layout: default
title: "AI行业热点: 2026-10-17 (ZH)"
date: 2026-10-17
lang: zh
briefing: ainews
---

> 从 79 条内容中筛选出 6 条重要资讯。

---

1. [Claude 破解 NIST ECDSA 曲线种子起源之谜](#item-1) ⭐️ 9.0/10
2. [特斯拉发布搭载冷气推进器与可选火箭发动机的 Roadster](#item-2) ⭐️ 8.0/10
3. [Llama.cpp 在越狱 PS5 上原生运行 GGUF 模型](#item-3) ⭐️ 8.0/10
4. [Jake Archibald 对比 JPEG XL 与 AVIF 的网页应用场景](#item-4) ⭐️ 8.0/10
5. [Nick Cammarata 声称智能体推翻多义性，提升可解释性](#item-5) ⭐️ 8.0/10
6. [Hugging Face 与 NVIDIA 发布 2.8 万亿 token 的印度语言预训练数据集](#item-6) ⭐️ 8.0/10

---

<a id="item-1"></a>
## [Claude 破解 NIST ECDSA 曲线种子起源之谜](https://www.anthropic.com/research/ecdsa-curve-origins) ⭐️ 9.0/10

Anthropic 的 Claude 发现 NIST 椭圆曲线 P-192、P-224、P-256、P-384 和 P-521 的种子是使用 C 库的 lrand48 随机数生成器并以 Unix 时间戳作为种子生成的，在不到半小时内破解了这个长达数十年的密码学谜团。 这一发现解决了长期以来关于 NIST 曲线是否包含隐藏后门的猜测，可能恢复人们对广泛使用的密码学标准的信任，同时也展示了 AI 在密码分析和科学发现方面的新兴能力。 这些种子并非如之前假设的那样来自任何哈希算法，而是来自以 Unix 时间戳为种子的 lrand48；然而，第五个二进制种子 B-163 仍无法解释，可能是发布过程中的笔误，而且该方法并不能排除故意选择时间戳以生成具有特定属性的曲线的可能性。

hackernews · ahlCVA · 10月16日 18:55 · [社区讨论](https://news.ycombinator.com/item?id=50122800)

**背景**: NIST 于 2000 年在 FIPS 186-2 中发布了 P-192、P-224、P-256、P-384 和 P-521 椭圆曲线，这些曲线按照 ANSI X9.62 标准通过用 SHA-1 哈希一个任意种子来派生参数。在此之前，没有人知道这些任意种子是如何选择的，引发了多年来关于 NSA 可能施加影响和后门的猜测。lrand48 是标准 C 库中的伪随机数生成器，使用 48 位整数运算的线性同余算法。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.anthropic.com/research/ecdsa-curve-origins">Claude reveals ECDSA curve origins \ Anthropic</a></li>
<li><a href="https://words.filippo.io/seeds-solved/">The NIST Elliptic Curves Seeds Bounty Has Been Claimed</a></li>
<li><a href="https://www.unite.ai/anthropic-says-claude-traced-nist-ecdsa-curve-seeds-to-a-1990s-rng/">Anthropic Says Claude Traced NIST ECDSA Curve Seeds to a 1990S RNG</a></li>

</ul>
</details>

**社区讨论**: 评论者对这一发现表示惊叹，有人开玩笑说负责的 NSA 员工，也有人指出生成方法并不能证明曲线不是故意选择的。一个值得注意的观点是，无法解释的 B-163 种子可能只是一个笔误，还有一位评论者分享了关于参与曲线生成的 Jerry Solinas 的个人轶事。

**标签**: `#cryptography`, `#ECDSA`, `#NIST curves`, `#AI for science`, `#random number generation`

---

<a id="item-2"></a>
## [特斯拉发布搭载冷气推进器与可选火箭发动机的 Roadster](https://www.tesla.com/roadster) ⭐️ 8.0/10

特斯拉发布了一款全新 Roadster，配备冷气推进器以及可选的 SpaceX 火箭发动机套件，演示视频显示该车能够短暂飞行，甚至吸附在天花板上。该车提供两种模式：一种使用冷气推进器以增强向前加速，另一种是视频中展示的仅限受邀用户使用的燃烧火箭发动机版本，据报道量产目标定在 2028 年。 这一发布将汽车工程推向了此前仅属于航天器和火箭直线加速赛车的领域，引发了关于此类推进系统在量产车中是否可行或安全的激烈争论。这也强化了特斯拉以极端工程展示作为营销手段的策略，可能影响竞争对手在性能宣传与造势上的定位。 冷气推进器使用加压惰性气体而非燃烧产生推力，因此结构简单可靠，但推力和效率远低于传统火箭发动机。仅限受邀用户使用的燃烧版本引发了明显的安全担忧，而且据报道特斯拉无法保证 Roadster 的预订最终能够交付。

hackernews · shekhar101 · 10月16日 01:32 · [社区讨论](https://news.ycombinator.com/item?id=50112657)

**背景**: 冷气推进器是一种通过喷射加压气体产生推力、不涉及燃烧的火箭发动机，因其结构简单可靠，数十年来一直被航天器用于姿态控制。相比之下，火箭车是由火箭发动机驱动的陆地车辆，历史上主要用于直线加速赛而非日常驾驶。埃隆·马斯克早在 2018 年就曾提到为下一代 Roadster 配备小型推进器的“SpaceX 套件”，因此这次发布是这一长期构想的最新进展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Cold_gas_thruster">Cold gas thruster - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Rocket_car">Rocket car - Wikipedia</a></li>
<li><a href="https://www.explainx.ai/blog/tesla-flying-roadster-cold-gas-thrusters-how-it-works-what-was-shown-2026">Tesla's Flying Roadster: What Was Shown, How Cold-Gas ...</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的评论者意见分歧：一些人称赞将风扇和火箭发动机装入高性能汽车的工程壮举，另一些人则斥之为永远不会量产的“迷因股”营销噱头。还有人提出了实际担忧，包括压缩气体储量有限、推进器带来的安全风险，以及特斯拉无法保证预订车辆交付等问题。

**标签**: `#Tesla`, `#electric vehicles`, `#rocket propulsion`, `#engineering`, `#marketing stunt`

---

<a id="item-3"></a>
## [Llama.cpp 在越狱 PS5 上原生运行 GGUF 模型](https://github.com/cobanov/PS5LM) ⭐️ 8.0/10

一个名为 PS5LM 的新 GitHub 项目展示了越狱后的 PlayStation 5 可以使用 llama.cpp 原生运行任何 GGUF 格式的大语言模型，从而直接在游戏机硬件上进行本地 LLM 推理。 这表明像游戏机这样封闭的消费级硬件可以被改造成通用 AI 机器，可能为爱好者和研究人员提供一种比专用 GPU 更便宜、更省电的本地模型运行方案。 该项目依赖 PS5 的越狱来获得原生执行权限，社区报告称它可以运行 Qwen 3.8 27B 等模型（2 比特量化），虽然精度有所下降，但对于长时间、低强度的任务仍然可行。

hackernews · Anon84 · 10月16日 18:32 · [社区讨论](https://news.ycombinator.com/item?id=50122431)

**背景**: llama.cpp 是一个用于本地运行大语言模型的开源 C/C++ 库，已成为 Ollama 和 LM Studio 等本地推理工具的事实标准。GGUF 是一种为量化设计的单文件模型格式，通过降低精度来减少内存占用并加速推理。PlayStation 5 是一台封闭的游戏机，因此在其上运行通用软件需要利用软件或硬件漏洞进行越狱。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Llama.cpp">Llama.cpp</a></li>
<li><a href="https://en.wikipedia.org/wiki/GGUF">GGUF - Wikipedia</a></li>
<li><a href="https://grokipedia.com/page/PlayStation_5_jailbreak">PlayStation 5 jailbreak</a></li>

</ul>
</details>

**社区讨论**: 评论者对于将 PS5 改用于长时间运行的 LLM 任务充满热情，有人指出它每天仅需约 70 美分电费就能处理服务器监控或安全录像分析。还有人认为类似方法可能适用于更便宜的 BC250 矿卡，但也有人警告索尼可能会下架该 GitHub 页面，建议使用自定义域名托管。

**标签**: `#llama.cpp`, `#PS5`, `#jailbreak`, `#GGUF`, `#local-llm`

---

<a id="item-4"></a>
## [Jake Archibald 对比 JPEG XL 与 AVIF 的网页应用场景](https://jakearchibald.com/2026/jpeg-xl-vs-avif/) ⭐️ 8.0/10

网页性能专家 Jake Archibald 在其博客上发布了一篇针对网页应用场景的 JPEG XL 与 AVIF 详细技术对比文章，并在 Hacker News 上引发了 190 分、142 条评论的热烈讨论。该文章从编码性能、实用参数设置以及编解码器成熟度等方面对这两种现代图像格式进行了分析。 在 JPEG XL 与 AVIF 之间做选择会直接影响网站的页面加载时间、带宽成本和图像质量，而这一对比出现在两种格式的浏览器支持和工具链仍在演进之际。讨论表明目前尚无明确的赢家，这对正在决定生产环境采用何种格式的开发者来说意义重大。 评论者指出，libjxl 的最高压缩档位速度极慢，需要 9 到 46 秒（是默认设置的 50 到 180 倍），而照片文件仅缩小 2% 到 7%，截图和插画约缩小 25%，而 jixel 工具在几秒内即可达到类似效果。讨论中还分享了实用的 AVIF 编码方案，包括一条使用 yuva444p 和 alphaextract 的 ffmpeg 命令，以保留类似 PNG 的透明度。

hackernews · farlight · 10月16日 16:12 · [社区讨论](https://news.ycombinator.com/item?id=50120224)

**背景**: JPEG XL 是一种新一代图像格式，旨在以更好的压缩率和渐进式解码能力超越 PNG、JPEG 2000、GIF 和 WebP；而 AVIF 是一种开放、免版税的格式，源自 AV1 视频编解码器，并存储在 HEIF 容器中。两者都致力于在网页上取代 JPEG 和 PNG 等传统格式，但在编码速度、工具链成熟度以及透明度、HDR 等特性的处理方式上存在差异。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://jakearchibald.com/2026/jpeg-xl-vs-avif/">JPEG XL vs AVIF for web use-cases - JakeArchibald.com</a></li>
<li><a href="https://en.wikipedia.org/wiki/AVIF">AVIF - Wikipedia</a></li>
<li><a href="https://jpegxl.info/">JPEG XL : Superior Image Compression</a></li>

</ul>
</details>

**社区讨论**: Hacker News 上的讨论总体上对宣布赢家持谨慎态度：一位评论者将当前局面比作 MP3 时代与 LAME 的发展历程，认为编解码器需要多年才能成熟，而 WebP 早年的过度宣传就是前车之鉴。也有人为 AVIF 在生产环境中的使用辩护并分享了优化后的 ffmpeg 设置，还有一位评论者批评 AVIF 在一张 F1 赛车图片中抹去了高光细节，称这正证明了该格式的缺陷。

**标签**: `#image-compression`, `#jpeg-xl`, `#avif`, `#web-performance`, `#codecs`

---

<a id="item-5"></a>
## [Nick Cammarata 声称智能体推翻多义性，提升可解释性](https://www.latent.space/p/ainews-agents-disprove-polysemanticity) ⭐️ 8.0/10

Goodfire 研究员、前 OpenAI 研究员 Nick Cammarata 声称智能体推翻了多义性，并大幅提升了可解释性和对齐。他指出，在 Qwen3-32B 等模型中，近 90% 的神经元具有单一明确功能，而 2023 年这一比例仅约 2%。 这挑战了机制可解释性中的基础概念——多义性，可能简化 AI 安全和对齐工作。如果属实，将使神经网络更透明、更可控，影响研究人员理解和对齐大语言模型的方式。 该主张基于对 Qwen3-32B 等模型的观察，其中神经元单义性显著增加。然而，内容简短且缺乏详细讨论，因此需要独立验证。

rss · Latent Space · 10月16日 04:16

**背景**: 多义性指神经网络中单个神经元代表多个不相关的特征，这增加了可解释性的难度。机制可解释性旨在逆向工程神经网络以理解其内部运作，被认为对 AI 安全和对齐至关重要。Nick Cammarata 因在 OpenAI 和 Goodfire 期间对叠加和可解释性的研究而闻名。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://officechai.com/ai/ai-researcher-nick-cammarata-who-helped-discover-superposition-now-says-the-theory-was-wrong-and-thats-great-news-for-understanding-ai/">AI Researcher Nick Cammarata Who Helped Discover ...</a></li>
<li><a href="https://cryptobriefing.com/nick-cammarata-neural-networks-interpretable/">Former OpenAI researcher Nick Cammarata says most AI neurons ...</a></li>
<li><a href="https://arxiv.org/abs/2210.01892">[2210.01892] Polysemanticity and Capacity in Neural Networks</a></li>

</ul>
</details>

**标签**: `#AI interpretability`, `#polysemanticity`, `#alignment`, `#AI safety`, `#research breakthrough`

---

<a id="item-6"></a>
## [Hugging Face 与 NVIDIA 发布 2.8 万亿 token 的印度语言预训练数据集](https://huggingface.co/blog/nvidia/scaling-indic-pretraining) ⭐️ 8.0/10

Hugging Face 与 NVIDIA 发布了一个包含 2.8 万亿 token 的印度语言预训练数据集，以及一套开放的数据生成流水线，相关细节在一篇新的博客文章中公布。此次发布同时提供了大规模语料库和可复现的工具链，用于构建面向印度语言的多语言语言模型。 印度语言在 LLM 预训练数据中长期代表性不足，此次发布以此前该地区难以获得的语料规模直接填补了这一空白。开放流水线还降低了研究人员和开发者复现、扩展或将方法迁移到其他低资源语言的门槛。 该数据集包含 2.8 万亿 token，并配有开放的数据生成流水线，这意味着数据筛选和处理步骤是公开可复用的，而非专有保留。这项工作顺应了利用合成数据和机器翻译数据来补充稀缺母语语料的更广泛趋势。

rss · Hugging Face Blog · 10月16日 01:44

**背景**: 预训练是语言模型在针对特定任务微调之前，从海量文本中学习通用语言模式的阶段。对于大多数非英语语言而言，高质量的预训练语料远少于英语，导致模型表现不佳；南亚地区超过十亿人使用的印度语言就是一个典型例子。AI4Bharat 的 IndicLLMSuite 等项目开创了开放的印度语言数据集，而此次新发布将这一努力大幅扩展。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/blog/nvidia/scaling-indic-pretraining">Scaling Indic Pretraining: 2.8 Trillion Tokens and an Open ...</a></li>
<li><a href="https://github.com/AI4Bharat/IndicLLMSuite">GitHub - AI4Bharat/IndicLLMSuite: A blueprint for creating ...</a></li>
<li><a href="https://arxiv.org/abs/2502.13252">[2502.13252] Multilingual Language Model Pretraining using ... Multilingual Language Model Pretraining using Machine ... How Can Synthetic Data Improve Multilingual Language Model ... A Primer on Pretrained Multilingual Language Models Code-switching finetuning: Bridging multilingual pretrained ... Pre-Trained Language Models and Their Applications</a></li>

</ul>
</details>

**标签**: `#multilingual`, `#pretraining`, `#dataset`, `#NLP`, `#Indic languages`

---