---
type: problem
platform: Codeforces
problem_id: 319C
title: "Kalila and Dimna in the Logging Industry"
rating: 2100
tags: ["dp","geometry"]
status: todo
priority: important
concepts: [DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 319C Kalila and Dimna in the Logging Industry

> [Codeforces 319C 原题](https://codeforces.com/problemset/problem/319/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

树高递增、完全砍倒的最大编号越大则之后充电单价越低，电锯初始已充电，求砍倒全部树的最小费用。

## 识别信号

转移可表示为直线在查询点的最小值；斜率和查询点都单调。

关联笔记：[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> 建模为 $f_1=0$、$f_i=\min_{j<i}(f_j+b_ja_i)$，将已完成状态作为直线 $y=b_jx+f_j$，用单调凸包查询。

## 复杂度

单调凸包均摊时间 $O(n)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：先查询后插入；乘积与费用使用 64 位，交叉乘比较用 i128；初始电量对应 $f_1=0$。
- 一句话总结：待独立完成后填写。
