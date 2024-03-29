---
layout:     post 
title:      "微服务进入深水区后该何去何从"
subtitle:   "2023伊始，关于微服务最新的解读与剖析"
description: "步入 2022 年，服务网格大势所趋，Proxy Service Mesh 仍旧是主流，社区生态逐步完善，但是也存在更多 Istio 的竞争者出现。期待服务网格继续呈现百花齐放、多家争鸣的状态，持续给用户带来更大的价值，解放生产力，为全行业实现全面云原生化做出贡献。"
date:       2023-02-23 12:00:00
author:     "罗广明"
image: "/img/bg/rice-field.png"
published: true
tags:
    - 微服务
    - 微服务架构
    - 微服务拆分
    - 微服务趋势
    - 降本增效
URL: "/2023/02/23/where-to-go-when-microservices-enter-the-deep-water/"
categories: [ Tech ]    
---

2022 年，关于微服务发生了几件有趣的事情。其一，正式掌管 Twitter 不久的 Elon Musk 对 Twitter 的开发团队 “批判” 了一番。他表示自己为 Twitter 在许多国家的极慢运行速度感到抱歉。之所以如此慢是因为 App 需要执行 1000 多个 “糟糕” 的批处理 RPC，而这只是为了渲染主页的时间线。Musk 表示 “今天的部分工作将是关闭臃肿的"微服务" 。
实际上，只有不到  20% 的微服务是 Twitter 需要的。” 其二，GitHub 前 CTO Jason Warner 在社交媒体上表示：“我确信过去十年中，最大的架构错误之一就是全面使用微服务。” “任何构建过大型分布式系统的人都知道他们并不真的那样工作，但还必须适应它。”那么，微服务架构是否是一个错误，或者微服务是否已经过时了呢？

## 业务是否需要微服务

微服务的起源，最早可以追溯到 2005 年 Peter Rodgers 博士提出的 Micro-Web-Service，即将应用程序设计成细粒度的 Web 服务。2014 年，Martin Fowler 与 James Lewis 首次正式提出了微服务的概念，定义了**微服务架构是以开发一组小型服务的方式来开发一个独立的应用系统，每个服务都以一个独立进程的方式运行，每个服务与其他服务使用轻量级通信机制（RPC、HTTP）通信**。这些微服务是围绕业务功能构建的，可以采用不同的编程语言。

微服务的诞生绝非偶然，CICD & Infrastructure As Code 的出现与发展，使得基础设施管理逐步简化、功能迭代也更快速和高效，推动与促进了微服务的进一步发展和落地。

然而，微服务架构并非银弹，微服务架构给业务带来收益的同时，也会带来相应的副作用。**在合适的阶段采用微服务架构、合理决定微服务架构的拆分粒度以及恰当的微服务技术选型**是决定微服务成败的**核心**。摒弃上述三点不谈，大肆抨击微服务存在的必要性，摇旗呐喊重回单体时代的言论都是站不住脚的。仔细分析 GitHub 前 CTO  Jason Warner 的观点，你会发现，其倡导的是从单体到微服务的有序拆分和推进，并且微服务的拆分数量需要适合组织规模，Warner 鼓励企业根据自己的情况来选择，而不是盲从。这和上述倡导的观点本质上是一致的。

### 合适的阶段采用微服务架构

据观察，**几乎所有成功的微服务架构都是从一个巨大的单体架构开始的**。面对一个新的产品以及一个新的领域，很难在一开始就把业务理解清晰，往往是经过一段时间后，业务逐渐弄清楚之后，才会逐渐转型成微服务架构。此外，在物理资源和人力资源受限的情况下，采用微服务架构的风险较大，很多优势无法体现，尤其在技术选型不当时，微服务性能上的劣势反而会更加突出。

**在微服务划分之前，也应该保证公司内部的基础设施及公共基础服务已经准备完备**。可以通过监控组件和产品快速定位服务故障，可以通过工具自动化部署与管理服务，可以通过一站式开发框架降低服务开发的成本，可以通过灰度发布和泳道验证和提升服务的可用性，可以通过资源调度平台快速申请与释放资源，可以通过弹性伸缩服务快速扩展应用。

