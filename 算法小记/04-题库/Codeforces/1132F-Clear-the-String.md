---
type: problem
platform: Codeforces
problem_id: 1132F
title: "Clear the String"
rating: 2000
tags: ["dp"]
status: todo
priority: important
concepts: [区间DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1132F Clear the String

> [Codeforces 1132F 原题](https://codeforces.com/problemset/problem/1132/F)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

每次删除一段连续且字符相同的子串，删除后两侧拼接，求删空字符串的最少操作数。

## 识别信号

删除中间后可合并相同端点；区间 DP。

关联笔记：[[03-算法/动态规划/03-区间DP|区间DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 先令 $f[l][r]=1+f[l+1][r]$；若 $s_l=s_k$，可让左端与 $k$ 同次删除，取 $f[l+1][k-1]+f[k][r]$，空区间为 0。

## 复杂度

时间 $O(n^3)$，空间 $O(n^2)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：删除后原本不相邻的字符会贴合；不能只统计当前连续段数量。
- 一句话总结：待独立完成后填写。
