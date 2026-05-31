---
title: "2026年6月1日 每日科技早报"
date: 2026-06-01T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年6月1日 科技新闻摘要：GitHub Copilot改Token计费、宇树科技IPO上会、英伟达GTC Taipei开幕。"
---

## 📰 头条新闻

**GitHub Copilot正式告别固定订阅：从6月1日起改按Token消耗计费**

微软GitHub Copilot于今日（6月1日）正式将计费模式从固定月费切换为基于Token使用量的动态计费。每个AI credit等于1美分，用户根据输入Token、输出Token和缓存Token的实际消耗付费。这一变化已在开发者社区引发广泛争议，部分用户反映月度账单可能面临数十倍涨幅。

新计费方案下，Copilot Pro（$10/月）包含1000 credits，Copilot Pro+（$39/月）包含3900 credits，Copilot Business（$19/月/用户）包含1900 credits，Copilot Enterprise（$39/月/用户）包含3900 credits。企业用户可在8月31日前享受促销配额。值得注意的是，代码补全和Next Edit Suggestions功能仍保持无限使用，不消耗credits。

社区反馈呈现两极分化：部分用户表示其账单可能从$29涨至$750，或从$50跳升至$3000；但也有开发者指出，合理使用下成本可控，暴涨账单往往来自"氛围编程"式的高频冗余迭代。批评者认为，微软此前曾鼓励用户高强度使用AI辅助，如今单方面改规则让开发者承担后果。

