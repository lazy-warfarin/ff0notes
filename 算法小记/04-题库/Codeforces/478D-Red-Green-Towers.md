---
type: problem
platform: Codeforces
problem_id: 478D
title: "Red-Green Towers"
rating: 2000
tags: ["dp"]
status: todo
priority: important
concepts: [01背包, 计数与方案]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 478D Red-Green Towers

> [Codeforces 478D 原题](https://codeforces.com/problemset/problem/478/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

用红绿积木搭最高的塔，第 $i$ 层需 $i$ 块且同层只能一种颜色，求达到最大可行高度的颜色分配方案数，模 $10^9+7$。

## 识别信号

每层是否使用红色是一次 01 决策，绿色用量由总量确定。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]、[[03-算法/动态规划/02-背包DP/05-计数与方案|计数与方案]]。

## 状态与转移

> [!tip]- 展开建模提示
> 先求满足 $h(h+1)/2\le r+g$ 的最大 $h$；对层高 1 到 $h$ 做红色用量的 01 计数，最后对同时满足红绿库存限制的用量求和。

## 复杂度

时间 $O(h\min(r,g))$（交换两种颜色后），空间 $O(\min(r,g))$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：最大高度只看总库存，但计数需检查两种库存；容量倒序；一色库存为 0。
- 一句话总结：待独立完成后填写。
