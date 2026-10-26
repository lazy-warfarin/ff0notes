---
type: problem
platform: Codeforces
problem_id: 4D
title: "Mysterious Present"
rating: 1700
tags: ["dp","sortings"]
status: todo
priority: core
concepts: [序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 4D Mysterious Present

> [Codeforces 4D 原题](https://codeforces.com/problemset/problem/4/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

信封和卡片都不可旋转，宽与高都严格更大才可套入，求能够装下给定卡片的最长信封链并输出原编号。

## 识别信号

二维偏序转为最长链 DP，并保存前驱。

关联笔记：[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 过滤装不下卡片的信封，按宽度排序，$f_i=1+\max_{w_j<w_i,h_j<h_i}f_j$，记录前驱；从最大终态回溯并反转。

## 复杂度

平方 DP 时间 $O(n^2)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：两维都要严格大于；排序后保留原编号；无可用信封只输出 0。
- 一句话总结：待独立完成后填写。
