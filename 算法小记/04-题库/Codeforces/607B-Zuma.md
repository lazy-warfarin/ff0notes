---
type: problem
platform: Codeforces
problem_id: 607B
title: Zuma
rating: 1900
tags: [dp]
status: todo
priority: core
concepts: [区间DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 607B Zuma

> [Codeforces 607B - Zuma](https://codeforces.com/problemset/problem/607/B)

## 题意摘要

一行 $n$ 个宝石（$n \le 500$），第 $i$ 个宝石颜色为 $c_i$。每秒可以选中一个回文的连续子串并整段移除；一段被移除后，两侧剩余的宝石会拼接到一起。求清空整行所需的最短时间。

## 识别信号

- 操作对象是连续区间，且删除后两侧会拼接、影响后续判断，属于区间 DP。
- 大区间答案由小区间合并而来，按区间长度从小到大枚举即可。
- 两端颜色相同时可以"合并成一次删除"，需要在转移里特判 a[l] == a[r]。

## 状态与转移

令 `dp[l][r]` 表示清空区间 $[l, r]$ 的最少操作数。

```text
若 l == r：dp[l][r] = 1
若 a[l] == a[r]：
  长度 2：dp[l][r] = 1
  长度 >= 3：dp[l][r] = dp[l + 1][r - 1]
枚举分割点 k（l <= k < r）：
  dp[l][r] = min(dp[l][r], dp[l][k] + dp[k + 1][r])
```

- 按区间长度 1..n 外层枚举，保证所有更短的区间已经算好。
- a[l] == a[r] 时，先把中间清空（代价 dp[l+1][r-1]），两个同色端点会拼到一起，可以随最后一段一起消掉。
- 分割转移覆盖两端颜色不同的情况，也兜底所有合并方式。

边界：长度为 1 的区间答案为 1；长度为 2 且两色相同时答案为 1，否则为 2（两种写法选其一即可）。最终答案是 `dp[1][n]`。

区间模型的系统整理见 [[03-算法/动态规划/03-区间DP|区间DP]]。

## 复杂度

- 时间：O(n^3)。
- 空间：O(n^2)。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
