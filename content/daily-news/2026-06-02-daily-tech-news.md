---
title: "2026年6月2日 每日科技早报"
date: 2026-06-02T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年6月2日 科技新闻摘要：微软Copilot因Azure断电大规模故障、Anthropic提交SEC S-1启动IPO流程、Google Gemma 4系列发布。"
---

## 📰 头条新闻

**微软Copilot因Azure断电大规模故障，云端AI可靠性引担忧**

5月29日起，微软Azure东美数据中心遭遇雷暴天气导致断电事故，影响微软365 Copilot等核心AI服务。备用发电机因洪水和自动转换开关故障无法启动，UPS单元因电压尖峰损坏，冷却系统失效后服务器开始过热。尽管紧急关机保护了硬件，多个服务器集群仍被迫下线。微软Azure状态页面于5/29下午确认"严重降级"，Copilot在Windows、Office等应用中无法使用或响应极慢。截至6/2上午，微软表示服务已恢复，但欧洲和亚洲地区因跨大西洋网络拥塞仍存在间歇性问题。该事件引发行业对云端AI基础设施弹性的广泛讨论——AI服务深度嵌入日常工作后，其故障成本远超传统云服务。

📖 来源：[Windows News](https://windowsnews.ai/article/microsoft-copilot-down-azure-power-incident-causes-widespread-disruption-june-1-2026.421260) | [Windows Forum](https://windowsforum.com/threads/microsoft-copilot-slow-or-unreachable-after-azure-power-incident-june-1-2026.421260/)

---

## 🤖 AI前沿

**更新｜MiniMax M3编程评测超GPT-5.5，开源权重即将发布**

MiniMax于6/1发布的M3模型编程评测集SWE-Bench Pro得分59.0%，超越GPT-5.5和Gemini 3.1 Pro，接近Opus 4.7；在Terminal-Bench 2.1得分66.0%，KernelBench Hard得分28.8%；自主论文复现（12小时18次提交）和CUDA内核优化（9.4倍加速）展示强Agentic能力。采用自研稀疏注意力架构MSA，100万上下文下单token计算量降至前代1/20，Prefill加速9倍+、Decoding加速15倍。Token Plan订阅方案：Plus 49元/月、Max 119元/月、Ultra 469元/月。模型权重及技术报告将于10天内开源。（6/1已报）

📖 来源：[凤凰网](https://tech.ifeng.com/c/8tb4RhHvtIJ) | [IT之家](https://www.ithome.com)

**更新｜Anthropic提交SEC S-1启动IPO流程，估值9650亿美元成全球最高**

Anthropic于6/1向SEC提交保密S-1招股书，启动可能成为史上最大IPO之一的上市流程。公司当前估值9650亿美元（5月底H轮融资后），ARR突破470亿美元，Claude Code等企业产品增长迅猛。Wedbush分析师称其为"结构性转变"而非单纯上市事件。2026年三大AI IPO（SpaceX、OpenAI、Anthropic）将争夺同一机构资本池——SpaceX目标估值1.75万亿美元并最快6月启动路演，OpenAI目标Q4上市。Anthropic是首家冲刺IPO的前沿AI实验室，也是PBC（公益公司）结构上市的首例。（5/29已报H轮650亿、估值9650亿）

📖 来源：[StockWireX](https://stockwirex.com/news/anthropic-ipo-filing-june-2026/) | [Asia Economics](https://www.asiae.co.kr/en/article/world-general/2026060203532027135)

**微软Build 2026开源Windows Agent Framework，Project Polaris替代GPT-4**

微软Build 2026于6/2-3日在旧金山举行，主题为自主Agent。核心发布：Windows Agent Framework v1.0以MIT许可证开源，开发者用YAML定义Agent即可跨本地Windows、Windows 365、Azure Arc设备运行；全新Agent Runtime管理生命周期、内存和权限；Copilot Workspace脱离Beta成为完整Agent编程环境。战略级消息：Project Polaris将于8月替代GPT-4 Turbo成为GitHub Copilot默认模型（可选三个月回退），微软开始与OpenAI从依赖走向竞争。

📖 来源：[TechFastForward](https://techfastforward.com/articles/microsoft-build-2026-cuts-the-openai-cord-with-polaris)

**英伟达发布Cosmos 3开源物理AI世界模型**

英伟达GTC Taipei 2026发布Cosmos 3，首个原生支持文本/图像/视频/声音/动作多模态的开源全模态物理AI基础模型。采用MoT（混合Transformer）架构，将物理AI训练周期从数月缩短至数天。可作为VLM观察物理世界、作为世界模型生成物理精确合成视频、作为仿真器实现闭环策略训练。Artificial Analysis榜单排名开源第一，Physics-IQ、PAI-Bench、R-Bench等多项基准测试领先。配套发布Cosmos Coalition联盟，联合Black Forest Labs、Runway等推进开放世界模型生态。

📖 来源：[NVIDIA官方新闻稿](https://www.nasdaq.com/press-release/nvidia-launches-cosmos-3-open-frontier-foundation-model-physical-ai-2026-06-01) | [GIGAZINE](https://gigazine.net/gsc_news/en/20260601-nemotron-3-ultra/)

**英伟达发布5500亿参数Nemotron 3 Ultra开源模型**

英伟达发布5500亿参数混合专家模型Nemotron 3 Ultra，基于SSM+MoE混合架构。性能领先同级别开源前沿模型，推理速度提升5倍，推理总成本（含FLOPs与时间）降低30%。支持主流智能体平台（Hermes Agent、LangChain、OpenClaw、OpenHands、OpenCode），CrowdStrike、Palantir、SAP、ServiceNow等已部署。预计6/4通过Hugging Face、ModelScope、OpenRouter、build.nvidia.com发布。

📖 来源：[NVIDIA官方新闻稿](https://www.nasdaq.com/press-release/nvidia-launches-cosmos-3-open-frontier-foundation-model-physical-ai-2026-06-01) | [IT之家](https://www.ithome.com)

**Google Gemma 4系列发布，AIME 2026得分89.2%**

Google发布Gemma 4系列开源模型，其中31B版本AIME 2026得分89.2%，在数学、代码和Agent任务上超越Llama 4系列，Apache 2.0许可证免费使用。基于与Gemini 3相同的研究和技术框架，商业使用限制较少。26B版本可在消费级GPU（如RTX 5070 Ti）上本地运行，量化后仅需16GB显存。

📖 来源：[TechFastForward](https://techfastforward.com/articles/google-gemma-4-31b-beats-400b-rivals-zero-license-cost)

**JetBrains开源Mellum2编程模型：12B参数仅激活2.5B**

JetBrains发布并开源Mellum2，12B参数的MoE编程模型，每Token仅激活2.5B参数，推理时间较同等密度模型减少一半以上。Apache 2.0许可证发布在Hugging Face，支持代码补全，自然语言处理、路由、摘要和中间推理流程。JetBrains定位其为"焦点模型"——适合高频低延迟任务的专用组件，典型场景包括AI负载路由、RAG管道构建、复杂工作流中的子Agent控制、私有部署等。

📖 来源：[TechZine EU](https://www.techzine.eu/news/devops/141755/jetbrains-releases-mellum2-coding-model/)

---

## 🔓 开源社区

**OpenAI Codex rust SDK v0.136.0发布**

OpenAI Codex rust SDK发布v0.136.0版本，主要更新：TUI markdown保持网页链接可点击；会话支持归档（`/archive`或`codex archive`），归档会话受保护不被恢复/分叉；支持MCP服务器状态显示；Windows沙箱配置新增alpha版提升路径。

📖 来源：[GitHub newreleases.io](https://newreleases.io/project/github/openai/codex/release/rust-v0.136.0)

**GitHub Trending：odysseus登顶，自托管AI工作空间获7233星**

本周GitHub热门项目odysseus（自托管AI工作空间）获得7,233 Star，上线不到一周。该项目实现AI能力产品化，降低大模型应用开发门槛。此外还有guizang-social-card-skill（小红书图文生成，2,023星）、gemini-web2api（Gemini转OpenAI兼容API，878星）、SenPaiScanner（Cloudflare IP扫描器，797星）等热门项目。

📖 来源：[GitHub Trending](http://m.toutiao.com/group/7646206265982517800/)

**Zig编程语言坚持禁止AI代码贡献，创建者称其为"垃圾"**

Zig创建者Andrew Kelley在JetBrains播客中表示，项目拒绝任何AI辅助生成的代码贡献，将其称为"垃圾"（"rubbish"）。Zig代码贡献由核心团队人类成员审查，Kelley认为AI贡献者像"路过型贡献者"——可能提交一两个PR但不会真正融入核心团队。Zig是少数坚持全面禁止AI代码的开源项目之一，其他项目包括QEMU、NetBSD和OBS Studio。

📖 来源：[36氪](https://eu.36kr.com/zh/p/3832633186952833)

**Apache Weblate 2026.6.1发布**

Weblate发布v2026.6.1版本，修复了语言级公告不再破坏语言概述页面的bug。

📖 来源：[newreleases.io](https://newreleases.io/project/github/WeblateOrg/weblate/release/weblate-2026.6.1)

**Refined GitHub 26.6.1发布**

Refined GitHub浏览器扩展发布v26.6.1版本，改进了GitHub导航和生产力功能，支持Chrome、Firefox和Edge。

📖 来源：[Warp2Search](https://www.warp2search.net/story/refined-github-for-chrome-firefox-and-edge-2661-released/)

---

## 💡 行业观察

**XCENA完成2000亿韩元B轮融资，估值突破8000亿韩元**

韩国AI芯片初创公司XCENA完成2000亿韩元B轮融资（原定目标1000亿韩元），由Atinum Investment和IMM Investment领投，逾10家新机构跟投，现有投资者Mirae Asset、LB Investment等追加投资。公司由前SK海力士高管Kim Jin-young创立，专注CXL（Compute Express Link）内存芯片研发，MX1芯片今年量产有望改善AI数据处理效率。估值从2024年A轮时的2500亿韩元增至8000亿韩元以上。资金将用于下一代CXL内存产品研发和全球销售网络建设。

📖 来源：[Chosun Biz](https://www.chosun.com/english/market-money-en/2026/06/01/7XIIYO5GKRCVTPH6EOK2FW3T2E/)

**存储芯片"超级周期"持续，三巨头市值破万亿**

三星电子、美国美光和SK海力士三家存储芯片制造商股价相继突破万亿美元市值，HBM（高带宽内存）需求激增是核心驱动力。AI基础设施建设带来长期结构性需求，使市场认为存储行业有望进入比以往更长的结构性高景气阶段。三星、SK海力士、美光是HBM主要制造商，AI大客户普遍提前锁定产能确保供应。不过部分机构已发出泡沫预警，美国范达公司负责人认为内存股已呈现"泡沫化"特征。

📖 来源：[经济参考报](https://www.stcn.com/article/detail/3935968.html)

---

## 📚 数据来源

- [NVIDIA Newsroom](https://nvidianews.nvidia.com/)
- [StockWireX](https://stockwirex.com/)
- [Windows News](https://windowsnews.ai/)
- [IT之家](https://www.ithome.com)
- [GIGAZINE](https://gigazine.net/)
- [TechFastForward](https://techfastforward.com/)
- [36氪](https://36kr.com/)
- [经济参考报](https://www.stcn.com)

---

> 📌 本日报由自动化系统生成，每日工作日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