### 合理决定微服务架构的拆分粒度

微服务架构的拆分粒度应当合理，**微服务架构中的微字，并不代表粒度越小越好，也不代表越多越好，应当追求一个合理的中间值**。粒度过微，微服务的缺点将被放大，此时的微服务相对于原先的单体确实弊大于利；粒度不够，单体的缺点并未消除，微服务的优点并未凸显，也是不合理的。微服务架构的粒度拆分是一件相当复杂的事情，对于业务和团队组织架构理解不深的新人或者外部人员，根本无法判断合理的微服务拆分粒度。

随着业务的发展，组织架构的变化，团队开发人员水平的提升，**粒度随时可能发生变化，这是一个不断演进的过程**，没有绝对的对错。微服务架构的设计与微服务的拆分应当符合**康威定律**，即微服务架构需要与产生这些设计的组织架构保持一致，甚至是动态一致。

当然，仅仅熟悉业务和团队组织架构是不够的，也需要合理的微服务拆分策略。例如，**比较独立的新业务优先采用微服务架构、优先抽象通用服务、优先抽象边界比较清晰的服务、优先抽象具有独立属性的服务**。最后，建议**优先抽象核心服务**，因为微服务的运维成本较高，不是所有的地方都需要拆分，此外随着时间的推移，业务可能发生变化，而核心服务比较稳定从而不需要做较大调整。

### 恰当的微服务技术选型

决定使用微服务后，微服务相关技术选型至关重要。微服务框架可以封装、抽象分布式场景下的通用能力，例如负载均衡、服务注册发现、容错以及基本的远程通信的能力，可以让开发人员快速开发出高质量的服务。因此，在采用微服务之前，应当进行开发语言的选择以及对应的微服务框架的选型与试用。

那么该如何选择微服务框架呢？建议从**扩展性、易用性、功能丰富度以及性能**四个角度进行衡量。

* 首先是 **扩展性**，一个开源框架如果与内部能力强耦合、支持场景单一且无法进行扩展，那这个框架则很难在企业内部定制化的场景下进行落地。

* 其次是 **易用性**，业务开发者不希望关注很多框架底层细节，使用起来需要足够简单；而面向框架的二次开发者，他们需要对框架做一些定制支持，如果框架提供的扩展能力过于宽泛让扩展成本很高，或者可扩展的能力不够多，那这个框架也是存在局限性的。

* 再次是 **功能丰富度**，虽然基于扩展性可以对框架进行定制，但不是所有开发者都有足够的精力做定制开发，如果框架本身对各种扩展能力提供了不同选择的支持，对于开发者来说只需要根据自己的基础设施进行组合就能在自己的环境中运行。

* 前面三点是微服务转型初期选择微服务框架需要重点关注的指标，但随着服务规模和资源消耗变大，**性能** 就成了不容忽视的问题，从长期来看，选择框架的时候一定要关注性能，否则后续只能**面临框架替换的巨大成本问题或者被迫对这个框架做定制优化与维护**。

总的来说，微服务并非银弹，但是单体同样有很多缺陷，**微服务是在单体架构之上自然衍生发展出来的一个面向现代化与云原生的架构**，是大势所趋。只是业务需要在**合适的阶段采用微服务架构、合理决定微服务架构的拆分粒度以及进行恰当的微服务技术选型**。如果步子迈得太快，服务拆分不合理，技术选型犯了一些错误，架构需要回退到单体，这也是个别案例，但也是大家需要警惕和引以为戒的。

## 微服务进入深水区后该何去何从

微服务火了近十年，围绕微服务诞生了很多技术创新和开源项目，也有相当多的企业在内部完成了微服务的落地与推广。以字节跳动为例，近年来其微服务数量和规模迎来快速发展，2018 年，在线微服务数大约是 7000-8000，到 2021 年底，微服务数量已经突破了 10 万。企业内部的微服务数量能达到如此规模是相当少见的，但这也意味着微服务在字节得到了深度的发展，那么下一步路在何方呢？

