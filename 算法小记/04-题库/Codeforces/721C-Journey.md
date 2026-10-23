---
type: problem
platform: Codeforces
problem_id: 721C
title: "Journey"
rating: 1800
tags: ["dp","graphs"]
status: todo
priority: core
concepts: [图上DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 721C Journey

> [Codeforces 721C 原题](https://codeforces.com/problemset/problem/721/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在带正时间的 DAG 中，从 1 到 $n$，总时间不超过 $T$，最大化访问顶点数并输出路线，保证至少一条可行路线。

## 识别信号

DAG 加路径长度维度；最小耗时状态比最大时间容量更合适。

关联笔记：[[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[len][v]$ 为恰经过 $len$ 个顶点到 $v$ 的最小耗时；枚举边从上一长度转移并保存前驱，选择满足时间上限的最大长度回溯。

## 复杂度

时间 $O(nm)$，保留路线表空间 $O(n^2)$；按原题内存预算选择紧凑的父节点类型。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：顶点数不是边数；无穷值加边权防溢出；不能按 $T\le10^9$ 做容量 DP。
- 一句话总结：待独立完成后填写。
