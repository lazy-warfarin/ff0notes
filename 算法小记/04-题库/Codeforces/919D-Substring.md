---
type: problem
platform: Codeforces
problem_id: 919D
title: Substring
rating: 1700
tags: [dfs and similar, dp, graphs]
status: todo
priority: core
concepts: [树形与图DP, 拓扑排序]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 919D Substring

> [Codeforces 919D - Substring](https://codeforces.com/problemset/problem/919/D)

## 题意摘要

给出 $n$ 个点、$m$ 条边的有向图，每个点上写有一个小写字母（$n, m \le 3 \times 10^5$）。一条路径的价值定义为该路径上出现次数最多的字母的出现次数。求所有路径价值的最大值；如果存在环，路径可以无限走，答案无界，输出 $-1$。

## 识别信号

- 路径价值只和 26 个字母各自的计数有关，"取最大值"这一步可以拆成 26 个互不干扰的计数问题。
- 有向图上沿着边走，后继依赖前驱，提示按拓扑序递推；有环即答案无界。
- 状态只需要"以某个点为终点"的信息，不需要记录整条路径的形态。

## 状态与转移

令 `dp[u][c]` 表示在所有以 u 为终点的路径中，字母 c 最多出现多少次。

```text
拓扑排序，按顺序取出 u：
  对每条边 u -> v：
    for c in 'a'..'z':
      dp[v][c] = max(dp[v][c], dp[u][c] + (letter[v] == c))
```

- 初始化 `dp[u][c] = 1`（当 `letter[u] == c`），否则为 0，表示路径只有 u 一个点。
- 每条边把"以 u 结尾的最优计数"推给 v；拓扑序保证处理 v 之前，所有能到达 v 的点都已经算完。
- 拓扑排序结束后仍有入度不为 0 的点，说明图中有环，直接输出 -1。

边界：n >= 1，单点路径也算路径，因此答案至少为 1。答案是所有 `dp[u][c]` 的最大值。

有向图上的顺序递推见 [[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 复杂度

- 时间：O((n + m) * 26)。
- 空间：O(n * 26)，用 `Vec<[i32; 26]>` 或展平成一维数组。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
