---
type: problem
platform: Codeforces
problem_id: 1633D
title: "Make Them Equal"
rating: 1600
tags: ["dp","greedy"]
status: todo
priority: core
concepts: [01背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1633D Make Them Equal

> [Codeforces 1633D 原题](https://codeforces.com/problemset/problem/1633/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

所有元素初始为 1，每次可令某个元素增加其值除以正整数的下取整；最多操作 $k$ 次，使元素恰好达到各自目标时获得奖励，求最大奖励。

## 识别信号

先计算达到每个目标的最小操作数，再做 01 背包。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 按数值递增预处理 $dist[y]$：从 $x$ 向 $x+\lfloor x/d\rfloor$ 松弛；每个目标变成重量 $dist[b_i]$、价值 $c_i$ 的 01 物品。容量截为 $\min(k,\sum dist[b_i])$。

## 复杂度

设最大目标为 $B$、截断后容量为 $K$，朴素预处理 $O(B^2)$，每组背包 $O(nK)$，空间 $O(B+K)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：$b_i=1$ 对应零费用物品，仍只能选一次；不要按原始 $k\le10^6$ 无条件开大循环。
- 一句话总结：待独立完成后填写。
