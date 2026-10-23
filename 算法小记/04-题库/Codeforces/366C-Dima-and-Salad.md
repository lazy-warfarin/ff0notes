---
type: problem
platform: Codeforces
problem_id: 366C
title: "Dima and Salad"
rating: 1900
tags: ["dp"]
status: todo
priority: important
concepts: [01背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 366C Dima and Salad

> [Codeforces 366C 原题](https://codeforces.com/problemset/problem/366/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

从水果中选择非空子集，使总美味值与总热量之比恰好等于 $k$，并最大化总美味值，无解输出 -1。

## 识别信号

比例约束转为差值为零的 01 背包。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $w_i=a_i-kb_i$，以差值为状态，保存最大美味值；每件物品从上一层转移。最终查看差值 0，排除只有空集的情况。

## 复杂度

设 $R=\sum|w_i|$，时间 $O(nR)$，空间 $O(R)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：差值可能为负；使用偏移或映射；值为 0 的初始空方案不能当作合法沙拉。
- 一句话总结：待独立完成后填写。
