---
type: problem
platform: Codeforces
problem_id: 474D
title: Flowers
rating: 1700
tags: [dp]
status: solved
priority: core
concepts: [线性DP, 前缀和]
code_path: D:/projects/Rust/algorithm-notes/examples/cf474d_flowers/main.rs
first_solved: 2026-10-12
last_review: 2026-10-12
next_review: 2026-10-19
failure_reason: 首次提交对每个 [a,b] 区间逐项求和，查询总复杂度过高导致超时；改为预处理前缀和。
---

# 474D Flowers

> [Codeforces 474D - Flowers](https://codeforces.com/problemset/problem/474/D)

## 题意摘要

一顿晚餐可以表示成一串红花和白花，规则是白花必须每 $k$ 朵为一组地吃。给出 $t$ 组询问 $(a, b)$，求长度在 $a$ 到 $b$ 之间（含端点）的合法花串数量之和，对 $10^9+7$ 取模（$t, k \le 10^5$，$a \le b \le 10^5$）。

## 识别信号

- 只需要按长度递推合法串数量，具体内容不重要，转移只看串尾，是线性 DP。
- 递推形如 f[i] = f[i-1] + f[i-k]，即"结尾是红花"或"结尾是 k 朵白花"，天然适合 DP + 前缀和。
- 询问数量多、询问的是长度区间之和，预处理前缀和可以 O(1) 回答。

## 状态与转移

令 `f[i]` 表示长度为 i 的合法晚餐串数量。

```text
f[i] = f[i - 1] + (i >= k ? f[i - k] : 0)
```

- `f[i - 1]`：第 i 朵是红花。
- `f[i - k]`：最后 k 朵是一组白花。
- i < k 时白花一组都放不下，只有 f[i-1] 一种来源，所以这一段全是 1。

边界：`f[0] = 1`（空串）。答案用前缀和 `S[i] = S[i-1] + f[i]` 计算：`(S[b] - S[a-1]) mod 10^9+7`，注意结果为负时补模。

题型的系统整理见 [[03-算法/动态规划/01-线性DP|线性DP]]。

## 复杂度

- 时间：O(maxB + t)。
- 空间：O(maxB)，其中 maxB 为最大询问右端点。

## Rust 实现

- [examples/cf474d_flowers/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf474d_flowers/main.rs)
- 线性 DP 计算 `f[i]` 后，再用前缀和在 O(1) 内回答每个闭区间查询；已通过 `cargo check` 和样例验证。

## 复盘

- 第一次错误：直接遍历每个 `[a,b]` 区间累加，最坏会重复计算约 `10^10` 个状态。
- 关键边界：`f[0] = 1`；查询是闭区间 `[a,b]`，用 `prefix[b + 1] - prefix[a]`，并补模。
- 一句话总结：静态数组的高频区间和查询，优先预处理前缀和。
