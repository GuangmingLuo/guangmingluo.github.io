---
title: "2026年5月29日 每日科技早报"
date: 2026-05-29T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年5月29日 科技新闻摘要：Claude Opus 4.8发布+Dynamic Workflows、NVIDIA Polar开源框架、Snowflake与AWS签60亿美元协议。"
---

## 📰 头条新闻

**Anthropic发布Claude Opus 4.8+Dynamic Workflows，同日完成650亿美元H轮融资估值首超OpenAI**

5月28日，Anthropic发布新一代旗舰模型Claude Opus 4.8，在编码、智能体任务、推理和知识工作方面均有提升。SWE-Bench Pro得分从64.3%提升至69.2%，超越GPT-5.5和Gemini 3.1 Pro。最大亮点是"诚实度"提升——模型更倾向标注不确定性，代码缺陷未说明通过率降低约4倍。定价不变（输入$5/百万token，输出$25/百万token），Fast Mode速度提升2.5倍且成本降至原来1/3。

同日发布Claude Code重大更新（v2.1.154，44项变更）：Dynamic Workflows支持数十至数百个Agent后台协调执行；安全修复包括危险路径拦截和数据泄露检测；桌面版支持多会话并行、内置终端和SSH远程连接。

同日，Anthropic宣布完成650亿美元H轮融资，投后估值达9650亿美元，首次超越OpenAI（8520亿美元）成为全球估值最高的AI初创企业。本轮由Altimeter Capital、Dragoneer、Greenoaks和红杉资本领投，亚马逊贡献50亿美元，美光、三星、SK海力士以战略伙伴身份参与。Anthropic年化营收已突破470亿美元，预计Q2首次盈利。

