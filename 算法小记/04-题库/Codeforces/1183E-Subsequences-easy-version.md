---
type: problem
platform: Codeforces
problem_id: 1183E
title: "Subsequences (easy version)"
rating: 2000
tags: ["dp","graphs","implementation","shortest paths"]
status: todo
priority: important
concepts: [序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1183E Subsequences (easy version)

> [Codeforces 1183E 原题](https://codeforces.com/problemset/problem/1183/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

从字符串的不同子序列中选出 $k$ 个组成集合，每个代价为删除字符数，求最小总代价，无法得到足够多不同子序列则输出 -1。

## 识别信号

按子序列长度计数并去重；优先选择更长的不同子序列。

关联笔记：[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 用位置与长度 DP 统计不同子序列：加入当前字符时减去其上次出现造成的重复贡献；小数据可用 128 位保存精确计数，再从长到短取至多 $k$ 个。

## 复杂度

时间与空间均为 $O(n^2)$；这里 $n\le100$，总子序列数不超过 $2^{100}$，可用 u128。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：空字符串也是子序列；按字符串内容去重而非下标；不能随意截断带减法的中间计数。
- 一句话总结：待独立完成后填写。
