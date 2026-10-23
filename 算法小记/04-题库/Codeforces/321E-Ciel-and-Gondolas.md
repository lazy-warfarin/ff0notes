---
type: problem
platform: Codeforces
problem_id: 321E
title: "Ciel and Gondolas"
rating: 2600
tags: ["data structures","divide and conquer","dp"]
status: todo
priority: challenge
concepts: [DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 321E Ciel and Gondolas

> [Codeforces 321E 原题](https://codeforces.com/problemset/problem/321/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

按原队列顺序分为恰好 $k$ 个非空连续组，每组代价为组内所有无序对的陌生度之和，求最小总代价。

## 识别信号

分段 DP，区间代价可预处理，最优分割点具有单调性。

关联笔记：[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> 二维前缀和计算 $cost(l,r)$；$f_g[i]=\min_{g-1\le j<i}(f_{g-1}[j]+cost(j+1,i))$，证明决策单调性后对每层分治求值。

## 复杂度

时间 $O(n^2+kn\log n)$，空间 $O(n^2)$，DP 层可滚动。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：矩阵对称，代价需避免重复计算一对人；必须非空分组；不能在未经证明的 DP 中照搬分治优化。
- 一句话总结：待独立完成后填写。
