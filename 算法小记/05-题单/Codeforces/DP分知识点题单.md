---
type: problem-set
platform: Codeforces
topic: 动态规划
---

# Codeforces DP 分知识点题单

只收录 Codeforces。按现有知识点章节和独立基础模型分配练习，不把所有章节机械设为同样题量；每个训练单元至少 4 道不同题。

## 题量安排

| 知识点 | 重要程度 | 目标题量 | 已配题量 |
| --- | --- | --- | --- |
| [[03-算法/动态规划/01-线性DP\|线性 DP]] | 核心 | 8 | 8 |
| [[03-算法/动态规划/02-背包DP/01-01背包与完全背包\|01 背包]] | 核心 | 5 | 5 |
| [[03-算法/动态规划/02-背包DP/01-01背包与完全背包\|完全背包]] | 核心 | 4 | 4 |
| [[03-算法/动态规划/02-背包DP/02-多重背包\|多重背包]] | 重要 | 4 | 4 |
| [[03-算法/动态规划/02-背包DP/03-分组与混合背包\|分组与混合背包]] | 重要 | 5 | 5 |
| [[03-算法/动态规划/02-背包DP/04-多维与依赖背包\|多维与依赖背包]] | 重要 | 4 | 4 |
| [[03-算法/动态规划/02-背包DP/05-计数与方案\|计数与方案]] | 核心 | 5 | 5 |
| [[03-算法/动态规划/03-区间DP\|区间 DP]] | 重要 | 6 | 6 |
| [[03-算法/动态规划/04-序列DP\|序列 DP]] | 核心 | 8 | 8 |
| [[03-算法/动态规划/05-树形与图DP\|树形 DP]] | 重要 | 4 | 4 |
| [[03-算法/动态规划/05-树形与图DP\|图上 DP]] | 重要 | 4 | 4 |
| [[03-算法/动态规划/06-状态压缩DP\|状态压缩 DP]] | 重要 | 6 | 6 |
| [[03-算法/动态规划/07-数位DP\|数位 DP]] | 专项 | 5 | 5 |
| [[03-算法/动态规划/08-DP优化\|DP 优化]] | 进阶核心 | 8 | 8 |

共 14 个训练单元、76 个章节练习入口，跨组去重后 66 道题。一个单元内按题号去重；455B 等旁支对照不计入状压覆盖量；同题的 Div.1/Div.2 对应版本或 easy/hard 版不重复凑数。

## 练习规则

- 线性、序列、优化是高频内容，配 8 题；区间、状压配 6 题；计数与方案、分组与混合各 5 题；专项至少 4 题。
- 01 背包与完全背包分别计数；树形和图上 DP 分别计数。其余复合页面按原章节配额，具体题型范围见下节，不能据此声称每个更细的子模型都已有 4 道。
- 组内按建模入门到综合应用排序，不要求 rating 严格递增。优先级 `core/important/challenge` 表示学习安排，不是题号字母或官方难度分级。
- 原有 solved 状态、代码路径和复习日期全部保留，新题均为 todo；已完成题可以复习，不会自动算作一次新的通过。
- 先独立做题，再展开新卡片中的折叠建模提示。重复出现在不同章节的题，复习时重点解释当前章节对应的状态或转移。
- 后续随薄弱点增减配额，但任何单元不能降到 4 道以下；每次修改同步笔记、总题单和状态看板，运行 `node 算法小记/scripts/check-dp-practice.mjs` 复核。
- 新增卡片的 title、rating、tags 已于 2026-10-23 从官方 API 补充核对（1934B、283C、1716D），此前卡片于 2026-10-22 核对；题意按官方页面核对，rating 以后可能变化。

## 复合模型边界

