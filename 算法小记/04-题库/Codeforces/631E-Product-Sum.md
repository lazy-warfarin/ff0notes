---
type: problem
platform: Codeforces
problem_id: 631E
title: "Product Sum"
rating: 2600
tags: ["data structures","dp","geometry"]
status: todo
priority: challenge
concepts: [DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 631E Product Sum

> [Codeforces 631E 原题](https://codeforces.com/problemset/problem/631/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

至多把一个元素移到任意位置，其他元素相对顺序不变，最大化 $\sum_i i a_i$；允许放回原处。

## 识别信号

枚举移出的元素后，其最佳新位置可转为直线最大值查询。

关联笔记：[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> 用前缀和推导左右移动的增益。移到右侧 $j>i$ 的增益为 $(j-i)a_i-(P_j-P_i)$；移到左侧为 $(j-i)a_i+P_{i-1}-P_{j-1}$。两次扫描维护候选 $j$ 的直线，取最大增益。

## 复杂度

使用凸包二分查询或离散 Li Chao 树，时间 $O(n\log n)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：查询横坐标 $a_i$ 不单调且可为负，不能直接用仅适用于单调查询的弹出队首写法；保留不移动的零增益。
- 一句话总结：待独立完成后填写。
