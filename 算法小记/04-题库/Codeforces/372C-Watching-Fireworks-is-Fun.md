---
type: problem
platform: Codeforces
problem_id: 372C
title: "Watching Fireworks is Fun"
rating: 2100
tags: ["data structures","dp","math"]
status: todo
priority: important
concepts: [DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 372C Watching Fireworks is Fun

> [Codeforces 372C 原题](https://codeforces.com/problemset/problem/372/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在街道上以受限速度移动，每场烟火的收益为基础快乐值减去距离，可自由选择初始位置，求所有烟火的最大总收益。

## 识别信号

时间差给出可达位置窗口；单调队列维护上一层窗口最大值。

关联笔记：[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f_i[x]=b_i-|a_i-x|+\max_{|y-x|\le d(t_i-t_{i-1})}f_{i-1}[y]$；截断窗口到街道范围，每层用队列线性扫描。

## 复杂度

时间 $O(nm)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：同时发生的烟火不能移动；收益可为负；移动距离乘法与累计收益使用 64 位。
- 一句话总结：待独立完成后填写。
