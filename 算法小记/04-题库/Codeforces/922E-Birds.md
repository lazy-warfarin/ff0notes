---
type: problem
platform: Codeforces
problem_id: 922E
title: "Birds"
rating: 2200
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

# 922E Birds

> [Codeforces 922E 原题](https://codeforces.com/problemset/problem/922/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

沿树列依次召唤鸟，每棵鸟数有限、召唤消耗法力，每召唤一只增加法力上限，移动到下一棵恢复法力，求最多召唤多少只。

## 识别信号

有限数量选择叠加资源恢复；这是动态容量建模，不是单纯套混合背包循环。

关联笔记：[[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[j]$ 表示处理当前树后召唤 $j$ 只鸟可剩余的最大法力；枚举当前树召唤数，先检查支付能力；移动时令法力为 $\min(W+jB,f[j]+X)$。

## 复杂度

设鸟总数为 $C$，逐组枚举的保守时间 $O(nC+C^2)$，空间 $O(C)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：第一棵树前不能凭空恢复法力；购买途中不能借未来恢复值；相同数量只保留剩余法力最多的状态。
- 一句话总结：待独立完成后填写。
