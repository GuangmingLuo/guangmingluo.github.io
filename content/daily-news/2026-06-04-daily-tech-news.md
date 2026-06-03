---
title: "2026年6月4日 每日科技早报"
date: 2026-06-04T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年6月4日 科技新闻摘要：SpaceX IPO路演正式启动、GitHub Copilot推出独立桌面应用、阶跃Step 3.7 Flash成全球最受关注开源模型。"
---

## 📰 头条新闻

**更新｜SpaceX IPO定价每股135美元，6月4日起全球路演**

SpaceX于6月3日确认IPO核心参数：每股定价135美元，计划发行5.556亿股，融资750亿美元，目标估值1.75万亿美元。路演于6月4日正式启动（由高盛、摩根士丹利、美银等21家投行承销），6月11日确定发行价，6月12日以代码"SPCX"登陆纳斯达克。

本次采用纯新股发行架构，所有募资归公司所有，现有股东无法套现。S-1文件显示：Starlink是唯一盈利业务，受AI基础设施、Starship研发和卫星部署拖累，Q1净亏损扩大至每股1.27美元。Morningstar分析师估值约7800亿美元，对"轨道数据中心"等未经验证项目发出风险警示。另有报道称马斯克拟将IPO股份30%分配给个人投资者、上市15个交易日后纳入纳斯达克100指数。（6/2已报IPO启动）

📖 来源：[财联社](https://finance.eastmoney.com/a/202606033758252536.html) | [Particle.news](https://particle.news/story/spacex-seeks-75-billion-ipo-at-175-trillion-valuation-with-135-a-share-target)

---

## 🤖 AI前沿

**GitHub Copilot发布独立桌面应用，Autonomous Agent Mode七月上线**

微软在Build 2026上正式发布GitHub Copilot App，定位为"智能体原生桌面体验"。新应用包含"My Work"统一控制台，可同时管理多个AI Agent的任务（修复Bug、实现新功能、PR Review等）。开发者可通过语音直接下达指令。配合发布两个新执行模式：Fleet模式支持仓库级重构无需逐步确认，Autopilot模式允许无人值守运行定义好的Issue队列。安全性方面支持沙箱隔离，并引入实验性AI风险评估系统。订阅模式延续Token计费，企业版Autonomous Agent Mode将于7月正式开放。（GitHub Copilot Token计费6/1已报）

📖 来源：[TechFastForward](https://www.techfastforward.com/articles/github-copilot-app-builds-autonomous-coding-agents) | [GIGAZINE](https://gigazine.net/gsc_news/en/20260603-github-copilot-app/)

**阶跃Step 3.7 Flash成为OpenRouter全球第二位最受欢迎开源模型**

阶跃星辰最新开源基座模型Step 3.7 Flash发布仅两天，即登上OpenRouter Trending全球第二位，成为近期开发者社区最受关注的开源模型之一。该模型面向Agent生产化阶段推出，围绕Agent、Coding、Search和多模态工作流进行系统优化。（6/1已报阶跃星辰融资）

📖 来源：[每日经济新闻](http://m.toutiao.com/group/7647308070686671395/)

**Google Gemma 4 12B发布：16GB显存可运行，原生多模态**

Google发布Gemma 4 12B，是Gemma 4系列中首款支持原生音频输入的中型模型。基于无编码器架构（encoder-free），可直接处理文本、图像和音频，无需独立编码器。在配备16GB显存的笔记本上即可运行。Apache 2.0许可证发布于Hugging Face和Kaggle。Gemma 4系列全球下载量已突破1.5亿次。（Gemma 4系列6/2已报）

📖 来源：[Agentic Tribune](https://agentictribune.com/article/20260603-google-launches-gemma-4-12b-an-open-licensed-multimodal-ai-that-runs-on-16gb-laptops)

---

## 🚀 云原生

**Google开源Agent Executor：Kubernetes原生Agent工作流运行时**

Google发布Agent Executor开源项目，为长时间运行的Agent工作流提供标准化管理能力。核心特性：持久化执行（事件日志+快照，支持故障恢复）、安全隔离（沙箱机制防止有害副作用）、会话一致性（单写架构防止状态损坏）、连接恢复（客户端可重新连接并接收补发响应）、轨迹分支（检查点支持探索不同决策路径）。与Google Kubernetes Engine团队合作开发的Agent Substrate可实现Agent在Pod间的实时迁移，优化计算资源调度。

📖 来源：[Google Cloud Blog](https://cloud.google.com/blog/products/kubernetes-engine/google-open-source-agent-executor) | [GitHub](https://github.com/google/agent-executor)

---

## 🔓 开源社区

**千问向第三方Agent、Skill全面开放**

千问宣布向第三方Agent和Skill全面开放，所有企业均可接入Skill，未来可在千问运营自有品牌Agent。目前瑞幸咖啡、肯德基、东方航空等首批企业已提供Skill服务，用户可体验到店自取等功能。企业可自定义Agent人设与服务边界，以对话形式提供产品服务。

📖 来源：[每日经济新闻](http://m.toutiao.com/group/7647308070686671395/)

---

## 💡 行业观察

**联芸科技定增20.62亿元投向数据中心存储主控芯片**

科创板上市公司联芸科技定增申请获上交所受理，拟募资不超20.62亿元，全部投向面向数据中心与智能终端的新一代数据存储主控芯片研发项目并补流。募投涵盖三大方向：企业级PCIe Gen6 SSD主控芯片（瞄准AI服务器数据中心）、消费级PCIe Gen6 SSD主控芯片、UFS 5.0嵌入式存储主控芯片。公司2024年11月IPO实际募资11.25亿元，截至Q1末尚有2.89亿元未使用。

📖 来源：[经济参考报](https://www.stcn.com/article/detail/3940429.html)

**好达电子科创板IPO获受理：年产能60亿颗滤波器**

国内声表面波滤波器IDM企业好达电子科创板IPO申请获受理，拟募资18.36亿元投向TC-SAW及TF-SAW滤波器产线扩建。公司是国内极少数具备芯片设计-晶圆制造-封装测试全链路能力的IDM厂商，年产能60亿颗，客户覆盖OPPO、vivo、小米、三星及比亚迪等头部品牌。TF-SAW技术可媲美BAW滤波器，是5G/6G高频段关键方案。

📖 来源：[搜狐财经](https://m.sohu.com/a/1031365807_121124376/)

---

## 📚 数据来源

- [财联社](https://www.cls.cn)
- [TechFastForward](https://www.techfastforward.com/)
- [GIGAZINE](https://gigazine.net/)
- [Particle.news](https://particle.news/)
- [经济参考报](https://www.stcn.com)
- [每日经济新闻](http://m.toutiao.com/)
- [Google Cloud Blog](https://cloud.google.com/blog/)

---

> 📌 本日报由自动化系统生成，每日工作日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
