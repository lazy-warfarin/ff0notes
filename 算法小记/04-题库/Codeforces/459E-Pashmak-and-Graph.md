---
type: problem
platform: Codeforces
problem_id: 459E
title: "Pashmak and Graph"
rating: 1900
tags: ["dp","sortings"]
status: todo
priority: important
concepts: [图上DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 459E Pashmak and Graph

> [Codeforces 459E 原题](https://codeforces.com/problemset/problem/459/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

在带权有向图中寻找边权严格递增且边数最多的路径，允许重复顶点，输出最大边数。

## 识别信号

原图可有环，但按边权分层后的状态依赖无环。

关联笔记：[[03-算法/动态规划/05-树形与图DP|树形与图DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 按边权排序，处理同权重的一整批边时先查询旧 $f[u]+1$，全部查询完再更新目标顶点，避免相同权重串接。

## 复杂度

时间 $O(m\log m)$，空间 $O(n+m)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：与 960F 不同，此题无输入顺序限制；同权重必须批量更新；答案统计边数。
- 一句话总结：待独立完成后填写。
