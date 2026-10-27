---
type: problem
platform: Codeforces
problem_id: 1579E2
title: Array Optimization by Deque
rating: 1700
tags: [data structures, greedy]
status: todo
priority: core
concepts: [红黑树, 顺序统计, 逆序对, 贪心]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1579E2 Array Optimization by Deque

> [Codeforces 1579E2 - Array Optimization by Deque](https://codeforces.com/problemset/problem/1579/E2)
>
> 元数据核对：2026-10-26，title / rating / tags 来自 [Codeforces 官方 problemset API](https://codeforces.com/api/problemset.problems)，题意和约束按官方题面核对。作为手写红黑树的接口练习，不代表官方指定这一实现。

## 题意摘要

按原顺序处理数组，每次把当前元素放到双端队列的队首或队尾，求处理完所有元素后逆序对数量的最小值。逆序对要求严格大于，相等元素不构成逆序对。

多组测试，$1\le n\le2\cdot10^5$、$-10^9\le a_i\le10^9$，所有测试的 $n$ 之和不超过 $2\cdot10^5$。

## 识别信号

- 当前元素只会与已经处理过的元素新增逆序对；之前元素的相对顺序不再改变。
- 只需要“之前有多少个值严格小于 / 严格大于当前值”，不需要真的维护双端队列。
- 属于基础 `RbTree` 之后的**多重集合与顺序统计扩展**：本题只需 `insert`、`rank`、`upper_rank` 与计重总数，不用删除或前驱后继；这不代表第一版就要实现排名。
- 值域较大且有重复；可以用带 `cnt + size` 的红黑树，也可以离散化后使用树状数组。

关联笔记：[[02-数据结构/树/01-红黑树|红黑树：插入与顺序统计]]。

## 状态与转移

设已处理元素的多重集合为 $S$，大小为 $m$，当前值为 $x$。按知识点笔记的接口语义：

$$
L=\operatorname{rank}(x)=\#\{v\in S:v<x\},\qquad
G=m-\operatorname{upper\_rank}(x)=\#\{v\in S:v>x\}.
$$

- 放队首新增 $L$ 个逆序对；放队尾新增 $G$ 个。
- 累加 $\min(L,G)$，再把 $x$ 插入树中。
- 每次选择不影响后续看到的历史元素多重集合；后续新增代价只取决于这个多重集合，因此可以逐项独立取较小值。

必须先查询再插入。重复值只增加 `cnt`；`size` 和排名都按重数计数。

## 复杂度

设一组中不同值数为 $d$：总时间 $O(n\log(d+1))$，树的存储空间 $O(d)$；另计输入缓冲。答案使用 `i64` 或 `u64`，不能用 32 位整数累加。

## Rust 实现

- 尚未实现，`code_path` 留空；本次不创建 Rust 源文件。
- 先完成基础 `RbTree` 的结构与插入、删除修复，再扩展为带 `cnt + size` 的 `RbMultiset`；这道题只调用扩展版的插入和排名接口。不要为了本题把排名维护混进第一版。
- 不使用 `BTreeSet::iter().filter(...).count()` 代替正式排名查询；那会遍历元素。
- 调试时用排序 `Vec` 统计严格大小关系，每一步检查根颜色、红红冲突、黑高与 `size`。

## 复盘

- 第一次错误：待完成后记录。
- 关键边界：全相等时答案为 $0$；纯递增或纯递减也可以得到 $0$；重复元素不能计入严格大小关系；多组测试必须重置树。
- 一句话总结：用历史元素的严格排名计算队首 / 队尾两种新增代价，逐项取最小。