- 01 与完全：01 背包只留 5 道；837D 是二维 01，只在多维页列。完全背包的 189A 是纯模板，1934B 是大容量硬币找零（按 15 周期调整），1716D 是按步数分层的完全背包式计数，283C 是完全背包加“严格大于”链约束；431C、474D 是容量外层的**有序计数**，只在计数页列，不要套完全背包的物品外层组合计数模板。
- 多重背包：106C 是混合（有馅有界 + 无馅完全）；1132E 是小重量大库存；95E 是连通块大小频次；922E 是有限库存加动态法力上限，属于扩展，不冒充普通多重模板；1856E1 是树形迁移，只在 DP 优化页列。
- 分组与混合：741B、148E、999F、2000F 练组内合法选项；106C 是混合代表；922E 只在多重页列，不算分组/混合。
- 多维与依赖：543A、687C、837D 练多维状态，815C 练树形优惠券依赖；这是 3+1，不等于两个子模型各有 4 题；815C 依赖的是优惠券而不是商品购买本身。
- 计数与方案：431C、474D、543A、478D 练计数，864E 练背包方案还原；4D、8C、453B 是 LIS/状压的还原练习，只在序列/状压页列，不标成背包。
- 图上 DP：919D、721C 的原图需要按拓扑依赖处理；459E、960F 的原图可有环，无环的是边权或输入顺序上的状态依赖。
- 优化：1856E1、95E 练按频次压缩或有界转移；319C、631E 练凸包查询；372C 练单调队列；833B、868F、321E 练分治及代价维护。631E 是同类线性表达式优化的迁移题。

## 线性 DP

