---
type: problem
platform: Codeforces
problem_id: 999F
title: "Cards and Joy"
rating: 2000
tags: ["dp"]
status: todo
priority: important
concepts: [分组与混合背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 999F Cards and Joy

> [Codeforces 999F 原题](https://codeforces.com/problemset/problem/999/F)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

将所有卡片分给玩家，每人恰有 $k$ 张，玩家只根据自己喜爱数字的卡片张数获得快乐值，求最大总快乐值。

## 识别信号

按数字拆开资源分配；每个玩家的一组选项有不同张数和非线性收益。

关联笔记：[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 预处理 $best[p][c]$：给 $p$ 位同喜好玩家分配不超过 $c$ 张喜爱卡片的最大快乐，每位玩家枚举 0 到 $k$ 张做分组转移；按每个数字的库存与玩家数查询并求和。

## 复杂度

公共预处理时间 $O(n^2k^2)$，空间 $O(n^2k)$；其余统计 $O(nk)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：每人最终恰有 $k$ 张，但不喜爱的卡片可以补位；快乐值按张数查表，不能按单张固定价值贪心。
- 一句话总结：待独立完成后填写。
