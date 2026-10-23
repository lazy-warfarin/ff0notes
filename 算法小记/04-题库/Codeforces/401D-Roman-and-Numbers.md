---
type: problem
platform: Codeforces
problem_id: 401D
title: "Roman and Numbers"
rating: 2000
tags: ["bitmasks","brute force","combinatorics","dp","number theory"]
status: todo
priority: important
concepts: [状态压缩DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 401D Roman and Numbers

> [Codeforces 401D 原题](https://codeforces.com/problemset/problem/401/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

重排给定整数的所有数位，不能有前导零，统计能被 $m$ 整除的不同整数个数。

## 识别信号

已用数位集合加余数；需要对重复数位去重。

关联笔记：[[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[mask][r]$ 从空集合开始，选未用数位 $d$ 得到余数 $(10r+d)\bmod m$；数位排序后，相同数位必须按索引顺序使用。

## 复杂度

设位数为 $L$，时间 $O(Lm2^L)$，空间 $O(m2^L)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：首位不能为 0；相同数位排列不算不同整数；计数不取模，使用 64 位。
- 一句话总结：待独立完成后填写。
