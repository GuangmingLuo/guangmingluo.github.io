---
title: "2026年6月1日 每日科技早报"
date: 2026-06-01T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年6月1日 科技新闻摘要：GitHub Copilot正式切换Token计费、英伟达GTC Taipei开幕、Liquid AI开源LFM2.5边缘模型。"
---

## 📰 头条新闻

**GitHub Copilot正式切换Token计费，社区争议激烈**

6月1日起，GitHub Copilot计费模式从固定订阅费切换为基于Token使用量的动态计费。每个AI Credit等于1美分，用户根据输入、输出和缓存Token的实际消耗付费。Copilot Pro（$10/月）含1000 Credits，Copilot Pro+（$39/月）含3900 Credits。代码补全和Next Edit Suggestions仍保持无限使用，不消耗Credits。

社区反馈两极分化：部分用户反映账单可能从$29涨至$750，或从$50跳升至$3000；但也有开发者指出，合理使用下成本可控，暴涨账单往往来自高频冗余的"氛围编程"迭代。批评者认为微软此前鼓励用户高强度使用AI辅助，如今单方面改规则让开发者承担后果。GitHub官方讨论帖已积累超400条评论和近900个踩。

📖 来源：[TechTimes](https://www.techtimes.com/articles/317456/20260531/github-copilot-billing-switches-token-costs-today-agentic-users-face-steepest-increases.htm) | [环球网](http://m.toutiao.com/group/7645855741718364715/)

**更新｜英伟达GTC Taipei 2026今日开幕，N1X笔记本芯片首度亮相**

英伟达GTC Taipei 2026今日在台北开幕，黄仁勋发表主题演讲。此前5/27报道GTC Taipei预告，本次重点：英伟达首款笔记本SoC——N1X正式亮相，搭载20核Arm CPU（联发科设计，台积电3nm）和相当于桌面RTX 5070的GPU（6144 CUDA核心），首批设备预计2026年底上市。Vera Rubin平台相关细节也有更新，摩根士丹利数据显示VR200物料成本较GB300大幅上涨，其中内存成本飙升435%。此外，英伟达宣布在台新总部"Constellation"项目，年采购额计划从当前1000亿美元增至1500亿美元。

📖 来源：[TechTimes](https://www.techtimes.com/articles/317446/20260530/computex-2026-jensen-huang-keynote-n1x-reveal-arc-g3-snapdragon-c-all-land-this-week.htm) | [TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261937540-computex-2026-jensen-huang-chip-titans-ai-highlights-watch-taipei-tradingkey)

---

## 🤖 AI前沿

**Liquid AI开源LFM2.5-8B-A1B边缘大模型：8.3B参数仅激活1.5B**

Liquid AI发布并开源边缘侧稀疏MoE模型LFM2.5-8B-A1B，总参数8.3B，每个Token仅激活1.5B。上下文窗口从32K扩展至128K，预训练数据增至38T tokens。该模型转为"先思考、后回答"的推理模式，幻觉率从前代7.46%降至63.47%（AA-Omniscience），工具调用能力大幅提升（Tau² Telecom从13.6%飙至88.07%）。在Apple M5 Max上可达253 tok/s，手机端约28 tok/s。另据《The Information》披露，苹果已将Liquid AI列为潜在收购对象。权重已在Hugging Face开放下载。

📖 来源：[Liquid AI官方博客](https://www.liquid.ai/blog/lfm2-5-8b-a1b) | [Gigazine](https://gigazine.net/gsc_news/en/20260531-lfm25-8b-a1b)

**阿里云百炼核心能力CLI化并开源**

阿里云5月29日宣布百炼核心能力CLI化并开源。百炼CLI支持一行命令调用150多款模型、十多款应用以及知识库、记忆、联网搜索等能力，原生适配Claude Code、OpenClaw、Hermes Agent等主流Agent框架。项目已在GitHub开源。

📖 来源：[IT之家](http://m.toutiao.com/group/7645210069247869483/) | [阿里云开发者社区](https://developer.aliyun.com/article/1738588)

---

## 🔓 开源社区

**MemPalace开源：本地AI Agent记忆系统，LongMemEval R@5达96.6%**

MemPalace是由Milla Jovovich参与创建的开源本地AI Agent记忆系统，采用"记忆宫殿"层级结构（Palace→Wing→Room→Drawer），核心设计是存储原文而非压缩总结。支持MCP协议一键集成Claude Code等客户端，LongMemEval基准测试R@5达96.6%（加入rerank后100%）。纯本地运行，零API费用，GitHub已获约48K Star。

📖 来源：[GitHub](https://github.com/milla-jovovich/mempalace) | [51CTO](https://blog.51cto.com/u_16213702/14642448)

**next-ai-draw-io开源：AI+draw.io图表工具，Star数超3万**

next-ai-draw-io将AI能力接入draw.io，核心创新是让AI直接操作draw.io的结构化XML而非生成图片，产出的图表可继续编辑、保存和版本管理。项目实现了MCP Server，支持Claude Code等AI Agent直接调用绘图能力，适合RAG架构图、云架构图等场景。

📖 来源：[GitHub](https://github.com/nicholaschenai/next-ai-draw-io)

---

## 💡 行业观察

**更新｜宇树科技科创板IPO今日上会**

上海证券交易所今日审议宇树科技首发申请。宇树科技是全球四足机器人头部厂商，累计销量超3万台，2024年已实现盈利，2025年前三季度净利润突破亿元。拟发行不低于4044.64万股，募资42.02亿元。若过会将成为A股人形机器人第一股。（5/25已报人形机器人IPO三连发）

📖 来源：[财联社](https://www.cls.cn)

**更新｜长鑫科技科创板IPO获上市委通过**

长鑫科技科创板IPO获上市委会议通过。公司2026年上半年预计营收1100-1200亿元，同比增长612%-677%；预计归母净利润500-570亿元，同比增长2244%-2544%。拟募资295亿元用于存储器晶圆制造量产线技术升级等项目。（5/18已报Q1财报/IPO上会，5/28已报提交注册）

📖 来源：[财联社](https://www.cls.cn)

**天机智能完成10亿元B轮及B+轮融资**

广东东莞具身智能Infra创企天机智能完成10亿元B轮及B+轮融资，高瓴创投、美团战投联合领投，腾讯、高榕创投等跟投，投后估值近百亿跻身独角兽。融资将用于技术研发、量产及全球销售网络建设。

📖 来源：[财联社](https://www.cls.cn)

**软银计划投资750亿欧元在法国建设数据中心**

软银宣布计划投资750亿欧元在法国建设数据中心，目标部署5吉瓦容量，是软银在欧盟最大的AI基础设施投资。

📖 来源：[TradingKey](https://www.tradingkey.com/analysis/stocks/us-stocks/261937540-computex-2026-jensen-huang-chip-titans-ai-highlights-watch-taipei-tradingkey)

**四部门联合印发2026年提升全民数字素养与技能工作要点**

中央网信办、教育部、工信部、人社部联合印发《2026年提升全民数字素养与技能工作要点》，部署6方面15项重点任务，含"提升全民人工智能素养"专项。

📖 来源：[财联社](https://www.cls.cn)

---

## 📚 数据来源

- [Liquid AI 官方博客](https://www.liquid.ai/blog)
- [财联社](https://www.cls.cn)
- [TechTimes](https://www.techtimes.com)
- [IT之家](https://www.ithome.com)
- [TradingKey](https://www.tradingkey.com)
- [阿里云开发者社区](https://developer.aliyun.com)

---

> 📌 本日报由自动化系统生成，每日工作日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