- [[04-题库/Codeforces/1195C-Basketball-Exercise|1195C Basketball Exercise]]
- [[04-题库/Codeforces/698A-Vacations|698A Vacations]]
- [[04-题库/Codeforces/455A-Boredom|455A Boredom]]
- [[04-题库/Codeforces/706C-Hard-problem|706C Hard problem]]
- [[04-题库/Codeforces/431C-k-Tree|431C k-Tree]]
- [[04-题库/Codeforces/118D-Caesar-s-Legions|118D Caesar's Legions]]
- [[04-题库/Codeforces/474D-Flowers|474D Flowers]]
- [[04-题库/Codeforces/977F-Consecutive-Subsequence|977F Consecutive Subsequence]]

## 01 背包

- [[04-题库/Codeforces/1633D-Make-Them-Equal|1633D Make Them Equal]]
- [[04-题库/Codeforces/366C-Dima-and-Salad|366C Dima and Salad]]
- [[04-题库/Codeforces/577B-Modulo-Sum|577B Modulo Sum]]
- [[04-题库/Codeforces/478D-Red-Green-Towers|478D Red-Green Towers]]
- [[04-题库/Codeforces/864E-Fire|864E Fire]]

## 完全背包

- [[04-题库/Codeforces/189A-Cut-Ribbon|189A Cut Ribbon]]
- [[04-题库/Codeforces/1934B-Yet-Another-Coin-Problem|1934B Yet Another Coin Problem]]
- [[04-题库/Codeforces/1716D-Chip-Move|1716D Chip Move]]
- [[04-题库/Codeforces/283C-Coin-Troubles|283C Coin Troubles]]

## 多重背包

- [[04-题库/Codeforces/106C-Buns|106C Buns]]
- [[04-题库/Codeforces/922E-Birds|922E Birds]]
- [[04-题库/Codeforces/1132E-Knapsack|1132E Knapsack]]
- [[04-题库/Codeforces/95E-Lucky-Country|95E Lucky Country]]

## 分组与混合背包

- [[04-题库/Codeforces/741B-Arpa-s-weak-amphitheater-and-Mehrdad-s-valuable-Hoses|741B Arpa's weak amphitheater and Mehrdad's valuable Hoses]]
- [[04-题库/Codeforces/106C-Buns|106C Buns]]
- [[04-题库/Codeforces/148E-Porcelain|148E Porcelain]]
- [[04-题库/Codeforces/2000F-Color-Rows-and-Columns|2000F Color Rows and Columns]]
- [[04-题库/Codeforces/999F-Cards-and-Joy|999F Cards and Joy]]

## 多维与依赖背包

- [[04-题库/Codeforces/543A-Writing-Code|543A Writing Code]]
- [[04-题库/Codeforces/687C-The-Values-You-Can-Make|687C The Values You Can Make]]
- [[04-题库/Codeforces/837D-Round-Subset|837D Round Subset]]
- [[04-题库/Codeforces/815C-Karen-and-Supermarket|815C Karen and Supermarket]]

## 计数与方案

- [[04-题库/Codeforces/431C-k-Tree|431C k-Tree]]
- [[04-题库/Codeforces/474D-Flowers|474D Flowers]]
- [[04-题库/Codeforces/543A-Writing-Code|543A Writing Code]]
- [[04-题库/Codeforces/478D-Red-Green-Towers|478D Red-Green Towers]]
- [[04-题库/Codeforces/864E-Fire|864E Fire]]

## 区间 DP

- [[04-题库/Codeforces/245H-Queries-for-Number-of-Palindromes|245H Queries for Number of Palindromes]]
- [[04-题库/Codeforces/607B-Zuma|607B Zuma]]
- [[04-题库/Codeforces/1114D-Flood-Fill|1114D Flood Fill]]
- [[04-题库/Codeforces/1132F-Clear-the-String|1132F Clear the String]]
- [[04-题库/Codeforces/598E-Chocolate-Bar|598E Chocolate Bar]]
- [[04-题库/Codeforces/1178F1-Short-Colorful-Strip|1178F1 Short Colorful Strip]]

## 序列 DP

- [[04-题库/Codeforces/1195C-Basketball-Exercise|1195C Basketball Exercise]]
- [[04-题库/Codeforces/706C-Hard-problem|706C Hard problem]]
- [[04-题库/Codeforces/977F-Consecutive-Subsequence|977F Consecutive Subsequence]]
- [[04-题库/Codeforces/4D-Mysterious-Present|4D Mysterious Present]]
- [[04-题库/Codeforces/467C-George-and-Job|467C George and Job]]
- [[04-题库/Codeforces/1183E-Subsequences-easy-version|1183E Subsequences (easy version)]]
- [[04-题库/Codeforces/1409F-Subsequences-of-Length-Two|1409F Subsequences of Length Two]]
- [[04-题库/Codeforces/10D-LCIS|10D LCIS]]

## 树形 DP

- [[04-题库/Codeforces/274B-Zero-Tree|274B Zero Tree]]
- [[04-题库/Codeforces/1092F-Tree-with-Maximum-Cost|1092F Tree with Maximum Cost]]
- [[04-题库/Codeforces/461B-Appleman-and-Tree|461B Appleman and Tree]]
- [[04-题库/Codeforces/543D-Road-Improvement|543D Road Improvement]]

## 图上 DP

- [[04-题库/Codeforces/919D-Substring|919D Substring]]
- [[04-题库/Codeforces/721C-Journey|721C Journey]]
- [[04-题库/Codeforces/459E-Pashmak-and-Graph|459E Pashmak and Graph]]
- [[04-题库/Codeforces/960F-Pathwalks|960F Pathwalks]]

## 状态压缩 DP

- [[04-题库/Codeforces/580D-Kefa-and-Dishes|580D Kefa and Dishes]]
- [[04-题库/Codeforces/16E-Fish|16E Fish]]
- [[04-题库/Codeforces/8C-Looking-for-Order|8C Looking for Order]]
- [[04-题库/Codeforces/401D-Roman-and-Numbers|401D Roman and Numbers]]
- [[04-题库/Codeforces/453B-Little-Pony-and-Harmony-Chest|453B Little Pony and Harmony Chest]]
- [[04-题库/Codeforces/895C-Square-Subsets|895C Square Subsets]]

## 数位 DP

- [[04-题库/Codeforces/1036C-Classy-Numbers|1036C Classy Numbers]]
- [[04-题库/Codeforces/855E-Salazar-Slytherin-s-Locket|855E Salazar Slytherin's Locket]]
- [[04-题库/Codeforces/628D-Magic-Numbers|628D Magic Numbers]]
- [[04-题库/Codeforces/1073E-Segment-Sum|1073E Segment Sum]]
- [[04-题库/Codeforces/55D-Beautiful-numbers|55D Beautiful numbers]]

## DP 优化

- [[04-题库/Codeforces/1856E1-PermuTree-easy-version|1856E1 PermuTree (easy version)]]
- [[04-题库/Codeforces/319C-Kalila-and-Dimna-in-the-Logging-Industry|319C Kalila and Dimna in the Logging Industry]]
- [[04-题库/Codeforces/372C-Watching-Fireworks-is-Fun|372C Watching Fireworks is Fun]]
- [[04-题库/Codeforces/833B-The-Bakery|833B The Bakery]]
- [[04-题库/Codeforces/95E-Lucky-Country|95E Lucky Country]]
- [[04-题库/Codeforces/868F-Yet-Another-Minimization-Problem|868F Yet Another Minimization Problem]]
- [[04-题库/Codeforces/321E-Ciel-and-Gondolas|321E Ciel and Gondolas]]
- [[04-题库/Codeforces/631E-Product-Sum|631E Product Sum]]
