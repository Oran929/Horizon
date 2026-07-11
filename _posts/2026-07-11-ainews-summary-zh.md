---
layout: default
title: "AI行业热点: 2026-07-11 (ZH)"
date: 2026-07-11
lang: zh
briefing: ainews
---

> 从 61 条内容中筛选出 5 条重要资讯。

---

1. [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](#item-1) ⭐️ 9.0/10
2. [人形机器人远程完成全球首例活猪胆囊手术](#item-2) ⭐️ 9.0/10
3. [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三层级](#item-3) ⭐️ 9.0/10
4. [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](#item-4) ⭐️ 8.0/10
5. [高盛分析中国 AI 大模型竞争格局](#item-5) ⭐️ 7.0/10

---

<a id="item-1"></a>
## [vLLM v0.25.0：Model Runner V2 成为默认，PagedAttention 被移除](https://github.com/vllm-project/vllm/releases/tag/v0.25.0) ⭐️ 9.0/10

vLLM v0.25.0 将 Model Runner V2 设为所有稠密模型的默认执行路径，并移除了传统的 PagedAttention 实现。该版本还新增了对 LLaVA-OneVision-2 和 GLM-5 等新模型的支持，并引入了用于工具调用/推理解析的流式解析引擎。 此版本标志着 vLLM 的重大架构转变，通过移除遗留代码简化了推理流程并提升了性能。新的默认 Model Runner V2 和增强的推测解码能力将使依赖 vLLM 进行高效服务的大型语言模型开发者和部署者受益。 Model Runner V2 现在支持 EVS、实时嵌入、Mamba 混合模型的前缀缓存以及多模态前缀双向注意力。Transformers 建模后端已优化至与原生 vLLM 速度相当，并引入了针对异构词汇表的通用推测解码（TLI）。

github · khluu · 7月11日 20:06

**背景**: vLLM 是一个高性能的大型语言模型推理引擎，最初由加州大学伯克利分校开发。PagedAttention 是一项关键创新，通过为 KV 缓存使用分页机制，实现了高效的 LLM 服务内存管理。Model Runner V2 是一个重新设计的执行路径，提高了模块化和效率，逐步取代了原始的 V1 实现。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://docs.vllm.ai/en/latest/design/model_runner_v2/">Model Runner V2 Design Document - vLLM</a></li>
<li><a href="https://en.wikipedia.org/wiki/PagedAttention">PagedAttention - Wikipedia</a></li>
<li><a href="https://docs.vllm.ai/en/latest/design/paged_attention/">Paged Attention - vLLM</a></li>

</ul>
</details>

**标签**: `#vLLM`, `#LLM inference`, `#open source`, `#release`, `#AI infrastructure`

---

<a id="item-2"></a>
## [人形机器人远程完成全球首例活猪胆囊手术](https://arstechnica.com/ai/2026/07/humanoid-robots-controlled-by-surgeons-did-world-first-operation-on-live-pigs/) ⭐️ 9.0/10

外科医生远程操控宇树 G1 人形机器人，成功在活猪身上完成了全球首例微创胆囊切除手术，结果已发表在《自然》期刊。 这一突破表明，低成本通用人形机器人有望替代达芬奇等昂贵专用手术系统，从而在偏远地区、战场甚至太空等场景中扩大微创手术的可及性。 宇树 G1 基础款售价 13500 美元，配备灵巧手后约 67000 美元，远低于达芬奇系统 50 万美元以上的价格。该机器人高 1.5 米，重 27 公斤，拥有 23 至 43 个关节电机以实现灵活性。

telegram · zaihuapd · 7月11日 02:29

**背景**: 腹腔镜胆囊切除术是一种微创手术，通常使用达芬奇等专用机器人系统完成。这些系统价格昂贵且需要专用硬件。宇树 G1 是一款通用人形机器人，最初为研究和工业任务设计，本研究将其改造用于远程手术操作。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.unitree.com/g1/">Humanoid robot G 1 _ Humanoid Robot ... | Unitree Robotics</a></li>
<li><a href="https://qviro.com/product/unitree/unitree-g1">Unitree G 1 Reviews, Price, Use-cases, Compare Humanoid Robots</a></li>
<li><a href="https://robixone.com/robots/unitree-unitree-g1/">Unitree G 1 Review | RobixOne</a></li>

</ul>
</details>

**标签**: `#robotics`, `#surgery`, `#humanoid robot`, `#medical technology`, `#AI`

---

<a id="item-3"></a>
## [OpenAI 发布 GPT-5.6 系列：Sol、Terra、Luna 三层级](https://t.me/zaihuapd/42497) ⭐️ 9.0/10

OpenAI 正式发布 GPT-5.6 系列，包含三个层级：旗舰级 Sol、平衡型 Terra 和低成本高并发型 Luna。该系列引入了 max/ultra 推理模式、多智能体协作和程序化工具调用，在代码、知识工作、设计、科研和网络安全能力上均有显著提升。 此次发布标志着 OpenAI 模型策略的重大进展，通过分层定价和能力覆盖从高端研究到大众市场的多种应用场景。新的多智能体协作和程序化工具调用功能可能实现更自主、更高效的 AI 工作流，有望重塑开发者构建复杂 AI 系统的方式。 GPT-5.6 系列默认使用 Sol 以获得最强能力，Terra 平衡性能与成本，Luna 面向高吞吐、低成本场景。新的程序化工具调用允许模型通过代码编排工具，而非逐个 API 往返，从而降低延迟和 token 消耗。

telegram · zaihuapd · 7月11日 13:34

**背景**: OpenAI 的 GPT 系列从 GPT-3 发展到 GPT-4 再到现在的 GPT-5.6，每一代都在推理、创造力和任务完成能力上有所提升。多智能体协作是指多个 AI 智能体协同解决复杂问题，而程序化工具调用则允许智能体编写和执行代码以更高效地使用外部工具。这些进步旨在使 AI 更加自主，能够处理真实世界的工作流。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://codersera.com/blog/gpt-5-6-sol-terra-luna/">GPT-5.6 Sol, Terra & Luna Explained: Tiers, Pricing ...</a></li>
<li><a href="https://agentos.guide/gpt56-sol-terra-luna">The Three-Tier Engine™ — GPT-5.6 Sol vs Terra vs Luna, tested ...</a></li>
<li><a href="https://www.vellum.ai/blog/gpt-5-6-benchmarks-explained">GPT-5.6 Sol vs Terra vs Luna: Which Tier Should You Actually Use?</a></li>

</ul>
</details>

**标签**: `#OpenAI`, `#GPT-5.6`, `#AI`, `#language model`, `#machine learning`

---

<a id="item-4"></a>
## [ClickHouse 将 PgBouncer 吞吐量提升 4 倍](https://clickhouse.com/blog/pgbouncer-clickhouse-managed-postgres) ⭐️ 8.0/10

ClickHouse 发布了一篇博客文章，详细介绍了他们如何通过使用 SO_REUSEPORT 套接字选项并实现用于取消转发的对等机制，将 PgBouncer 的吞吐量提升了 4 倍。 这一优化使得 PgBouncer 能够处理每台机器上更多的连接，从而降低基础设施成本并提高基于 PostgreSQL 的服务的性能。它还展示了扩展数据库连接池的实用技术。 SO_REUSEPORT 允许多个 PgBouncer 进程绑定到同一端口，将传入连接均匀分布到这些进程。对等机制确保取消请求被转发到拥有该会话的正确进程。

hackernews · saisrirampur · 7月11日 15:28 · [社区讨论](https://news.ycombinator.com/item?id=48872874)

**背景**: PgBouncer 是 PostgreSQL 的轻量级连接池，用于管理数据库连接以减少开销。传统上，在同一台机器上运行多个 PgBouncer 进程需要不同的端口或复杂的负载均衡。SO_REUSEPORT 是一个 Linux 套接字选项，允许多个套接字监听同一端口，由内核分发连接。PgBouncer 中的对等机制允许进程共享取消令牌，因此到达错误进程的取消请求可以被转发到正确的进程。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://lwn.net/Articles/542629/">The SO_REUSEPORT socket option [LWN.net]</a></li>
<li><a href="https://www.pgbouncer.org/config.html">PgBouncer config</a></li>
<li><a href="https://github.com/pgbouncer/pgbouncer/releases">Releases · pgbouncer/pgbouncer</a></li>

</ul>
</details>

**社区讨论**: 评论者推荐了 Odyssey 和 pgdog 等替代工具，并询问了对等设置的简便性。一位用户提到他们在 Kubernetes 上运行 PgBouncer，使得多进程扩展变得简单。讨论反映了对 PgBouncer 实际扩展解决方案的兴趣。

**标签**: `#PostgreSQL`, `#PgBouncer`, `#performance`, `#database`, `#infrastructure`

---

<a id="item-5"></a>
## [高盛分析中国 AI 大模型竞争格局](https://news.google.com/rss/articles/CBMif0FVX3lxTE5BYU1Yc1JJeldCc3ZIRDhrQ2ZOcmE5WUtNSHBDNUQwNnAyRmxqbmJFZEh0QkE1M2R3Q3ZraW1Zb3lHTzZIZDh2aVEzVFFDV01GWmhEXzZBbWl4bG80cnFZUmlyUXdyVDFvRl9xUTV2TjlfZXNpMThPQ1BzRHB4ODg?oc=5) ⭐️ 7.0/10

高盛发布了一份报告，详细分析了中国 AI 大模型行业的竞争格局，并指出了潜在的长期赢家。 该报告为投资者和行业观察者提供了关于哪些中国 AI 公司可能主导快速发展的市场的宝贵见解，影响投资决策和战略规划。 该报告可能评估了技术能力、数据资源、人才和商业化潜力等因素，但摘要中未详细说明具体发现。

google_news · PANews · 7月11日 08:35

**背景**: 中国的 AI 大模型领域有多家参与者，如百度、阿里巴巴、腾讯和初创公司，在政府支持和海量数据的推动下竞争。高盛的分析有助于厘清哪些公司具有可持续优势。

**标签**: `#AI`, `#China`, `#large language models`, `#industry analysis`, `#Goldman Sachs`

---