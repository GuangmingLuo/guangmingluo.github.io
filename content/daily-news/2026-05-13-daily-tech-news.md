---
title: "2026年5月13日 每日科技早报"
date: 2026-05-13T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源社区"]
description: "2026年5月13日 科技新闻摘要，涵盖人工智能、云计算、开源社区等领域的最新动态。"
---

## 📰 头条新闻

### 谷歌 Cloud Next '26 大会：GKE Agent Sandbox 和 Hypercluster 正式发布，Kubernetes 成为 AI 代理时代操作系统

在 Cloud Next '26 大会上，谷歌宣布了 Google Kubernetes Engine（GKE）的多项重大更新，其中最引人注目的是用于保证代理代码执行安全的 GKE Agent Sandbox，以及可以通过一个控制平面管理多达一百万个加速器芯片的 GKE hypercluster。

- **GKE Agent Sandbox**：利用 gVisor 为不受信任的代理代码执行提供内核级隔离，每秒可创建 300 个沙箱，延迟低于一秒。Lovable 平台每天为超过 20 万个 AI 生成项目提供支持，已在 Agent Sandbox 上运行生产工作负载。
- **GKE hypercluster**：已进入私有版正式发布阶段，可在 256000 个节点、横跨多个区域管理 100 万个芯片。
- **推理优化**：GKE Inference Gateway 的"预测性延迟优化"功能将首个 Token 延迟降低多达 70%，KV 缓存分层存储可提升 50-70% 吞吐量。

