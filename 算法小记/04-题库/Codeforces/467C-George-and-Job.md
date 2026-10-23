---
type: problem
platform: Codeforces
problem_id: 467C
title: "George and Job"
rating: 1700
tags: ["dp","implementation"]
status: todo
priority: core
concepts: [序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 467C George and Job

> [Codeforces 467C 原题](https://codeforces.com/problemset/problem/467/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

从数组中恰好选出 $k$ 段互不相交、长度均为 $m$ 的连续子数组，求最大总和。

## 识别信号

前缀最优与选段数量；“不选当前位置”和“在此结束一段”两类转移。

关联笔记：[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[c][i]=\max(f[c][i-1],f[c-1][i-m]+prefix_i-prefix_{i-m})$，只从合法且可达的状态转移。

## 复杂度

时间 $O(nk)$，空间 $O(nk)$，滚动选段数维度可降为 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：必须恰选 $k$ 段；区间不能重叠；总和使用 64 位。
- 一句话总结：待独立完成后填写。
