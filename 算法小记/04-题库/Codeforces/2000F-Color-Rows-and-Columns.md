---
type: problem
platform: Codeforces
problem_id: 2000F
title: "Color Rows and Columns"
rating: 1900
tags: ["dp","greedy","implementation","math"]
status: todo
priority: important
concepts: [分组与混合背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 2000F Color Rows and Columns

> [Codeforces 2000F 原题](https://codeforces.com/problemset/problem/2000/F)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在若干矩形中逐格涂色，每涂满一行或一列获得 1 分，求至少得到 $k$ 分所需的最少涂格数，无解输出 -1。

## 识别信号

每个矩形先求不同得分的代价表，再做分组最小值背包。

关联笔记：[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 单矩形每次看剩余矩形，完成较短边方向的一条线；变成正方形后行列交替，得到各得分档位的最小代价。注意最后一格可能同时完成一行和一列；全局状态将得分饱和到 $k$，每个矩形从上一组转移。不要写成“先把短边全部填完”，例如 $4\times4$、$k=5$ 会得到 16，正确是 14。

## 复杂度

每矩形预处理至所需得分后，全局时间 $O(nk^2)$，空间 $O(k)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：目标是至少 $k$ 分；最后一格的双倍得分；每个矩形只选择一档代价，不能重复购买各档。
- 一句话总结：待独立完成后填写。