📖 来源：[Anthropic](https://www.anthropic.com) | [财联社](http://m.toutiao.com/group/7645049146293977640/) | [9to5Mac](https://9to5mac.com/2026/05/28/anthropic-upgrades-claude-with-new-opus-4-8-model-heres-whats-new/) | [36氪](https://36kr.com/p/3829512317379713)

---

## 🤖 AI前沿

**面壁智能PilotDeck开源：项目级Agent操作系统，白盒记忆+智能路由**

清华THUNLP、面壁智能与OpenBMB联合开源智能体操作系统PilotDeck，核心设计以"工作舱WorkSpace"取代对话框，为每个项目建立独立环境：记忆白盒化让AI记忆全链路可见可改可追溯；"Dream"机制支持空闲整理与一键回滚；智能路由根据任务难度动态分配模型，社交媒体场景成本节省近70%，复杂任务1/6成本效果反超Sonnet 4.6单Agent。支持Always-on常驻任务24小时自主推进。GitHub：https://github.com/OpenBMB/PilotDeck

📖 来源：[36氪](https://36kr.com/p/3828807269274503) | [腾讯新闻](http://news.qq.com/rain/a/20260528A077Z600)

**快手可灵AI Q1收入同比增长超300%，年化收入近5亿美元**

快手2026年Q1财报显示，可灵AI收入同比增长超300%，商业化进程提速。2026年3月可灵AI年化收入（ARR）近5亿美元，而去年3月仅1亿美元，一年内增长4倍。CEO程一笑表示增长主要来自B端API调用和P端付费会员双轮驱动。

📖 来源：[21世纪经济报道](http://m.toutiao.com/group/7644976584062943790/)

---

## 🔓 开源社区

**NVIDIA开源Polar框架：不改代码让Codex SWE-Bench分数从3.8%飙至26.4%**

英伟达研究团队开源智能体强化学习框架Polar，核心创新是在模型API边界放置代理，无需修改现有智能体框架（Codex/Claude Code/Qwen Code）即可接入GRPO强化学习训练。基于同一Qwen3.5-4B底座模型，Codex框架下SWE-Bench Verified pass@1从3.8%提升至26.4%，Claude Code从29.8%提升至34.6%。引入prefix_merging策略后训练墙钟时间缩短5.39倍，GPU利用率从20.4%升至87.7%。论文：https://arxiv.org/pdf/2605.24220

📖 来源：[IT之家](https://www.ithome.com/0/956/293.htm) | [NVIDIA/MarkTechPost](https://news.aibase.com/news/28430)

**自变量Wall-OSS-0.5开源：预训练具身模型无微调直接上机跑17个任务**

自变量机器人开源Wall-OSS-0.5预训练具身大模型，在20多种机器人形态、100万条轨迹及9000万多模态语料上完成预训练。无微调直接上真机跑17个任务，未见过的"绳子收紧"柔性双臂操作零样本拿到82分，微调后平均任务进度比π0.5领先17.5分。

📖 来源：[新智元/36氪](https://36kr.com/p/3828807269274503)

---

## 💡 行业观察

**Snowflake Q1营收增33%与AWS签60亿美元五年协议，盘后暴涨36%**

Snowflake第一财季营收13.9亿美元，同比增长33%，远超预期。公司宣布未来五年向AWS投入60亿美元，涵盖Graviton芯片及AI GPU资源，这是继Anthropic之后AWS在AI领域又一重大客户承诺。值得关注的是，随着AI从聊天机器人向智能体转型，具备通用计算能力的CPU（如Graviton）正迎来需求复苏。公司还宣布收购AI智能体平台Natoma，全年产品营收指引上调至58.4亿美元。

📖 来源：[华尔街见闻](http://m.163.com/dy/article/KU0P9BH105198NMR.html) | [金融界](http://m.toutiao.com/group/7644841046631662130/)

**更新｜Anthropic完成650亿美元H轮融资，估值9650亿美元首超OpenAI**

Anthropic正式完成H轮融资，投后估值9650亿美元，超越OpenAI的8520亿美元。本轮由Altimeter Capital、Dragoneer、Greenoaks和红杉资本领投，云厂商承诺投资150亿美元（亚马逊50亿）。美光、三星、SK海力士以战略基础设施伙伴身份参与。年化营收突破470亿美元，预计Q2首次盈利。正在积极筹备IPO，预计最快10月上市。

📖 来源：[财联社](http://m.toutiao.com/group/7645049146293977640/) | [IT之家/TechCrunch](https://finance.jrj.com.cn/2026/05/29074757245301.shtml)

**墨芯完成近10亿元C轮融资，稀疏计算加速商业化闭环**

国产AI芯片创企墨芯人工智能完成近10亿元C轮融资，由深创投、岩山科技、大湾区共同家园等联合投资。墨芯是国内少数走差异化稀疏计算路线的创企，AI加速卡在MLPerf评测中三度夺冠，性能超过英伟达A100、H100。预计年底发布新一代推理卡SparsePrime，基于自研Antoum2.0芯片架构。

📖 来源：[36氪](https://36kr.com/p/3828243885707913)

**市场监管总局、发改委联合印发AI计量体系指引(2026版)**

市场监管总局、国家发展改革委联合印发《人工智能计量体系和能力建设指引（2026版）》，围绕基础支撑、通用技术、核心技术、计量技术规范、计量服务产业、智能赋能计量六大部分系统布局。针对算法"黑箱"、决策可解释性差等痛点，推动建立AI可靠、安全、可信的计量标准。

📖 来源：[市场监管总局](https://www.samr.gov.cn/xw/zj/art/2026/art_f43aa2c974654d66b91bbad8410d0d71.html) | [新华网](http://www.xinhuanet.com/tech/20260528/60a3478007284ff2892dc98ff74b30d3/c.html)

**戴尔Q1业绩超预期，AI服务器展望上调盘后涨38%**

戴尔科技第一财季业绩远超预期，受益于AI服务器需求强劲，公司上调全年AI服务器销售额展望。财报公布后戴尔盘后涨幅扩大至38%。

📖 来源：[华尔街见闻](https://wallstreetcn.com)

---

## 📚 数据来源

- [Anthropic](https://www.anthropic.com)
- [36氪](https://36kr.com)
- [财联社](https://www.cls.cn)
- [IT之家](https://www.ithome.com)
- [华尔街见闻](https://wallstreetcn.com)
- [21世纪经济报道](https://21jingji.com)
- [市场监管总局](https://www.samr.gov.cn)
- [9to5Mac](https://9to5mac.com)

---

> 📌 本日报由自动化系统生成，每日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
