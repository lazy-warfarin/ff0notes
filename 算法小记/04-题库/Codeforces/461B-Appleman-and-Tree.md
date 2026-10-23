---
type: problem
platform: Codeforces
problem_id: 461B
title: "Appleman and Tree"
rating: 2000
tags: ["dfs and similar","dp","trees"]
status: todo
priority: important
concepts: [树形DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 461B Appleman and Tree

> [Codeforces 461B 原题](https://codeforces.com/problemset/problem/461/B)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

树上部分顶点为黑色，删除若干边，使每个连通块恰含一个黑点，求删边集合数量，模 $10^9+7$。

## 识别信号

树形计数；状态记录与父节点相连的未封闭连通块含 0 或 1 个黑点。

关联笔记：[[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 合并孩子：保留边时两个未封闭块的黑点总数不能超过 1；切断边时孩子的未封闭块必须恰含一个黑点。根最终必须处于 1 状态。

## 复杂度

时间 $O(n)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：节点编号从 0 开始；切断边不能遗留无黑点连通块；深链使用迭代后序。
- 一句话总结：待独立完成后填写。
