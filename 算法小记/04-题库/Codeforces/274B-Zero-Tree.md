---
type: problem
platform: Codeforces
problem_id: 274B
title: Zero Tree
rating: 1800
tags: [dfs and similar, dp, greedy, trees]
status: todo
priority: important
concepts: [树形与图DP, 贪心]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 274B Zero Tree

> [Codeforces 274B - Zero Tree](https://codeforces.com/problemset/problem/274/B)

## 题意摘要

给定一棵以 $1$ 为根、$n$ 个点的树，第 $i$ 个点有权值 $a_i$。每次操作可以选一棵连通且包含根节点 $1$ 的子树，把其中所有点的权值同时 $+1$ 或同时 $-1$。求把所有点权值都变成 $0$ 的最少操作次数。

## 识别信号

- 每次操作都作用于"包含根的一段连通块"，方向从根往下传播，适合自底向上统计每个点需要多少次加法、多少次减法。
- 一个点的 +1 次数必须不少于它每个孩子的 +1 次数（孩子的每一次加操作都能顺带覆盖到它），所以合并方式是取最大值而不是求和。
- 目标是把所有值归零，加减两种操作可以互相抵消，需要在合并后按当前点的剩余值补足差距。

## 状态与转移

对每个点 u 维护两个量：`inc[u]` 表示覆盖 u 的 +1 操作次数，`dec[u]` 表示覆盖 u 的 -1 操作次数。自底向上（DFS 后序）合并：

```text
inc[u] = max(inc[v])   // v 取遍 u 的所有孩子，叶子为 0
dec[u] = max(dec[v])
val = a[u] + inc[u] - dec[u]
若 val > 0：dec[u] += val     // 还多出正数，补减操作
若 val < 0：inc[u] += -val    // 还多出负数，补加操作
```

- 每一步操作作用于包含根的连通块，因此父亲的操作次数一定是孩子的上界，取 max 恰好表达"和孩子共用操作"。
- 合并孩子之后 u 的值变成 `a[u] + inc[u] - dec[u]`，不为 0 就只能对"以 u 为最上端的连通块"单独补操作，缺多少补多少。
- 叶子没有孩子，`inc = dec = 0`，此时 val = a[leaf]，直接补足。

边界：答案是 `inc[1] + dec[1]`。权值可能很大，累加结果要用 64 位整数。

树上自底向上的合并见 [[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 复杂度

- 时间：O(n)，每个点只处理一次。
- 空间：O(n)，递归 DFS 需要额外 O(n) 栈空间，必要时应改为显式栈或按拓扑序迭代。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
