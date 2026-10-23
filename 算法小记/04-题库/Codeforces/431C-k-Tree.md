---
type: problem
platform: Codeforces
problem_id: 431C
title: "k-Tree"
rating: 1600
tags: ["dp","implementation","trees"]
status: todo
priority: core
concepts: [线性DP, 完全背包, 计数与方案]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 431C k-Tree

> [Codeforces 431C 原题](https://codeforces.com/problemset/problem/431/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在每个节点都有权重 1 到 $k$ 的子边的无限树中，统计从根出发、总权重恰好为 $n$ 且至少含一条权重不小于 $d$ 的路径，模 $10^9+7$。

## 识别信号

完全背包式有序计数；额外状态记录是否使用过大边。

关联笔记：[[03-算法/动态规划/01-线性DP|线性DP]]、[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]、[[03-算法/动态规划/02-背包DP/05-计数与方案|计数与方案]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[s][used]$ 表示总和为 $s$ 的有序路径数；总和外层递增，枚举下一条边 $w$，更新到 $(s+w,used\lor(w\ge d))$，初始 $f[0][0]=1$。

## 复杂度

时间 $O(nk)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：路径顺序不同算不同方案；容量必须恰好；不要按边权外层写成无序组合计数。
- 一句话总结：待独立完成后填写。
