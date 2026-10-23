---
type: problem
platform: Codeforces
problem_id: 1409F
title: "Subsequences of Length Two"
rating: 2100
tags: ["dp","strings"]
status: todo
priority: important
concepts: [序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1409F Subsequences of Length Two

> [Codeforces 1409F 原题](https://codeforces.com/problemset/problem/1409/F)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

至多修改字符串 $s$ 的 $k$ 个字符，最大化给定二字符字符串 $t$ 作为子序列出现的次数。

## 识别信号

后续贡献取决于前面有多少个 $t_0$，需要增加计数维度。

关联笔记：[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 当 $t_0\ne t_1$，状态为处理位置、已修改次数、已有 $t_0$ 数量；放 $t_1$ 时增加该数量的贡献。每位考虑保留或改为目标字符；两字符相同则单独按组合数处理。

## 复杂度

时间 $O(n^2k)$，滚动空间 $O(nk)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：$t_0=t_1$ 不能套互异状态；出现次数是子序列而非连续子串；修改次数是至多。
- 一句话总结：待独立完成后填写。
