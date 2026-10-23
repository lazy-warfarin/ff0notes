---
type: problem
platform: Codeforces
problem_id: 543D
title: "Road Improvement"
rating: 2300
tags: ["dp","trees"]
status: todo
priority: challenge
concepts: [树形DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 543D Road Improvement

> [Codeforces 543D 原题](https://codeforces.com/problemset/problem/543/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

树上道路初始都坏，选择修好部分道路；对每个首都位置，统计从首都到任一点至多经过一条坏路的修路方案数，模 $10^9+7$。

## 识别信号

面向每个根的乘积型树 DP；换根时排除单个邻居贡献。

关联笔记：[[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 从根看每个孩子方向：连接边修好时递归选择，保持坏路时其后所有边必须修好，因此贡献为 $f_v+1$；两遍遍历配合邻居前后缀积计算全部根。

## 复杂度

时间 $O(n)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：某个贡献模后可能为 0，使用前后缀积而不是直接除法；同一方案按修好边的集合区分。
- 一句话总结：待独立完成后填写。
