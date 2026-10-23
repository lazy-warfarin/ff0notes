---
type: problem
platform: Codeforces
problem_id: 10D
title: "LCIS"
rating: 2800
tags: ["dp"]
status: todo
priority: challenge
concepts: [序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 10D LCIS

> [Codeforces 10D 原题](https://codeforces.com/problemset/problem/10/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

给定两个整数序列，输出它们的最长公共严格递增子序列及其长度。

## 识别信号

LCS 与 LIS 的组合；固定第一序列当前元素，维护更小值前驱的最优值。

关联笔记：[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 扫描 $A_i$ 时从左到右扫描 $B$，维护 $B_j<A_i$ 的最大旧长度；相等时更新以 $B_j$ 结尾的长度。还原建议保存历史版本或二维父状态，避免一维前驱被后续覆盖。

## 复杂度

长度计算时间 $O(nm)$、空间 $O(m)$；稳健还原保留历史表时空间 $O(nm)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：相等值不能延长严格递增链；公共子序列要求同时保留两边顺序；回溯前驱需要版本一致。
- 一句话总结：待独立完成后填写。
