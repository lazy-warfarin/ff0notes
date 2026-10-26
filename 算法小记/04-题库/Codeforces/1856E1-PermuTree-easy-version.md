---
type: problem
platform: Codeforces
problem_id: 1856E1
title: "PermuTree (easy version)"
rating: 1800
tags: ["dfs and similar","dp","trees"]
status: todo
priority: core
concepts: [多重背包, DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1856E1 PermuTree (easy version)

> [Codeforces 1856E1 原题](https://codeforces.com/problemset/problem/1856/E1)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

给根树的顶点分配一个排列，最大化满足 $a_u<a_{\operatorname{lca}(u,v)}<a_v$ 的点对 $(u,v)$ 数量；每个无序点对至多一个方向满足，计数时不要乘 2。

## 识别信号

树上贡献拆分后对子树大小做背包；相同大小可聚合成有限库存。

关联笔记：[[03-算法/动态规划/02-背包DP/02-多重背包|多重背包]]、[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> 对每个节点，将孩子子树整体分为两侧；设孩子总大小为 $S$，背包求可达 $s$，该节点贡献为最大的 $s(S-s)$（每个点对只算一次）。累加各节点贡献；可以把相同子树大小按出现次数做多重背包对照。

## 复杂度

easy 版逐孩子做局部 01 背包，总时间 $O(n^2)$；复用工作数组时空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：这里物品是整棵孩子子树，不是单个节点；只收录 easy 版，不把 hard 版重复算作另一题。
- 一句话总结：待独立完成后填写。
