---
type: problem
platform: Codeforces
problem_id: 95E
title: "Lucky Country"
rating: 2500
tags: ["dp","dsu","graphs"]
status: todo
priority: challenge
concepts: [多重背包, DP优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 95E Lucky Country

> [Codeforces 95E 原题](https://codeforces.com/problemset/problem/95/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

无向图的连通块代表地区，希望通过新增最少道路得到一个连通块，使其中岛屿数量是幸运数（十进制只含 4 和 7），无法做到则输出 -1。

## 识别信号

DSU 提取块大小，再按相同大小聚合为多重背包。

关联笔记：[[03-算法/动态规划/02-背包DP/02-多重背包|多重背包]]、[[03-算法/动态规划/08-DP优化|DP优化]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $f[s]$ 为拼出总大小 $s$ 的最少连通块数，同大小块的数量就是库存；按余数用单调队列做有界最小值转移，枚举幸运数取 $f[s]-1$。

## 复杂度

设不同块大小数为 $D$，时间 $O((n+m)\alpha(n)+nD)$，空间 $O(n)$；$D=O(\sqrt n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：原有幸运连通块需要 0 条路；自环重边不影响 DSU；最小块数最后减一。
- 一句话总结：待独立完成后填写。
