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
| [[01-线性DP\|线性 DP]] | 核心 | 8 | 8 |
| [[01-01背包与完全背包\|01 背包]] | 核心 | 5 | 5 |
| [[01-01背包与完全背包\|完全背包]] | 核心 | 4 | 4 |
| [[02-多重背包\|多重背包]] | 重要 | 4 | 4 |
| [[03-分组与混合背包\|分组与混合背包]] | 重要 | 5 | 5 |
| [[04-多维与依赖背包\|多维与依赖背包]] | 重要 | 4 | 4 |
| [[05-计数与方案\|计数与方案]] | 核心 | 5 | 5 |
| [[03-区间DP\|区间 DP]] | 重要 | 6 | 6 |
| [[04-序列DP\|序列 DP]] | 核心 | 8 | 8 |
| [[05-树形与图DP\|树形 DP]] | 重要 | 4 | 4 |
| [[05-树形与图DP\|图上 DP]] | 重要 | 4 | 4 |
| [[06-状态压缩DP\|状态压缩 DP]] | 重要 | 6 | 6 |
| [[07-数位DP\|数位 DP]] | 专项 | 5 | 5 |
| [[08-DP优化\|DP 优化]] | 进阶核心 | 8 | 8 |

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

- [[1195C-Basketball-Exercise|1195C Basketball Exercise]]
- [[698A-Vacations|698A Vacations]]
- [[455A-Boredom|455A Boredom]]
- [[706C-Hard-problem|706C Hard problem]]
- [[431C-k-Tree|431C k-Tree]]
- [[118D-Caesar-s-Legions|118D Caesar's Legions]]
- [[474D-Flowers|474D Flowers]]
- [[977F-Consecutive-Subsequence|977F Consecutive Subsequence]]

## 01 背包

- [[1633D-Make-Them-Equal|1633D Make Them Equal]]
- [[366C-Dima-and-Salad|366C Dima and Salad]]
- [[577B-Modulo-Sum|577B Modulo Sum]]
- [[478D-Red-Green-Towers|478D Red-Green Towers]]
- [[864E-Fire|864E Fire]]

## 完全背包

- [[189A-Cut-Ribbon|189A Cut Ribbon]]
- [[1934B-Yet-Another-Coin-Problem|1934B Yet Another Coin Problem]]
- [[1716D-Chip-Move|1716D Chip Move]]
- [[283C-Coin-Troubles|283C Coin Troubles]]

## 多重背包

- [[106C-Buns|106C Buns]]
- [[922E-Birds|922E Birds]]
- [[1132E-Knapsack|1132E Knapsack]]
- [[95E-Lucky-Country|95E Lucky Country]]

## 分组与混合背包

- [[741B-Arpa-s-weak-amphitheater-and-Mehrdad-s-valuable-Hoses|741B Arpa's weak amphitheater and Mehrdad's valuable Hoses]]
- [[106C-Buns|106C Buns]]
- [[148E-Porcelain|148E Porcelain]]
- [[2000F-Color-Rows-and-Columns|2000F Color Rows and Columns]]
- [[999F-Cards-and-Joy|999F Cards and Joy]]

## 多维与依赖背包

- [[543A-Writing-Code|543A Writing Code]]
- [[687C-The-Values-You-Can-Make|687C The Values You Can Make]]
- [[837D-Round-Subset|837D Round Subset]]
- [[815C-Karen-and-Supermarket|815C Karen and Supermarket]]

## 计数与方案

- [[431C-k-Tree|431C k-Tree]]
- [[474D-Flowers|474D Flowers]]
- [[543A-Writing-Code|543A Writing Code]]
- [[478D-Red-Green-Towers|478D Red-Green Towers]]
- [[864E-Fire|864E Fire]]

## 区间 DP

- [[245H-Queries-for-Number-of-Palindromes|245H Queries for Number of Palindromes]]
- [[607B-Zuma|607B Zuma]]
- [[1114D-Flood-Fill|1114D Flood Fill]]
- [[1132F-Clear-the-String|1132F Clear the String]]
- [[598E-Chocolate-Bar|598E Chocolate Bar]]
- [[1178F1-Short-Colorful-Strip|1178F1 Short Colorful Strip]]

## 序列 DP

- [[1195C-Basketball-Exercise|1195C Basketball Exercise]]
- [[706C-Hard-problem|706C Hard problem]]
- [[977F-Consecutive-Subsequence|977F Consecutive Subsequence]]
- [[4D-Mysterious-Present|4D Mysterious Present]]
- [[467C-George-and-Job|467C George and Job]]
- [[1183E-Subsequences-easy-version|1183E Subsequences (easy version)]]
- [[1409F-Subsequences-of-Length-Two|1409F Subsequences of Length Two]]
- [[10D-LCIS|10D LCIS]]

## 树形 DP

- [[274B-Zero-Tree|274B Zero Tree]]
- [[1092F-Tree-with-Maximum-Cost|1092F Tree with Maximum Cost]]
- [[461B-Appleman-and-Tree|461B Appleman and Tree]]
- [[543D-Road-Improvement|543D Road Improvement]]

## 图上 DP

- [[919D-Substring|919D Substring]]
- [[721C-Journey|721C Journey]]
- [[459E-Pashmak-and-Graph|459E Pashmak and Graph]]
- [[960F-Pathwalks|960F Pathwalks]]

## 状态压缩 DP

- [[580D-Kefa-and-Dishes|580D Kefa and Dishes]]
- [[16E-Fish|16E Fish]]
- [[8C-Looking-for-Order|8C Looking for Order]]
- [[401D-Roman-and-Numbers|401D Roman and Numbers]]
- [[453B-Little-Pony-and-Harmony-Chest|453B Little Pony and Harmony Chest]]
- [[895C-Square-Subsets|895C Square Subsets]]

## 数位 DP

- [[1036C-Classy-Numbers|1036C Classy Numbers]]
- [[855E-Salazar-Slytherin-s-Locket|855E Salazar Slytherin's Locket]]
- [[628D-Magic-Numbers|628D Magic Numbers]]
- [[1073E-Segment-Sum|1073E Segment Sum]]
- [[55D-Beautiful-numbers|55D Beautiful numbers]]

## DP 优化

- [[1856E1-PermuTree-easy-version|1856E1 PermuTree (easy version)]]
- [[319C-Kalila-and-Dimna-in-the-Logging-Industry|319C Kalila and Dimna in the Logging Industry]]
- [[372C-Watching-Fireworks-is-Fun|372C Watching Fireworks is Fun]]
- [[833B-The-Bakery|833B The Bakery]]
- [[95E-Lucky-Country|95E Lucky Country]]
- [[868F-Yet-Another-Minimization-Problem|868F Yet Another Minimization Problem]]
- [[321E-Ciel-and-Gondolas|321E Ciel and Gondolas]]
- [[631E-Product-Sum|631E Product Sum]]
