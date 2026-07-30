---
layout: default
title: "AI行业热点: 2026-07-30 (ZH)"
date: 2026-07-30
lang: zh
briefing: ainews
---

> 从 162 条内容中筛选出 13 条重要资讯。

---

1. [GitHub 推出堆叠拉取请求公开预览](#item-1) ⭐️ 9.0/10
2. [OpenAI 将 GPT-5.6 Luna 价格降低 80%](#item-2) ⭐️ 9.0/10
3. [Kimi K3：采用新型注意力和 MoE 的开源前沿模型](#item-3) ⭐️ 9.0/10
4. [Anthropic 的 AI 发现 NIST 后量子候选算法 HAWK 严重弱点](#item-4) ⭐️ 9.0/10
5. [施奈尔：写作作业是健身任务，而非工作任务](#item-5) ⭐️ 8.0/10
6. [本体论回归：AI 代理重振语义网](#item-6) ⭐️ 8.0/10
7. [闲置 GPU：新型停飞飞机](#item-7) ⭐️ 8.0/10
8. [DeepSeek 在蒙古建设 10 亿美元 1 吉瓦 AI 数据中心](#item-8) ⭐️ 7.0/10
9. [AI 公司转向人类书籍，互联网数据已不够用](#item-9) ⭐️ 7.0/10
10. [轻量化异构双臂机器人结合 VLA/世界模型用于家庭服务](#item-10) ⭐️ 7.0/10
11. [中国科技巨头争夺企业 AI Agent 主导权](#item-11) ⭐️ 7.0/10
12. [扎克伯格押注个人 AI Agent，为数十亿 Meta 用户开启 Agent 时代](#item-12) ⭐️ 7.0/10
13. [腾讯开源 AngelSpec 框架提升大模型推理效率](#item-13) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [GitHub 推出堆叠拉取请求公开预览](https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/) ⭐️ 9.0/10

GitHub 已推出堆叠拉取请求的公开预览，允许开发者直接在平台上创建和管理作为堆栈的依赖 PR。该功能将在未来几天内向所有仓库推出，并逐步支持合并队列。 这是 GitHub 多年来最大的工作流程变化之一，使开发者能够将大型变更拆分为小型、可审查的 PR，从而更容易审查和合并。它有可能显著提高代码审查质量和开发者生产力，特别是对于使用堆叠差异的团队。 该功能包括新的 gh stack CLI 扩展和用于管理堆栈的 UI 支持。然而，一些用户报告了合并整个堆栈的问题，特别是在使用压缩合并并要求重新批准时。

hackernews · tomzorz · 7月30日 16:26 · [社区讨论](https://news.ycombinator.com/item?id=49112232)

**背景**: 堆叠拉取请求（或堆叠差异）是一种工作流程，其中一系列小型、依赖的 PR 相互叠加构建，允许每个 PR 独立审查。这种方法在大型代码库中很受欢迎，以保持审查的可管理性，但 GitHub 之前缺乏原生支持，迫使团队使用第三方工具如 Graphite 或 git spr。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.blog/changelog/2026-07-30-stacked-pull-requests-are-now-in-public-preview/">Stacked pull requests are now in public preview - GitHub ...</a></li>
<li><a href="https://github.github.com/gh-stack/">GitHub Stacked PRs | GitHub Stacked PRs - github.github.com</a></li>
<li><a href="https://stackoverflow.com/questions/26619478/are-dependent-pull-requests-in-github-possible">git - Are dependent pull requests in GitHub possible? - Stack ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：知名开发者 steveklabnik 称赞这是一项重大改进，而一些用户如 matharmin 报告了合并整个堆栈的关键错误。一位 GitHub 团队成员确认了反馈并承诺更多更新。

**标签**: `#GitHub`, `#stacked PRs`, `#developer workflow`, `#version control`, `#open source`

---

<a id="item-2"></a>
## [OpenAI 将 GPT-5.6 Luna 价格降低 80%](https://openai.com/index/advancing-the-price-performance-frontier-with-gpt-5-6/) ⭐️ 9.0/10

OpenAI 宣布推出其最快、最实惠的模型 GPT-5.6 Luna，价格降低 80%，使其比以前便宜五倍。 这一大幅降价挑战了 AI 模型定价趋于平稳的观念，使得先进 LLM 的部署更加广泛且经济高效，可能重塑竞争格局。 GPT-5.6 Luna 每次请求可接受多达 100 万个 token 的上下文，并通过 API、ChatGPT 和 Codex 提供。80% 的降价得益于内核优化，使服务成本降低 20%，token 生成效率提升超过 15%。

hackernews · tedsanders · 7月30日 17:15 · [社区讨论](https://news.ycombinator.com/item?id=49112867)

**背景**: 像 GPT-5.6 这样的大型语言模型通常按 token 定价，推理效率（模型生成响应的速度和成本）是关键竞争因素。OpenAI 的 GPT-5.6 系列包括三个层级：Sol（能力最强）、Terra（均衡）和 Luna（最快/最便宜）。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://free.ai/models/openai-gpt-5-6-luna/">OpenAI: GPT - 5 . 6 Luna - AI Chat | Free.ai</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT - 5 . 6 Sol vs Terra vs Luna : Which Tier Should You Actually Use?</a></li>
<li><a href="https://epoch.ai/models/gpt-5-6-luna">Explore benchmark performance data for the GPT - 5 . 6 Luna model.</a></li>

</ul>
</details>

**社区讨论**: 社区表达了惊讶和兴奋，许多人注意到价格从上涨转为下跌。一些人强调了决定何时使用更便宜模型的挑战，而另一些人则指出了大规模节省成本的潜力，将其比作从拨号上网到宽带的转变。

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI pricing`, `#inference efficiency`, `#LLM`

---

<a id="item-3"></a>
## [Kimi K3：采用新型注意力和 MoE 的开源前沿模型](https://www.reddit.com/r/MachineLearning/comments/1vaysjf/how_kimi_k3_engineered_its_way_to_the_frontier_r/) ⭐️ 9.0/10

Moonshot AI 发布了 Kimi K3，这是一个 2.8T 参数的开源权重模型，在 Artificial Analysis 的 580 个模型中排名第四，仅次于 Claude Opus 5、Fable 5 和 GPT-5.6 Sol。该模型引入了 Kimi Delta Attention、用于 MoE 的 Quantile Balancing 以及用于 RL 训练的 AgentENV。 Kimi K3 证明了开源权重模型可以达到前沿性能，挑战了专有模型的主导地位。其工程创新——尤其是 75% 的 KV 缓存缩减和高效的专家平衡——可能影响未来的 LLM 架构，并让顶级 AI 更加普及。 Kimi Delta Attention 在 93 层中的 69 层用每个注意力头一个 128x128 矩阵替换了 KV 缓存，将 1M token 上下文的显存从 104.6 GiB 降至 27.2 GiB。Quantile Balancing 直接从路由器得分边际计算偏置，以保持每层 896 个专家负载均衡，避免了 DeepSeek-V3 固定步长偏置推动的不稳定性。

reddit · r/MachineLearning · /u/noninertialframe96 · 7月30日 16:37

**背景**: 大型语言模型（LLM）通常使用注意力机制，需要为每个 token 缓存键值对（KV），这在长上下文场景下会消耗大量显存。混合专家模型（MoE）每个 token 只激活部分参数，但专家负载不均衡会损害训练效率。用于 LLM 的强化学习（RL）通常需要运行大量沙箱环境来生成训练轨迹。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://arxiv.org/abs/2510.26692">[2510.26692] Kimi Linear: An Expressive, Efficient Attention ... GitHub - MoonshotAI/Kimi-Linear KDA (Kimi Delta Attention) | fla-org/flash-linear-attention ... GitHub - hwilner/kimi-delta-attention: Educational ... Linear Attention: Kimi Delta Attention | Jianyu Huang Kimi K3 Tech Blog: Open Frontier Intelligence Kimi Linear: An Expressive, Efficient Attention Architecture</a></li>
<li><a href="https://github.com/MoonshotAI/Kimi-Linear">GitHub - MoonshotAI/Kimi-Linear</a></li>
<li><a href="https://github.com/firecracker-microvm/firecracker">GitHub - firecracker-microvm/firecracker: Secure and fast ... GitHub Pages - Firecracker Firecracker Sandbox | AerolVM - microvm.aerol.ai Firecracker MicroVM Sandboxing Features Explained Understanding Sandboxes</a></li>

</ul>
</details>

**社区讨论**: Reddit 社区称赞了其技术深度和开源发布，许多人强调 KV 缓存缩减和专家平衡是重要贡献。一些用户质疑第四名排名的实际影响，指出前三名是专有模型且可能能力更强。其他人则对用于 RL 扩展的 AgentENV 沙箱方法表示兴趣。

**标签**: `#LLM`, `#open-weight`, `#attention`, `#MoE`, `#RL`

---

<a id="item-4"></a>
## [Anthropic 的 AI 发现 NIST 后量子候选算法 HAWK 严重弱点](https://startupfortune.com/claude-mythos-broke-hawk-and-the-nist-post-quantum-timeline-may-not-survive-it/) ⭐️ 9.0/10

Anthropic 宣布，其 Claude Mythos Preview 模型在大约 60 小时内发现了 NIST 后量子候选算法 HAWK 的严重弱点，将其有效密钥强度从 2^64 降至 2^38，API 费用约为 10 万美元。 这一突破表明，AI 现在在发现漏洞方面可以超越人类密码分析员，可能加速后量子密码标准的评估，并重塑 AI 在安全研究中的角色。 该攻击不在多项式时间内运行，因此更大的密钥仍然安全，HAWK 也尚未被公开撤回。研究还包括对七轮 AES-128 的改进攻击，但完整的 AES-128 为 10 轮，不受影响。

telegram · zaihuapd · 7月30日 05:47

**背景**: HAWK 是一种基于模块格同构问题（module-LIP）的后量子数字签名方案，是 NIST 额外数字签名流程第三轮中唯一的基于格的候选算法。NIST 正在标准化后量子密码学，以防范未来可能破解当前公钥系统的量子计算机。白宫已要求联邦机构在 2030 年前迁移至抗量子密钥体系，并在 2031 年前完成数字签名迁移。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://blog.cryptographyengineering.com/2026/07/29/some-notes-about-anthropics-new-results/">Some thoughts about Anthropic’s new cryptanalysis results – A Few Thoughts on Cryptographic Engineering</a></li>
<li><a href="https://www.techtimes.com/articles/321876/20260728/ai-cracks-post-quantum-cipher-60-hours-after-two-years-human-review-failed.htm">AI Cracks Post-Quantum Cipher in 60 Hours After Two Years of Human Review Failed</a></li>
<li><a href="https://eprint.iacr.org/2026/1078">Post-Quantum HAWK Signature Acceleration with RISC-V-Based Hardware-Software Co-Design</a></li>

</ul>
</details>

**标签**: `#AI`, `#cryptography`, `#post-quantum`, `#security`, `#Anthropic`

---

<a id="item-5"></a>
## [施奈尔：写作作业是健身任务，而非工作任务](https://simonwillison.net/2026/Jul/30/bruce-schneier/#atom-everything) ⭐️ 8.0/10

布鲁斯·施奈尔在 2026 年 7 月的一篇博文中指出，写作作业是旨在培养批判性思维的“健身任务”，而非可以外包给 AI 的“工作任务”。 这一区分提供了一个清晰的框架，帮助教育者和学生判断何时使用 AI 是合适的，回应了人们对 AI 削弱教育中批判性思维能力的日益担忧。 施奈尔强调，写作的过程——思考、列提纲、起草、编辑和修改——是防止批判性思维技能退化的必要心智锻炼，而雇主们已经注意到了这种退化。

rss · Simon Willison · 7月30日 18:25

**背景**: 随着像 ChatGPT 这样的生成式 AI 工具能够生成学生可能作为自己作业提交的论文和备忘录，关于 AI 在教育中作用的争论愈演愈烈。施奈尔的“健身任务”比喻将作业重新定义为心智成长的练习，而非供外部消费的产出，类似于健身房锻炼是为了增强力量而非生产商品。

**标签**: `#AI`, `#education`, `#critical thinking`, `#writing`

---

<a id="item-6"></a>
## [本体论回归：AI 代理重振语义网](https://www.latent.space/p/ontologies-agentic-systems) ⭐️ 8.0/10

AI 工程师正在重新发现本体论，为概率性 AI 代理提供确定性护栏，将符号 AI 原理与现代代理系统相结合。 这一趋势弥合了符号 AI 与大语言模型之间的差距，提高了代理的可靠性和可解释性，对于在高风险领域部署 AI 至关重要。 本体论定义了领域内的概念、属性和关系，实现了结构化知识表示，能够将 LLM 的输出约束在预定义边界内。

rss · Latent Space · 7月30日 11:17

**背景**: 语义网旨在通过本体论和链接数据使网络数据机器可读，但采用有限。现在，随着概率性 AI 代理的兴起，本体论被重新用于提供确定性护栏，结合了符号 AI 和概率 AI 的优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.geeksforgeeks.org/machine-learning/introduction-to-ontologies/">Introduction to Ontologies - GeeksforGeeks</a></li>
<li><a href="https://en.wikipedia.org/wiki/Semantic_Web">Semantic Web - Wikipedia</a></li>
<li><a href="https://en.wikipedia.org/wiki/Symbolic_artificial_intelligence">Symbolic artificial intelligence - Wikipedia</a></li>

</ul>
</details>

**标签**: `#ontologies`, `#AI agents`, `#semantic web`, `#symbolic AI`, `#LLMs`

---

<a id="item-7"></a>
## [闲置 GPU：新型停飞飞机](https://huggingface.co/blog/Dharma-AI/gpu-management) ⭐️ 8.0/10

一篇 Hugging Face 博客文章将闲置 GPU 比作停飞飞机，指出 AI/ML 工作负载中许多 GPU 闲置时间高达 68%，并提供了提高利用率的策略。 提高 GPU 利用率可直接降低成本并加速 AI/ML 工作流，因此高效的 GPU 管理成为扩展 AI 运营的组织关注的关键问题。 文章引用了 GPU 闲置时间达 68%的数据，并讨论了动态 GPU 分配（如 Hugging Face ZeroGPU）和合理作业调度等减少浪费的技术。

rss · Hugging Face Blog · 7月30日 15:09

**背景**: GPU 是训练和运行大型 AI 模型所必需的昂贵且耗电的资源。在许多数据中心，由于调度效率低、过度配置或工作负载不匹配，GPU 经常未被充分利用，导致巨大的成本和能源浪费。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://levitation.in/posts/gpus-68-percent-idle-costs">GPU Utilization : Fix 68% Idle Time, Cut Costs | Levitation</a></li>
<li><a href="https://huggingface.co/docs/hub/spaces-zerogpu">Spaces ZeroGPU: Dynamic GPU Allocation for Spaces · Hugging Face</a></li>

</ul>
</details>

**标签**: `#GPU management`, `#AI/ML infrastructure`, `#cost optimization`, `#Hugging Face`

---

<a id="item-8"></a>
## [DeepSeek 在蒙古建设 10 亿美元 1 吉瓦 AI 数据中心](https://www.infomoney.com.br/business/deepseek-startup-chinesa-de-ia-monta-datacenter-bilionario-de-1-gw-na-mongolia/) ⭐️ 7.0/10

中国 AI 初创公司 DeepSeek 正在蒙古建设一个耗资数十亿美元、功率达 1 吉瓦（GW）的数据中心，这标志着全球最大的 AI 基础设施项目之一。 这一巨额投资表明 DeepSeek 有意扩大 AI 训练和推理能力，可能加剧与 OpenAI、谷歌等 AI 领导者的竞争。同时，它也凸显了对高能耗 AI 基础设施日益增长的需求。 该 1 吉瓦数据中心的规模与 Anthropic/亚马逊和 xAI 等计划中的最大 AI 数据中心相当。建设 1 吉瓦设施通常耗资数百亿美元，其中很大一部分用于 IT 硬件。

gdelt · infomoney.com.br · 7月30日 23:00

**背景**: DeepSeek 是一家成立于 2023 年的中国 AI 公司，由对冲基金 High-Flyer 支持。它开发大型语言模型，并因其高效模型迅速获得关注。1 吉瓦或更大规模的数据中心正成为训练前沿 AI 模型的必要条件，但需要巨大的资本和能源资源。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/DeepSeek">DeepSeek - Wikipedia</a></li>
<li><a href="https://orennia.com/insights/what-it-actually-costs-to-build-a-1-gw-data-center">What It Costs to Build a 1 GW Data Center | Orennia</a></li>

</ul>
</details>

**标签**: `#AI`, `#datacenter`, `#infrastructure`, `#DeepSeek`, `#China`

---

<a id="item-9"></a>
## [AI 公司转向人类书籍，互联网数据已不够用](https://expansion.mx/tecnologia/2026/07/30/empresas-de-ia-recurren-libros-humanos) ⭐️ 7.0/10

AI 公司越来越多地购买并使用 2022 年之前印刷的实体书籍作为训练数据，因为互联网内容受到 AI 生成材料的污染，且不足以支持高质量模型训练。 这一转变凸显了 AI 面临的数据稀缺危机，依赖互联网数据可能因合成内容导致“模型崩溃”，并凸显了原创人类创作材料的价值。 据报道，公司在数字化后销毁数百万本书籍以避免版权问题，有些公司外包给中间商秘密购书。Books3 数据集包含近 20 万本书，未经作者同意被使用。

gdelt · expansion.mx · 7月30日 23:00

**背景**: AI 模型需要大量高质量文本数据来学习语言模式和知识。公共互联网曾是主要来源，但现在包含越来越多的 AI 生成内容，用作训练数据时会降低模型性能——这种现象称为“模型崩溃”。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://mashable.com/life/ai-companies-destroy-books-training-data">AI companies are buying and destroying old books for training data | Mashable</a></li>
<li><a href="https://www.tomshardware.com/tech-industry/artificial-intelligence/ai-companies-are-reportedly-shredding-millions-of-books-to-train-models-tech-giants-outsource-to-middlemen-to-secretly-buy-up-books-for-training-material">AI companies are reportedly shredding millions of books after using them to train AI models — tech giants outsource to middlemen to secretly buy up books for training material | Tom's Hardware</a></li>
<li><a href="https://www.cnn.com/2023/10/08/style/ai-books3-authors-nora-roberts-cec">These books are being used to train AI. No one told the authors | CNN</a></li>

</ul>
</details>

**标签**: `#AI`, `#training data`, `#machine learning`, `#data sourcing`

---

<a id="item-10"></a>
## [轻量化异构双臂机器人结合 VLA/世界模型用于家庭服务](https://news.google.com/rss/articles/CBMiXkFVX3lxTFBPVnpIZVp6QlNENzRzYldZTTBvbjJESVAyemxaU3lGU0NZYU9tQk5VY044SHpfNHFWZFdiOW14ZWFiTm11R1ZmaXhQTnJwSERjSm5VeTNwbWJCdk81OVE?oc=5) ⭐️ 7.0/10

在 AICon 深圳的一场演讲中，展示了将轻量化异构双臂机器人与视觉-语言-动作（VLA）模型及世界模型相结合，用于家庭服务具身 AI 的实际部署。 这项工作展示了在真实家庭环境中部署先进具身 AI 的可行路径，可能加速服务机器人在家庭中的普及，并缩小研究与实际应用之间的差距。 该机器人采用异构双臂（每只手臂设计不同）以平衡负载能力和灵活性，VLA 模型实现从视觉和语言输入直接生成动作，世界模型则提供预测规划能力。

google_news · Infoq.cn · 7月30日 02:00

**背景**: 视觉-语言-动作（VLA）模型是一种 AI 模型，它以图像和文本指令为输入，直接输出机器人动作，通常通过微调视觉-语言模型构建。世界模型是物理环境的预测模型，使机器人能够规划和推理未来状态。异构双臂机器人使用不同机械设计的手臂，以结合高负载和高灵活性等优势。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Vision–language–action_model">Vision–language–action model - Wikipedia</a></li>
<li><a href="https://github.com/LMD0311/Awesome-World-Model">GitHub - LMD0311/Awesome- World - Model : Collect some World ...</a></li>
<li><a href="https://www.emerald.com/ir/article/51/2/301/1226559/Sky-Worker-a-heterogeneous-dual-arm-robot-with">Sky-Worker: a heterogeneous dual-arm robot with dynamic ...</a></li>

</ul>
</details>

**标签**: `#embodied AI`, `#robotics`, `#VLA`, `#world models`, `#home service`

---

<a id="item-11"></a>
## [中国科技巨头争夺企业 AI Agent 主导权](https://news.google.com/rss/articles/CBMiU0FVX3lxTFBSNzBNTVRYdkRDQzBHNUJCeW9mZGZMaTlKUm5BNlpqb3NsQmtMYUY0UWlOaDUwVmZURTRvSHlHMjJwQzhwdUd0ejIzM2tocldQZXJv?oc=5) ⭐️ 7.0/10

腾讯、阿里巴巴和字节跳动正加剧竞争，力图成为企业 AI Agent 的主要平台，各自依托微信、钉钉和飞书等现有生态系统。 这场竞争将决定哪家公司掌控下一代企业生产力工具，可能重塑到 2030 年达 470 亿美元的 AI Agent 市场，并影响企业自动化任务的方式。 腾讯的 WorkBuddy 与微信集成，阿里巴巴的 QoderWork 整合其 AI 产品，字节跳动的豆包利用其内容生态。Gartner 预测到 2026 年 40%的企业应用将具备 AI Agent。

google_news · 华尔街见闻 · 7月30日 04:05

**背景**: AI Agent 是能自主代表用户执行任务（如安排会议或处理数据）的软件程序。中国科技巨头正从模型竞争转向专注于深度嵌入企业工作流的 Agent 平台，类似于微软和 Salesforce 等美国公司集成 AI 助手的方式。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.ainchina.com/blog/china-ai-agent-wars-tencent-alibaba-bytedance-2026/">The Agent Wars: How Tencent, Alibaba, and ByteDance Are ...</a></li>
<li><a href="https://beam.ai/agentic-insights/ai-agents-in-2026-how-the-us-and-china-are-building-two-very-different-futures">AI Agents in 2026: US vs China's Two Different Futures</a></li>

</ul>
</details>

**标签**: `#AI Agents`, `#Enterprise AI`, `#China Tech`, `#Competition`

---

<a id="item-12"></a>
## [扎克伯格押注个人 AI Agent，为数十亿 Meta 用户开启 Agent 时代](https://news.google.com/rss/articles/CBMiVkFVX3lxTFBVUWtNM3R5MXhIa25HMEdBQTUteEtLOTRBbDZUMW94S1laRURyRXRCQVg4UktJdFVKXzRhLWhwY05DZEdzMjMybDhiQmp5cElVaXJyUDFn?oc=5) ⭐️ 7.0/10

Meta CEO 马克·扎克伯格宣布计划将个人 AI Agent 带给 Meta 平台上数十亿用户，旨在将公司带入 Agent 时代。 此举可能改变数十亿用户与 AI 的交互方式，使自主 Agent 成为日常任务的主流工具，并可能重塑数字广告和商业格局。 据报道，Meta 以约 20 亿美元收购了 AI 初创公司 Manus 以加速其 Agent 战略，其 REA Agent 已将广告模型准确率提升了一倍。

google_news · SOHU · 7月30日 04:08

**背景**: AI Agent 是一种智能系统，能够感知环境并自主采取行动以实现目标，通常通过学习改进。Meta 的策略是将此类 Agent 集成到其平台中，充当商业中介，从而捕获交易费用或广告信号。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Personal_agent">Personal agent</a></li>
<li><a href="https://fourweekmba.com/ai-meta-zuckerberg-ai-agent-business-model/">Mark Zuckerberg's AI Agent Bet Is Breaking Meta in... - FourWeekMBA</a></li>
<li><a href="https://www.linkedin.com/posts/emilio-njagi_meta-buys-manus-to-jump-start-its-ai-agent-activity-7412110782240382976-Nyj9">Meta Acquires Manus for AI Agent Strategy Boost | LinkedIn</a></li>

</ul>
</details>

**标签**: `#AI`, `#Meta`, `#AI Agents`, `#Tech Industry`

---

<a id="item-13"></a>
## [腾讯开源 AngelSpec 框架提升大模型推理效率](https://news.google.com/rss/articles/CBMiTkFVX3lxTE9mMllYdU4yVmhtTGN4blhGLU84dVllZC1CR0E5MEoxdjlvTDhzekt6SGZuWEIzTzR3Tjh3clJiV3hEV28xMnB5VjZueDNXZw?oc=5) ⭐️ 7.0/10

腾讯开源了 AngelSpec 框架，这是一个基于 PyTorch 的原生框架，用于训练推测解码的草稿模型，旨在提升大语言模型在实际场景中的推理效率。 这解决了大模型部署中的关键瓶颈：推理延迟和成本。通过开源 AngelSpec，腾讯使更广泛的 AI 社区能够利用先进的推测解码技术，有望加速大模型在生产环境中的应用。 AngelSpec 支持自回归 MTP（多令牌预测）草稿和块并行 DFlash 系列方法。它由腾讯混元 AI 基础设施团队开发，并在 GitHub 上开源。

google_news · AIBase · 7月30日 02:39

**背景**: 大语言模型（LLM）逐个生成令牌，速度慢且成本高。推测解码通过使用小型草稿模型提出多个令牌，再由大模型验证，从而加速生成。AngelSpec 为这类草稿模型提供了统一的训练框架。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://github.com/Tencent/AngelSpec">Tencent/ AngelSpec : A unified, torch-native training framework for...</a></li>
<li><a href="https://angelspec.readthedocs.io/">AngelSpec Documentation — AngelSpec</a></li>
<li><a href="https://arxiv.org/html/2607.25852v1">AngelSpec : Towards Real-World High Performance Inference with...</a></li>

</ul>
</details>

**标签**: `#LLM`, `#inference`, `#open-source`, `#AI infrastructure`, `#Tencent`

---