结合字节跳动服务框架团队实践以及业界趋势，我们认为后续的微服务发展方向主要会围绕**安全、稳定性、成本优化以及微服务治理标准化**展开。

### 微服务安全

在微服务架构中，微服务的数量随着业务的分解和增长呈指数增加。由于微服务分布在不同的服务器上，因此与同一平台的单一实现相比，微服务通常会暴露出更大、更多样化的攻击面，这使得尽快发现和修复漏洞以避免问题变得更加困难。因此，**每个微服务都需要对用户的行为进行认证和许可，明确当前访问用户的身份与权限级别**。
与此同时，整个系统可能还需要对外提供一定的服务，比如第三方登录授权等。在这种情况下，如果要求每个微服务都实现各自的用户信息管理系统，既增加了开发的工作量，出错的概率也会增加，因此，**统一的认证和授权以及支持按需开启 mTLS 就显得尤其重要**。

**服务鉴定是一种基于身份标识校验请求身份合法性的微服务访问控制能力**。服务通过为具体方法或通配方法配置全局开关为开启状态，达到严格的身份鉴定的效果。为了配合合规要求，字节跳动开展了跨业务线数据访问专项治理，治理的一个先决条件就是全面落地零信任（ZTI）的服务身份，从而识别数据请求方的可信身份进一步实现细粒度访问控制来满足用户隐私合规要求，保障微服务接口安全和防止类似删库这样的误操作。

**严格授权是一种基于允许访问列表 + 不允许访问列表的微服务访问控制能力**。服务通过为具体方法或通配方法配置对上游服务的具体集群或通配集群授权，结合全局开关为开启状态，达到严格的访问控制效果。

部分 RPC 框架本身也具备严格授权能力，但不同框架对于该能力的实现是不对齐的，而且越来越难以满足业务的配置需求。字节跳动基于服务网格 ByteMesh 来实现统一的严格授权能力，这也得益于服务网格技术已经在字节跳动内部实现了全面的落地。

### 微服务稳定性

线上服务稳定性对互联网应用至关重要，稳定性差的服务将带给用户不好的使用体验，甚至给企业造成直接的经济损失。衡量服务常态稳定性一个重要指标是 SLO（Service-Level Objectives），代表服务可用水平目标。例如将服务接口的成功率 SLO 定为 99.99%，一周内低于 SLO 基线的不可用时长少于 X 小时，超过 X 小时就表示该服务稳定性不达标。
通常，微服务的治理能力，如**超时、重试、容错、限流**等能力可以满足大多数场景，提高微服务的稳定性。字节跳动内部微服务化水平高、规模大，为了做好精细化的服务治理，诞生了单实例治理与动态过载保护等一系列服务治理方案，进一步提升微服务的稳定性。

微服务化、大规模分布式部署带来了一定的运维负担，甚至有些时候，业务很难分辨问题的范畴是基础设施还是业务自身。其中，最为常见也往往不需要业务感知的问题是：极少部分（一个或几个）实例的服务能力异常导致服务 SLA 抖动。我们将这类问题统称为**单实例问题**。单实例问题的成因复杂，混杂了物理层面、业务层面等多种因素，而且几乎无法彻底根除。

为了降低单实例问题的业务感知、提升业务核心服务的 SLA，字节跳动服务框架团队基于服务网格 ByteMesh 的动态负载均衡能力构建了单实例问题抖动治理的解决方案。该方案通过收集 ByteMesh 数据面上报的 RPC 相关指标（延时、错误率等）、服务端实例的负载指标（排队时间、 CPU/MEM/IO 使用率等），动态更新服务端实例的权重，来达到服务负载更平均的效果。
该中心化控制方案在抖音电商等业务经过大规模验证，有效提高了故障识别的效率。以某一个具体服务为例，当发生单实例故障，默认配置在 1min 以内会执行服务发现降权或摘除，因此服务 SLO 不可用时长控制在 1min 以内，并且提供了单实例治理摘除大盘，可以方便排查单实例问题。

