---
type: problem
platform: Codeforces
problem_id: 148E
title: "Porcelain"
rating: 1900
tags: ["dp"]
status: todo
priority: important
concepts: [分组与混合背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 148E Porcelain

> [Codeforces 148E 原题](https://codeforces.com/problemset/problem/148/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

每层架子只能从两端拿走瓷器，恰好拿走 $m$ 件，使价值总和最大。

## 识别信号

先枚举组内合法选择，再做分组背包。

关联笔记：[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 对每层预处理 $best[t]$：左端拿 $x$ 件、右端拿 $t-x$ 件的最大价值；以每层为一组、拿走件数为容量，从上一层架子状态转移。

## 复杂度

设架子长度为 $len_i$，时间 $O(\sum len_i^2+m\sum len_i)$，空间 $O(m+\max len_i)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：左右选择不能重叠；同一层所有选项必须读上一组；最后取恰好 $m$ 件。
- 一句话总结：待独立完成后填写。
