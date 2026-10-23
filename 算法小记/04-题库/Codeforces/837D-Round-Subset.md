---
type: problem
platform: Codeforces
problem_id: 837D
title: "Round Subset"
rating: 2100
tags: ["dp","math"]
status: todo
priority: important
concepts: [01背包, 多维与依赖背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 837D Round Subset

> [Codeforces 837D 原题](https://codeforces.com/problemset/problem/837/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

恰好选择 $k$ 个数，最大化它们乘积末尾的零的个数。

## 识别信号

分解出因子 2、5，将双指标最优值转为二维 01 背包。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]、[[03-算法/动态规划/02-背包DP/04-多维与依赖背包|多维与依赖背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[c][s]$ 为恰选 $c$ 个数且因子 5 数量为 $s$ 时最多的因子 2 数量；件数和因子 5 数量倒序，答案为 $\max_s\min(s,f[k][s])$。

## 复杂度

设 $S$ 为所需因子 5 数量上界，时间 $O(nkS)$，空间 $O(kS)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：必须恰选 $k$ 个；不可达状态用负值；不能实际计算巨大乘积。
- 一句话总结：待独立完成后填写。
