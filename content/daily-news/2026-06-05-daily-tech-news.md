---
title: "2026年6月5日 每日科技早报"
date: 2026-06-05T08:00:00+08:00
categories: ["每日早报"]
tags: ["科技新闻", "人工智能", "云计算", "开源"]
description: "2026年6月5日 科技新闻摘要：英伟达开源550B Nemotron 3 Ultra、博通Q2 AI半导体收入108亿美元。"
---

## 🤖 AI前沿

**英伟达开源Nemotron 3 Ultra：550B MoE模型，专为长时运行Agent优化**

英伟达在Computex 2026上正式开源Nemotron 3 Ultra，这是其迄今为止最大的开源AI模型。该模型采用混合Transformer-Mamba MoE架构，总参数550B、激活参数55B，上下文窗口达100万token，专为长时运行的多步骤Agent工作流设计。在DeepInfra上实测推理速度达300+ tokens/秒，相比同级别开源模型快5倍、成本低30%。模型已上架Hugging Face、ModelScope、NVIDIA NIM及OpenRouter，支持SGLang、Miles等主流Agent编排框架，企业搜索服务商Glean等已宣布接入。

📖 来源：[TechFastForward](https://techfastforward.com/articles/nvidia-nemotron-3-ultra) | [HKU Space AI Hub](https://aihub.hkuspace.hku.hk/2026/06/05/nvidia-nemotron-3-ultra-now-available-on-amazon-sagemaker-jumpstart/)

**字节跳动开源Bernini视频生成与编辑模型**

字节跳动发布并开源Bernini，一个面向高保真视频生成和精准编辑的开源模型。该模型支持从文本或视觉提示合成高质量视频内容，并可对现有视频流进行时空维度的精确修改。开发者可本地部署和微调，对于受限或高安全环境具有重要价值。安全专家指出，此类强大的生成模型普及将推动AI驱动网络攻击和深度伪造的讨论。

📖 来源：[The Next Gen Tech Insider](https://www.thenextgentechinsider.com/pulse/bytedance-open-sources-bernini-video-generation-and-editing-model)

---

## 🔓 开源社区

**Go 1.26.4发布：修复crypto/x509等多个安全漏洞**

Go语言发布1.26.4版本，包含针对crypto/x509、mime和net/textproto包的安全修复，以及compiler、runtime、go fix命令和crypto/fips140包的bug修复。这是自6月2日以来的最新稳定版本，建议所有用户升级。

📖 来源：[FreeBSD Ports](https://www.freshports.org/lang/go126/)

**OpenSSH修复CVE-2026-35414认证绕过漏洞**

OpenSSH发布9.8p1安全更新，修复编号为CVE-2026-35414的认证绕过漏洞。该漏洞允许攻击者在特定条件下绕过authorized_keys限制。XCP-ng等发行版已推送安全补丁，建议所有运行OpenSSH服务器的用户尽快更新。

📖 来源：[XCP-ng Koji](https://koji.xcp-ng.org/buildinfo?buildID=5656)

---

## 💡 行业观察

**博通Q2 AI半导体收入108亿美元，Q3指引不及预期股价跌超11%**

博通公布2026财年Q2财报（截至5月3日）：总营收222亿美元（同比+48%）、AI半导体收入108亿美元（同比+143%，占营收49%）、Q3 AI收入指引160亿美元（低于市场预期的172亿美元）。尽管AI业务持续强劲增长，但全年AI芯片销售目标仍维持在1000亿美元（CEO陈福阳未上调预期），引发投资者失望。财报公布后股价盘后下跌11-14%。陈福阳表示"对定制AI加速器和网络产品的需求永不满足"，Q2获得超300亿美元AI半导体订单，是实际出货量的2.7倍。

📖 来源：[TechFastForward](https://techfastforward.com/articles/broadcom-ai-revenue-doubles-to-108b-as-orders-surge) | [上海证券报](http://www.cnstock.com/commonDetail/724737)

---

## 📚 数据来源

- [TechFastForward](https://techfastforward.com/)
- [HKU Space AI Hub](https://aihub.hkuspace.hku.hk/)
- [FreeBSD Ports](https://www.freshports.org/)
- [上海证券报](http://www.cnstock.com/)
- [The Next Gen Tech Insider](https://www.thenextgentechinsider.com/)

---

> 📌 本日报由自动化系统生成，每日工作日早上推送至 [Guangming's Blog](https://guangmingluo.github.io/)
