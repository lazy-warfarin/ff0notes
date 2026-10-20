---
type: problem
platform: Codeforces
problem_id: 698A
title: Vacations
rating: 1400
tags: [dp]
status: solved
priority: core
concepts: [线性DP, 状态机DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf698a_vacations/main.rs
first_solved: 2026-10-12
last_review: 2026-10-12
next_review: 2026-10-19
failure_reason:
---

# 698A Vacations

> [Codeforces 698A - Vacations](https://codeforces.com/problemset/problem/698/A)

## 题意摘要

Vasya 有 $n$ 天假期（$n \le 100$），每天给出 $a_i$：$0$ 表示健身房关闭且没有比赛，$1$ 表示有比赛，$2$ 表示健身房开放，$3$ 表示两者都有。每天他可以选择休息、参加比赛（当天有比赛时）或锻炼（健身房开放时），但不允许连续两天做同一件事（不会连续两天比赛，也不会连续两天锻炼）。求最少需要休息多少天。

## 识别信号

- 每天只有"休息 / 比赛 / 锻炼"三种选择，限制只存在于相邻两天之间，是典型的状态机线性 DP。
- 目标是最小化休息天数，可以把休息记作代价 1，其余选择代价 0，等价于求最小代价路径。
- 某些天某种选择不可用（由 a_i 决定），不可用状态用 +∞ 表示。

## 状态与转移

令 `dp[i][0/1/2]` 表示考虑前 i 天、第 i 天分别（0）休息、（1）比赛、（2）锻炼时，前 i 天的最少休息天数。

```text
dp[i][0] = 1 + min(dp[i-1][0], dp[i-1][1], dp[i-1][2])
dp[i][1] = min(dp[i-1][0], dp[i-1][2])        // 仅当 a[i] ∈ {1, 3}
dp[i][2] = min(dp[i-1][0], dp[i-1][1])        // 仅当 a[i] ∈ {2, 3}
```

- dp[i][0]：今天休息，前一天做什么都行。
- dp[i][1] / dp[i][2]：不能从"前一天做同一件事"转移过来，这正是题目禁止连续同活动的约束。
- 当天不具备某活动的条件时，对应状态保持 +∞。

边界：`dp[0][0] = 0`，`dp[0][1] = dp[0][2] = +∞`。按 i 从小到大遍历，答案是 `min(dp[n][0], dp[n][1], dp[n][2])`。

本题属于 [[03-算法/动态规划/01-线性DP|线性DP]] 中的多状态（状态机）模型。

## 复杂度

- 时间：O(n)。
- 空间：O(n)，三个状态滚动更新后为 O(1)。

## Rust 实现

- [examples/cf698a_vacations/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf698a_vacations/main.rs)
- 状态机 DP：`dp1/dp2` 分别表示前 i 天中「第 i 天不健身 / 不比赛」时的最大活动天数，答案 `n - max(dp1[n], dp2[n])`，与上方最小休息模型等价；已通过官方三组样例。

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