### 微服务成本优化

在云原生时代，随着微服务的不断拆分和大规模增长，**出现微服务过微是必然会面临的问题**，由此带来的额外延迟和资源消耗等缺点越发凸显。业界也出现了很多反微服务的声音，呼吁回归单体。然而单体更加不是银弹，回归单体无异于饮鸩止渴，更不符合业务发展趋势。为此，针对微服务的成本优化，字节跳动探索出了很多路径，包括但不限于**合并部署、JSON 序列化优化、开发框架开销优化**等。此外，在公司推进成本优化的背景下，服务框架团队与业务、其他基础团队促成更多的合作，力求挖掘出更多性能优化点。

#### 合并部署

字节在微服务架构之上对性能优化方案做了深入探索，探索了多种合并部署方案。虽然业界其他公司对合并部署也有过一些探索，但相关方案在编译、部署、监控、服务治理、服务隔离多个方面对现有体系的冲击较大，无法很好地支持现有体系，同时部署存在相互影响导致协作效率降低的问题。
针对这一问题，基础架构团队提出了一种新的合并部署方案，结合容器亲和性调度、流量调度计算、更高效的本地通信，让原本需要跨机的网络通信变成同机进程间调用，既能与现有体系融合又能减少微服务链路带来的性能损耗。在 QCon 2021 上，基础架构服务框架团队对外分享了《字节跳动微服务合并部署实践》，得到业界其他公司的广泛关注。
合并部署方案主要思路是结合**容器亲和性调度、流量调度计算、更高效的本地通信**，让原本需要跨机的网络通信变成**同机进程间调用**，既能与现有体系融合又能减少微服务链路带来的**性能损耗**。

以 IO 密集型测试服务为例，落地合并部署方案后，CPU 降低了 30% - 40%，延迟更加稳定，波动问题也没有了。目前合并部署已经在字节多个业务方落地，在完成性能及策略的进一步优化后，通过全局决策控制，合并部署有望在全公司范围内大规模落地。

#### JSON 序列化优化

JSON 以其简洁的语法和灵活的自描述能力，被广泛应用于各互联网业务。但是由于 JSON 本质上是一种文本协议，且没有类似 Protobuf 的强制模型约束，编解码效率往往十分低下。再加上有些业务开发者对 JSON 库的不恰当选型与使用，最终导致服务性能急剧劣化。
字节跳动也遇到了上述问题。根据此前统计的公司 CPU 占比 TOP 50 服务的性能分析数据，JSON 编解码开销总体接近 10%，单个业务占比甚至超过 40%，提升 JSON 库的性能至关重要。因此字节跳动自研了一套 JSON 高性能编解码库 sonic-go 以及适用于 C/C++ 服务的 sonic-cpp，目前均已开源在 Bytedance GitHub 组织下。

在设计 sonic-go 的过程中，团队借鉴了其他领域 / 语言的优化思想（不仅限于 JSON），将其融合到各个处理环节中。其中较为核心的技术有三块：**JIT、lazy-load 与 SIMD**。
除了上述提到的技术外，sonic 内部还有很多的细节优化，比如使用 RCU 替换 sync.Map 提升 codec cache 的加载速度，使用内存池减少 encode buffer 的内存分配等等。自 2021 年 7 月份发布以来， sonic-go 已被抖音、今日头条等诸多业务采用，累计为字节跳动节省了数十万 CPU 核。目前 sonic-go v2 正在设计研发中，预计将取得更大性能提升。

而 sonic-cpp 则在设计上整合了 rapidjson ，yyjson 和 simdjson 三者的优点，并在此基础上做进一步的优化。在实现的过程中，主要通过充分利用向量化（SIMD）指令、优化内存布局和按需解析等关键技术，使得序列化、反序列化和增删改查能达到极致的性能。sonic-cpp 在字节内部上线以来， 已为抖音、今日头条等核心业务累计节省了数十万 CPU 核心。

