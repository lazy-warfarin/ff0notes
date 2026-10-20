---
type: problem
platform: Codeforces
problem_id: 455A
title: Boredom
rating: 1500
tags: [dp]
status: solved
priority: core
concepts: [线性DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf455a_boredom/main.rs
first_solved: 2026-10-11
last_review: 2026-10-11
next_review: 2026-10-18
failure_reason:
---

# 455A Boredom

> [Codeforces 455A - Boredom](https://codeforces.com/problemset/problem/455/A)

## 题意摘要

给出 $n$ 个整数 $a_i$（$1 \le n \le 10^5$，$1 \le a_i \le 10^5$）。每一步选择一个值等于 $x$ 的元素并删除它，获得 $x$ 分；这一步同时删除所有值等于 $x-1$ 和 $x+1$ 的元素。值为 $x$ 的其他元素不受影响，可以继续选择。求能获得的最大分数。

## 识别信号

- 选择只和数值有关，和原数组顺序无关。
- 取了一个值就禁止相邻的值，这正是打家劫舍的相邻约束。
- 值域不大（10^5），适合在值域上线性 DP，而不是在位置上下标。

## 状态与转移

令 `cnt[x]` 表示值 x 出现的次数，`f[i]` 表示只考虑值 `1..i` 时的最大分数。

```text
f[i] = max(f[i - 1], f[i - 2] + i * cnt[i])
```

- `f[i - 1]`：不选值 i。
- `f[i - 2] + i * cnt[i]`：选定值 i，把它的 cnt[i] 个元素逐个取完，共得 i * cnt[i] 分；第一次取 i 时值 i-1 和 i+1 就已经被删除，所以相邻的值不能再取。

边界：`f[0] = 0`，`f[1] = cnt[1]`。

## 复杂度

- 时间：O(n + maxA)。
- 空间：O(maxA)，滚动两个变量后为 O(1)。

## Rust 实现

- [examples/cf455a_boredom/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf455a_boredom/main.rs)
- 值域 DP，`marr[i]` 原地滚动，时间 O(n + maxA)，已通过官方三组样例。

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
