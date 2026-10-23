---
type: problem
platform: Codeforces
problem_id: 960F
title: "Pathwalks"
rating: 2100
tags: ["data structures","dp","graphs"]
status: todo
priority: important
concepts: [图上DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 960F Pathwalks

> [Codeforces 960F 原题](https://codeforces.com/problemset/problem/960/F)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在有向图中选择最长的边序列，要求首尾连通、边权严格递增，而且所选边必须按原输入顺序出现；可重复顶点、存在自环重边。

## 识别信号

输入顺序形成前后依赖；每个顶点还需维护权重前缀最优。

关联笔记：[[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 严格按输入处理每条 $u\to v$、权重 $w$ 的边，查询 $u$ 处所有权重小于 $w$ 的最优长度，加一后更新 $v$ 的权重 $w$；可逐顶点离散化后用树状数组。

## 复杂度

时间 $O(m\log m)$，空间 $O(n+m)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：不能按边权排序破坏输入顺序；自环也要先查询后更新；查询不含相等权重。
- 一句话总结：待独立完成后填写。