sonic-go 与 sonic-cpp 均兼容常见 json 库的所有接口，改造成本极低，方便存量服务的快速迁移。业务规模越大，迁移到 sonic-go 与 sonic-cpp 的业务所获得收益则更多。

#### 开发框架开销优化

对于业务来说，选择高性能的编程语言很重要，但是往往受限于研发团队的技术栈和历史背景。且语言的迁移往往成本较大，也需要很大的动力来推动。对于一些创业公司，或者对于具有一定规模的公司的新增业务线来说，**Golang 在云原生时代是最好的选择之一，其学习成本不高，对于云原生生态友好，且具有较高的性能表现**。

2014 年，Golang 被引入字节跳动，以快速解决长连接推送业务所面临的高并发问题。随后，技术团队推出了 Kite 和 Ginex （基于 Gin 的扩展）框架，这两个原始框架的推出，极大推动了 Golang 在公司内部的应用。在 Kite 和 Ginex 发布之初，由于很多功能版本过低，包括 Thrift 当时只有 v0.9.2，它们其实存在很多问题，再加上 Golang 迎来数轮大版本迭代，Kite  和 Ginex 在性能与可维护性上存在较大问题。
综上种种原因，服务框架团队正式启动了 Kite 这个字节自有 RPC 框架的重构，新的框架命名为 Kitex。这是一个自下而上的整体升级重构，围绕**性能**和**可扩展性**的诉求展开设计。类似的设计思路和底层模块也被应用在字节跳动自研 Golang HTTP 框架 Hertz 上，该项目同样具备高性能与高可扩展性。此后，Kitex 与 Hertz 进入了大规模落地的阶段，并且仍旧在围绕性能和扩展性方面持续迭代与优化。2022 年，Kitex 启动了序列化与 Thrift 专项优化，进一步提升与优化内容拷贝以及 IO 操作相关的开销。

在选择了 Golang 的前提之下，选择合适的 Golang 微服务框架同样是至关重要的。如前面所言，最合适的微服务框架应当同时具备**高可扩展性、高易用性、高性能以及内置功能足够丰富**。CloudWeGo 正是这样的开源的微服务框架与中间件集合，包含了上述字节开源的 Kitex 与 Hertz，是 Golang 领域推荐的微服务框架，也是 CNCF Landscape 推荐的微服务框架。
CloudWeGo 除了在字节内部业务大规模落地外，自 2021 年开源以来，已经在森马、华兴证券、贪玩游戏、禾多科技、沐瞳科技等数十家企业落地，基于 CloudWeGo 构建的微服务落地规模从数十个到上千个不等，上线后均获得了性能和稳定性上的收益。

## 微服务治理标准化

微服务离不开配套的治理能力，如服务可观测、全链路压测与灰度、注册发现、配置中心等，这些治理能力的实现依托于服务框架、SDK、Java Agent 以及服务网格。在这些技术的发展过程中，业界逐渐形成百花齐放的局面，产生了不同的开发语言、框架和架构，这给企业带来了繁重的维护负担以及技术选型上的困扰。而且，不同框架之间的互通也存在各类损耗和高复杂度等问题，不同的微服务开发框架及工具链，对于服务治理体系的理解和实现存在差异性，不利于微服务技术的沉淀及长期发展。终端用户必须在不同的基础设施和适当的工具之间做出艰难的抉择，才可能解决微服务架构落地过程中的各种问题，加大了企业在微服务架构落地过程中的成本。

为了解决这一难题，2022 年诞生了两套微服务治理标准化方案，面向多语言、多框架和异构基础设施，涵盖流量治理、服务容错、服务元信息治理、安全治理等关键治理领域，提供一系列的治理能力与标准、生态适配与最佳实践。

