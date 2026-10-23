---
type: problem
platform: Codeforces
problem_id: 741B
title: "Arpa's weak amphitheater and Mehrdad's valuable Hoses"
rating: 1600
tags: ["dfs and similar","dp","dsu"]
status: todo
priority: core
concepts: [分组与混合背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 741B Arpa's weak amphitheater and Mehrdad's valuable Hoses

> [Codeforces 741B 原题](https://codeforces.com/problemset/problem/741/B)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

朋友关系的每个连通块可以全选、选其中一人或不选，在总重量限制内最大化总美丽值。

## 识别信号

DSU 确定组；每组的单人选项和整体选项互斥。

关联笔记：[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 每个连通块构造所有单人物品与一个整组物品，再做每组最多选一项的分组背包。

## 复杂度

时间 $O((n+m)\alpha(n)+nW)$，空间 $O(n+W)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：整组与组内单人不能叠加；不能任取同组两人；单点组的重复选项不应多次选取。
- 一句话总结：待独立完成后填写。
