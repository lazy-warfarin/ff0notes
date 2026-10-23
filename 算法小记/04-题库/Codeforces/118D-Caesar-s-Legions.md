---
type: problem
platform: Codeforces
problem_id: 118D
title: "Caesar's Legions"
rating: 1700
tags: ["dp"]
status: todo
priority: core
concepts: [线性DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 118D Caesar's Legions

> [Codeforces 118D 原题](https://codeforces.com/problemset/problem/118/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

将所有步兵和骑兵排成一列，连续步兵与连续骑兵的长度分别有上限，同类士兵不可区分，求排列数，模 $10^8$。

## 识别信号

计数型线性 DP；剩余数量与末尾兵种共同决定后续选择。

关联笔记：[[03-算法/动态规划/01-线性DP|线性DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $f[i][j][type]$ 为用了 $i$ 个步兵、$j$ 个骑兵且末尾为指定兵种的方案数；枚举末尾连续段长度，从另一兵种结尾转移。

## 复杂度

时间 $O(n_1n_2(k_1+k_2))$，空间 $O(n_1n_2)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：模数是 $10^8$；全由一种兵组成的边界需单独初始化；不能把同类士兵编号计入方案。
- 一句话总结：待独立完成后填写。