> 原文链接：[Google Announces GKE Agent Sandbox and Hypercluster at Next '26](https://www.infoq.com/news/2026/05/gke-agent-sandbox-hypercluster/)

---

## 🚀 云原生动态

### Kubernetes v1.36 正式发布：Volume Group Snapshots GA，DRA 迎来重大升级

Kubernetes v1.36 于 2026 年 4 月 22 日正式发布，带来多项重要更新：

**核心特性升级：**
- Volume Group Snapshots 升级为 GA
- Declarative Validation 升级为 GA
- Pod-Level Resource Managers 进入 Alpha
- In-Place Pod-Level Resources Vertical Scaling 进入 Beta
- Tiered Memory Protection with Memory QoS 引入分层内存保护

**DRA 重大更新：**
- Prioritized List 升级为 Stable
- Extended Resource Support 进入 Beta
- Partitionable Devices 进入 Beta
- Device Taints 进入 Beta
- Device Binding Conditions 进入 Beta
- Resource Health Status 进入 Beta

**废弃与移除：**
- gitRepo Volume Plugin 永久禁用（安全漏洞）
- IPVS Mode in kube-proxy 已移除

> 原文链接：[Kubernetes Blog](http://blog.kubernetes.io)

### 云原生智能体标准化：CNCF 发布《Cloud Native Agentic Standards》

CNCF 发布《Cloud Native Agentic Standards》白皮书，为云原生智能体提供标准化框架：

- **基础容器最佳实践**：安全（MELT 可观测性）、Gateway API 的 Inference Extensions
- **控制与通信**：MCP（Model Context Protocol）、A2A（Agent-to-Agent）、AP2（Agent Payment Protocol）
- **身份认证**：SPIFFE/SPIRE、Agntcy 身份框架
- **可观测性升级**：Token 使用量、推理成本、置信度追踪
- **治理**：Agent-as-a-Judge、Model Openness Framework

> 原文链接：[2026年K8s新战场：云原生智能体正在改写基础设施规则](https://blog.csdn.net/u012516914/article/details/159481030)

### KubeCon Europe 2026：华为云展示"智能原生"基础设施

在阿姆斯特丹举行的 KubeCon + CloudNativeCon Europe 2026 上，华为云以 "Powering the Agentic Future" 为主题参展：

- **Volcano**：AI 全生命周期调度引擎，推出 Kthena（LLM 推理）和 AgentCube（Agent 工作负载编排）
- **Karmada**：多云容器编排平台，支持跨云边界的统一调度
- **云原生 Agent 标准**：联合阿里云、CNCF 共同推进

> 原文链接：[华为云亮相 KubeCon Europe 2026](https://blog.csdn.net/hwcloud_OS/article/details/159732103)

---

## 🤖 AI前沿

### DeepSeek 拟融资 500 亿元，估值突破 3500 亿

据 The Information 报道，DeepSeek 正在寻求其首轮融资，计划募集最多 500 亿元人民币（约 73.5 亿美元）。若交易达成，将创下中国 AI 企业史上最大单笔融资纪录，整体估值有望突破 3500 亿元（约 515 亿美元）。

- **投资方**：国家集成电路产业投资基金、腾讯、阿里等巨头均被传出投资意向
- **V4.1 计划**：预计 6 月发布，新增图像、音频理解处理能力，强化 MCP 适配

> 原文链接：[DeepSeek拟融资500亿，国产AI掀凶猛融资潮](http://m.toutiao.com/group/7637526239380800027/)

### 月之暗面 Kimi 完成 20 亿美元融资，ARR 超 2 亿美元

月之暗面完成约 20 亿美元融资，投后估值突破 200 亿美元。本轮由美团龙珠领投，中国移动、CPE 源峰等参投。

- 公司半年内累计融资超 39 亿美元
- ARR 在 4 月已超 2 亿美元
- 付费订阅与 API 收入加速增长

> 原文链接：[国资与产业资本齐入场 AI领域频现大额融资](https://m.sohu.com/a/1020823883_120988533/)

### 阶跃星辰将完成近 25 亿美元融资，加速冲刺港股 IPO

阶跃星辰被曝将完成近 25 亿美元融资，本轮吸引了华勤技术、龙旗科技、豪威集团、中兴通讯等手机产业链企业，以及香港投资管理有限公司（HKIC）。

- 年内连续完成两轮大额融资（1月超50亿元B+轮、5月近25亿美元）
- 或将成为继智谱、MiniMax 之后第三家登陆港股的国产大模型企业

### 无问芯穹获 7 亿元融资，日均 Token 调用量增长超 20 倍

AI 原生基础设施公司无问芯穹宣布再获超 7 亿元融资，持续稳居中国 AI 原生基础设施公司融资规模之首。

- 核心 AgenticMaaS 平台已上线 160 余种大模型
- 日均 Token 调用量较 2025 年底增长超 20 倍
- 系统吞吐量较行业平均水平提升 2-3 倍

> 原文链接：[估值狂飙！DeepSeek拟融资500亿](https://m.sohu.com/a/1020823883_120988533/)

### 阿里千问：一周三款模型，调用量登顶全球

阿里云通义大模型团队在 4 月初一周内连续发布三款模型：

- **Qwen3.5-Omni**：全模态大模型，215 项音视频理解任务取得 SOTA
- **Wan2.7-Image**：图像生成与编辑统一模型，支持千人千面定制
- **Qwen3.6-Plus**：旗舰语言模型，日调用量突破 1.4 万亿 Token

> 原文链接：[2026年4月AI圈动态盘点](https://blog.csdn.net/weixin_41908519/article/details/159963116)

### 谷歌 Gemma 4 开源模型发布，Apache 2.0 许可证

谷歌 DeepMind 发布 Gemma 4 系列开源模型，包含 E2B、E4B、26B MoE 和 31B Dense 四款型号，全部采用 Apache 2.0 开源协议。

### Anthropic Claude Mythos Preview 发布，年化收入超 300 亿美元

Anthropic 发布 Claude Mythos Preview，代码和推理能力表现突出。基于安全考虑，该模型通过 "Project Glasswing" 计划向安全研究合作伙伴提供访问。

- 年化收入已超 300 亿美元
- 首次超过 OpenAI 的 250 亿美元

---

## 🔓 开源社区

### GitHub Trending 热门项目（2026年5月上旬）

**AI Agent 相关项目持续火爆：**
- **open-design**：本地优先的 AI 设计工具，替代 Anthropic 的 Claude Design，19 Skills + 71 Design Systems
- **UI-TARS-desktop**：字节跳动的多模态 AI Agent 栈，连接 cutting-edge AI 模型
- **agent-skills**：Anthropic 出品的生产级 AI 编码技能
- **GenericAgent**：自进化 Agent，技能树从 3.3K 行种子代码成长，Token 消耗降低 6 倍

**开发者工具热门：**
- **warp**：终端工具，本周飙升进入前 2
- **CloakBrowser**：通过所有机器人检测的 stealth Chromium
- **docuseal**：开源 DocuSign 替代方案

**资源推荐：**
- **dive-into-llms**：深度学习 LLM 指南
- **local-deep-research**：本地深度研究工具，支持 10+ 搜索引擎
- **TabPFN**：表格数据的 Foundation Model

> 原文链接：[GitHub Explore](https://github.com/explore)

### OpenClaw: After Hours @ GitHub HQ

GitHub 将于 6 月 3 日在旧金山举办 OpenClaw 活动，面向 Agentic 系统前沿的开发者。

> 原文链接：[GitHub OpenClaw](https://github.com/blog)

---

## 💡 行业观察

### 国产大模型"资本大年"与"上市元年"

2026 年正成为中国 AI 大模型的"资本大年"与"上市元年"：

| 公司 | 融资/轮次 | 估值 |
|------|----------|------|
| DeepSeek | 拟融资 500 亿 | ~3500 亿 |
| 月之暗面 | 累计超 376 亿 | ~1362 亿 |
| 阶跃星辰 | 近 170 亿（5月） | IPO冲刺 |
| 智谱 | 超 10 亿美元 | ~70 亿美元 |
| MiniMax | 8.5 亿美元 | ~55 亿美元 |

**三大特征：**
- 资本高度集中：头部企业资金门槛升至百亿级
- 模型迭代加速：发布节奏密集
- 智能体成为新焦点：从概念走向落地

---

## 📡 数据来源

- [Kubernetes Blog](http://blog.kubernetes.io)
- [InfoQ](https://www.infoq.com)
- [CSDN](https://blog.csdn.net)
- [GitHub Trending](https://github.com/explore)
- [36氪](https://36kr.com/)
- [新浪财经](http://finance.sina.com.cn)

---

*本文由每日科技早报自动生成，订阅地址：[guangmingluo.github.io](https://guangmingluo.github.io)*
