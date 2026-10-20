---
type: problem
platform: Codeforces
problem_id: 868F
title: Yet Another Minimization Problem
rating: 2500
tags: [divide and conquer, dp]
status: todo
priority: challenge
concepts: [DP优化, 分治优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 868F Yet Another Minimization Problem

> [Codeforces 868F - Yet Another Minimization Problem](https://codeforces.com/problemset/problem/868/F)

## 题意摘要

给出长度为 $n$ 的数组 $a$（$n \le 10^5$）和段数 $k$（$k \le 20$）。把数组切成 $k$ 段连续的非空区间，一段区间的代价是段内“值相等的数对”个数，即 $\sum_x \binom{\operatorname{cnt}[x]}{2}$。求所有段代价之和的最小值。

## 识别信号

- 切分连续区间、段数固定、段代价与区间内元素的分布有关，先写 O(k n^2) 的朴素 dp。
- 代价函数满足四边形不等式，最优分割点随右端点单调不减，符合分治优化的条件。
- 代价按端点增删元素时只变更一个计数，可以 O(1) 维护：加入一个值 x 时，新增的数对数是加之前的 `cnt[x]`。

## 状态与转移

令 `dp[j][i]` 表示前 $i$ 个数切成 $j$ 段的最小总代价，`cost(s, e)` 表示区间 $[s, e]$ 的代价。

```text
dp[j][i] = min over t in [j - 1, i - 1] of (dp[j - 1][t] + cost(t + 1, i))
```

对固定的 j，用分治优化求解，同时用两个指针维护 `cost`：

```text
solve(j, l, r, optL, optR):
  mid = (l + r) / 2
  移动窗口指针，令当前窗口为 [t + 1, mid]，随 t 枚举同步增删元素
  加入元素 x：cur += cnt[x]; cnt[x] += 1
  删除元素 x：cnt[x] -= 1; cur -= cnt[x]
  枚举 t 得到最小值与最优 t = opt
  solve(j, l, mid - 1, optL, opt)
  solve(j, mid + 1, r, opt, optR)
```

- 代价单调性保证只在 `[optL, optR]` 内枚举 t，分治把每层枚举量压到 O(n log n)。
- 指针在递归中反复移动，但总移动量同时也是 O(n log n)，每次增删都是 O(1)。
- 每层对 j 从小到大递推，答案在 `dp[k][n]`。

边界：`dp[0][0] = 0`，其余初始化为 +∞；空段不允许出现。答案为 64 位整数（最多约 n^2 / 2 个数对）。

分治优化与决策单调性的适用条件见 [[03-算法/动态规划/08-DP优化|DP优化]]。

## 复杂度

- 时间：O(k * n log n)。
- 空间：O(n)，两层 dp 滚动数组 + 计数数组。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