📖 来源：[TechCrunch](https://www.techtimes.com/articles/317456/20260531/github-copilot-billing-switches-token-costs-today-agentic-users-face-steepest-increases.htm) | [环球网](http://m.toutiao.com/group/7645855741718364715/) | [华尔街见闻](http://m.toutiao.com/group/7645875345412883007/)

**宇树科技科创板IPO今日上会：人形机器人第一股来了**

今日上午，上海证券交易所召开2026年第31次上市审核委员会审议会议，审议宇树科技股份有限公司首发申请。宇树科技是全球四足机器人赛道头部玩家，产品远销海外，四足机器人累计销量已超过3万台。招股书显示，公司2024年已实现盈利，2025年前三季度净利润突破亿元。

此次IPO，宇树科技拟发行不低于4044.64万股，计划募集资金42.02亿元，将全部投向智能机器人模型研发、本体研发、新产品开发及制造基地建设。若成功过会，宇树科技将成为A股人形机器人第一股。

📖 来源：[财联社](https://c.m.163.com/news/a/KU89034805198CJN.html)

**英伟达GTC Taipei 2026大会今日开幕：Vera Rubin平台疑将揭晓**

英伟达年度AI开发者大会GTC Taipei 2026今日在台北盛大开幕，英伟达CEO黄仁勋发表主题演讲。大会议程涵盖AI工厂与扩充基础架构、代理与推理AI、科学领域AI、物理AI与机器人技术等多元主题。黄仁勋于5月23日提前抵达台北，先后拜访台积电创始人张忠谋、逛夜市吃刨冰为大会造势。

本次大会的焦点是英伟达下一代AI芯片平台Vera Rubin的相关细节。联发科已提前放出预告，暗示NVIDIA N1/N1X平台即将亮相。N1系列SoC规格近日泄露，包含20核Arm配置，分N1和N1X两版，预计填补PC处理器市场空白，挑战英特尔、AMD和苹果。

📖 来源：[36氪](https://36kr.com/) | [HyperAI超神经](https://hyper.ai/cn/stories?page=21)

---

## 🤖 AI前沿

**Liquid AI开源LFM2.5边缘大模型：8.3B参数仅激活1.5B，手机笔记本流畅运行**

AI创业公司Liquid AI发布并开源边缘侧大模型LFM2.5-8B-A1B，专为消费级硬件设计，优化了工具调用和指令遵循能力。该模型采用稀疏混合专家架构，总参数8.3B，但每个Token仅激活1.5B参数，在降低计算成本的同时增强推理性能，可流畅运行于手机和笔记本电脑。

📖 来源：[AIbase](https://www.aibase.com/search/Open-Source%20AI%20Model)

**阿里云百炼全面CLI化并开源：Agent开发门槛降至地板**

阿里云百炼平台宣布全面CLI化并开源，将主流模型调用、工作流编排、知识库管理、Agent开发等核心能力封装为命令行入口。开发者只需一行命令即可完成AI Agent的全栈能力搭建。这一动作表明AI Agent开发正在从"平台的游戏"变成"程序员的玩具"，当工具链足够简洁，AI应用生态有望迎来爆发。

📖 来源：[AIbase](https://www.aibase.com/news/28430)

---

## 🔓 开源社区

**MemPalace开源：给AI Agent装本地长期记忆，LongMemEval冠军R@5=96.6%**

MemPalace是一个纯本地运行的AI Agent记忆系统，通过四级层级结构（Palace→Wing→Room→Drawer）解决AI Agent"记不住"的核心痛点。其核心优势在于存储原文而非压缩总结，保证信息不丢失；支持MCP协议一键集成到Claude Code。GitHub已获52K Star，LongMemEval基准测试R@5达96.6%，API费用为零，数据完全本地处理不外传。

📖 来源：[HyperAI超神经](https://hyper.ai/cn/stories?page=21)

**next-ai-draw-io开源：3万Star的AI+图表工具，让模型直接操作draw.io XML**

next-ai-draw-io是GitHub上一个将AI能力接入draw.io的开源项目，目前Star数已超过3万。该项目核心创新是让AI直接操作draw.io背后的结构化XML，而非生成图片，这意味着产出的图表可以继续被打开、编辑、保存和版本管理。项目还实现了MCP Server，支持Claude Code等AI Agent直接调用绘图能力，适合RAG架构图、云架构图、技术文档插图等场景。支持模型包括Claude Sonnet 4.5、GPT-5.1、Gemini 3 Pro等。

📖 来源：[硅基观察室](http://m.toutiao.com/group/7646028266603610651/)

---

## 💡 行业观察

**天机智能完成10亿元B轮及B+轮融资，跻身独角兽行列**

广东东莞具身智能Infra创企天机智能宣布完成10亿元B轮及B+轮融资，由高瓴创投、美团战投联合领投，腾讯、高榕创投、光合创投、纪涵资本等跟投，投后估值近百亿跻身独角兽。融资将用于技术研发、大规模量产及全球销售网络建设。天机智能聚焦具身智能基础设施赛道，与宇树科技等人形机器人整机厂商形成产业链协同。

📖 来源：[财联社](https://c.m.163.com/news/a/KU89034805198CJN.html)

**更新｜长鑫科技科创板IPO获上市委会议通过：Q1营收突破千亿**

长鑫科技集团股份有限公司科创板IPO获上市委会议通过。公司2026年上半年预计营收1100亿至1200亿元，同比增长612%至677%；预计归母净利润500亿至570亿元，同比增长2244%至2544%。此次IPO拟募资295亿元，用于存储器晶圆制造量产线技术升级改造、DRAM存储器技术升级等项目。

📖 来源：[财联社](https://c.m.163.com/news/a/KU89034805198CJN.html)

**软银计划投资750亿欧元在法国建设数据中心：欧洲最大AI基建投资**

软银宣布计划投资750亿欧元在法国建设数据中心，目标部署5吉瓦容量。此举是软银在欧盟最大的AI基础设施投资，旨在抢占欧洲算力高地。三星、海力士和美光三大存储芯片厂商市值均已突破万亿，AI爆发需求、行业寡头垄断及长期供货协议三大因素正重塑存储芯片格局。

📖 来源：[HyperAI超神经](https://hyper.ai/cn/stories?page=21)

**四部门联合印发2026年提升全民数字素养与技能工作要点**

中央网信办、教育部、工信部、人社部联合印发《2026年提升全民数字素养与技能工作要点》，部署6方面15项重点任务，其中包括"提升全民人工智能素养"专项，要求强化AI赋能教育、加快AI人才培育、深化AI普及应用。

📖 来源：[财联社](https://c.m.163.com/news/a/KU89034805198CJN.html)

---

## 📚 数据来源

- [36氪](https://36kr.com)
- [财联社](https://www.cls.cn)
- [TechCrunch](https://techcrunch.com)
- [AIbase](https://www.aibase.com)
- [HyperAI超神经](https://hyper.ai)
- [华尔街见闻](https://wallstreetcn.com)

---

> 📌 本日报由自动化系统生成，每日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
