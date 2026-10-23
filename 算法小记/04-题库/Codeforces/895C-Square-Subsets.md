---
type: problem
platform: Codeforces
problem_id: 895C
title: "Square Subsets"
rating: 2000
tags: ["bitmasks","combinatorics","dp","math"]
status: todo
priority: important
concepts: [状态压缩DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 895C Square Subsets

> [Codeforces 895C 原题](https://codeforces.com/problemset/problem/895/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

从数组中选非空下标子集，使乘积为完全平方数，求方案数，模 $10^9+7$；元素值介于 1 到 70。

## 识别信号

每个质因子指数只关心奇偶；按数值频次聚合状压计数。

关联笔记：[[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 将值映为 19 位奇偶掩码；出现 $c>0$ 次的值，选偶数次和奇数次的方案均为 $2^{c-1}$；分别保留或异或该掩码，最终取零掩码并减空集。

## 复杂度

时间 $O(70\cdot2^{19}+n)$，空间 $O(2^{19})$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：重复值按下标区分方案；值为 1 也影响方案数；最后减去空集并规范化取模。
- 一句话总结：待独立完成后填写。