2022 年 3 月，NextArch 基金会正式宣布成立微服务 SIG，来自腾讯、字节跳动、七牛云、快手、BIGO、好未来和蓝色光标等多家企业的技术专家成为首批成员。该小组致力于推动微服务技术及其开源生态的持续发展，将面向企业在微服务生产实践中遇到的问题，针对不同行业和应用场景输出标准化解决方案，并且联合 PolarisMesh、TARS、go-zero、GoFrame、CloudWeGo 和 Spring Cloud Tencent 等开源社区提供开箱即用的实现，从而降低微服务用户的落地门槛。根据各自企业在分布式或者微服务生产实践中的经验和痛点，面向多语言、多框架和异构基础设施，针对不同行业和应用场景输出微服务落地的标准化方案，并且依托相关开源社区提供推荐实现，方便终端用户落地。

2022 年 4 月，微服务治理规范 OpenSergo 项目正式开源。OpenSergo 是开放通用的，覆盖微服务及上下游关联组件的微服务治理项目，从微服务的角度出发，涵盖流量治理、服务容错、服务元信息治理、安全治理等关键治理领域，提供一系列的治理能力与标准、生态适配与最佳实践，支持 Java, Go, Rust 等多语言生态。OpenSergo 项目由阿里巴巴、bilibili、中国移动、SphereEx 等企业，以及 Kratos、CloudWeGo、ShardingSphere、Database Mesh、Spring Cloud Alibaba、Apache Dubbo 等社区联合发起，共同主导微服务治理标准建设与能力演进。OpenSergo 的最大特点就是以统一的一套配置 /DSL/ 协议定义服务治理规则，面向多语言异构化架构，覆盖微服务框架及上下游关联组件。

整体来看，微服务治理标准尚处于早期建设阶段，从微服务治理标准定义，到控制面的实现，以及 Java/Go/C++/Rust 等多语言 SDK 与治理功能的实现，再到各个微服务生态的整合与落地，都还有大量的演进工作，尚需进一步迭代和完善。

## 总结与展望

微服务并非银弹，但也并非过时。**微服务不是香饽饽，落地微服务有一定的挑战；微服务也不是豺狼虎豹，无需避而远之**。微服务的持续高速发展，使得它已经和计算、存储、网络、数据库、安全一样成为云计算的基础设施。只不过在每个不同的发展阶段，微服务面临的挑战并不相同。
云原生普及之前，微服务开发者专注的是微服务的架构、迭代、交付和运维。随着云原生技术的成熟，微服务也在被云原生化，这时候，开发者和架构师更关心的是如何借助云的优势，简化微服务的治理与运维，并更专注在业务的**交付效率**上。高性能的服务框架选型与迁移以及微服务治理的标准化同样是微服务进入深水区需要持续探索的方向。

随着云原生和微服务的发展，服务网格应运而生，我们通常将以服务网格为核心的架构称为云原生微服务架构。云原生微服务架构具有以下四个特性：**具备弹性计算资源；具备原生微服务基础能力；服务网格统一流量调度；解决多语言 RPC 治理和升级问题**。此外，服务网格的落地能够更好地实现微服务的安全管控和稳定性治理。
然而，服务网格同样不是银弹，并不能解决所有问题。云原生微服务架构下，Sidecar 增加了系统与运维的复杂性，部分社区实现性能表现不佳还会带来显著的微服务通信时延，组件多语言 SDK 的问题仍然存在且十分严重，通用服务依赖如网关仍需显式接入等。

为了让通用能力持续下沉以及实现服务网格基础能力复用，促使云原生微服务架构逐步演进到多运行时微服务架构（Multiple-Runtime Microservices）。**多运行时微服务架构实现多语言 SDK 的进一步下沉，且提供了安全、灵活、可控的变更**。
当然，多运行时架构也存在一定的局限性，业务仍需进行改造才能接入，且运行时资源与业务资源存在竞争会引发一些较为复杂的问题。为了解决这些问题，我们希望实现**更加标准化与平台化的服务网格开发与运维能力，规范化 Sidecar 与运行时的定义，同时将运维平台变得更加标准易用**。

路漫漫其修远兮，吾将上下而求索。