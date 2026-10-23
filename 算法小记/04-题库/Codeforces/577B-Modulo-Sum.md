---
type: problem
platform: Codeforces
problem_id: 577B
title: "Modulo Sum"
rating: 1900
tags: ["combinatorics","data structures","dp","two pointers"]
status: todo
priority: important
concepts: [01背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 577B Modulo Sum

> [Codeforces 577B 原题](https://codeforces.com/problemset/problem/577/B)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

判断能否从数组中选出非空子序列，使其和被 $m$ 整除。

## 识别信号

01 选择与模数状态；大规模输入先用抽屉原理缩减。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 当 $n\ge m$ 时由前缀余数可直接判定存在；否则维护非空子集可达余数，每次从旧数组加入当前数，另加入单元素状态。

## 复杂度

读取时间 $O(n)$；需要 DP 时 $O(nm)$ 且 $n<m$，空间 $O(m)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：不能让空集使余数 0 初始可达；同一轮读旧层；存在值为 0 的元素时立即有解。
- 一句话总结：待独立完成后填写。
