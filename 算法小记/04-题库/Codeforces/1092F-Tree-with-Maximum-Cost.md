---
type: problem
platform: Codeforces
problem_id: 1092F
title: Tree with Maximum Cost
rating: 1900
tags: [dfs and similar, dp, trees]
status: todo
priority: important
concepts: [树形与图DP, 换根DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1092F Tree with Maximum Cost

> [Codeforces 1092F - Tree with Maximum Cost](https://codeforces.com/problemset/problem/1092/F)

## 题意摘要

给出一棵 $n$ 个点的树，第 $i$ 个点有权值 $a_i$。定义 $f(x)$ 为所有点的权值乘以“该点到 $x$ 的距离”之和，即 $f(x)=\sum_i a_i \cdot \operatorname{dist}(i,x)$。求 $f(x)$ 的最大值。

## 识别信号

- 对每个点都算一次显然是 O(n^2)，但相邻两个点的 f 值只差一个可以整体计算的量，提示换根 DP。
- 第一次 DFS 用来求"从根出发的答案"和子树权值和；第二次 DFS 把根沿着边平移，用 O(1) 更新得到新根的答案。
- 指标是"到所有点的距离加权和"，只与子树权值和有关，不需要重新遍历整棵树。

## 状态与转移

第一次 DFS（后序）求出 `sub[u]`：以 1 为根时子树 u 的权值和；同时得到 `f[1] = sum(a[i] * dist(1, i))`。

第二次 DFS 做换根，把答案从父亲 u 推到孩子 v：

```text
sub[u]  = a[u] + sum(sub[v])           // v 取遍 u 的孩子
f[1]    = sum(a[i] * dist(1, i))       // 第一次 DFS 顺带累加
f[v]    = f[u] + total - 2 * sub[v]    // total = sum(a[i])
```

- 从 u 走到 v 时，v 子树内的点距离全部减少 1，其余点距离全部增加 1。
- 所以变化量是 `(total - sub[v]) - sub[v] = total - 2 * sub[v]`，无需重新计算距离。
- 答案在两次 DFS 过程中对 `f[x]` 取最大值即可。

边界：n = 1 时答案为 0。`total`、`sub`、`f` 都是加权和，可能超过 32 位，统一用 64 位整数。

换根（二次扫描）是树形 DP 的常见套路，见 [[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 复杂度

- 时间：O(n)，两次 DFS。
- 空间：O(n)，存图和 dp 数组。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
