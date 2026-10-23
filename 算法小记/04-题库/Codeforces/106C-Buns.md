---
type: problem
platform: Codeforces
problem_id: 106C
title: "Buns"
rating: 1700
tags: ["dp"]
status: todo
priority: core
concepts: [完全背包, 多重背包, 分组与混合背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 106C Buns

> [Codeforces 106C 原题](https://codeforces.com/problemset/problem/106/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

有一份总面团和若干限量馅料，带馅面包消耗对应馅料与面团，无馅面包只消耗面团且不限个数，求最大收入。

## 识别信号

有馅物品是多重背包，无馅物品是完全背包，是直接的混合背包例题。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]、[[03-算法/动态规划/02-背包DP/02-多重背包|多重背包]]、[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 第 $i$ 种带馅面包最多做 $\lfloor a_i/b_i\rfloor$ 个，按此数量做有界转移；无馅面包按容量正序做无限次转移。

## 复杂度

设面团总量为 $N$、第 $i$ 种馅料最多可做 $q_i=\lfloor a_i/b_i\rfloor$ 个面包。朴素时间 $O(N(1+\sum_i q_i))$，二进制拆分后 $O(N(1+\sum_i\log(q_i+1)))$；空间 $O(N)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：件数由馅料除法决定，不是直接取馅料克数；无馅面包允许重复；剩余原料可丢弃。
- 一句话总结：待独立完成后填写。
