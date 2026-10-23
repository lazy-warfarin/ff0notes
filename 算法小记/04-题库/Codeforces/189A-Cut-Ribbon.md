---
type: problem
platform: Codeforces
problem_id: 189A
title: "Cut Ribbon"
rating: 1300
tags: ["brute force","dp"]
status: todo
priority: core
concepts: [完全背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 189A Cut Ribbon

> [Codeforces 189A 原题](https://codeforces.com/problemset/problem/189/A)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

将长度为 $n$ 的丝带恰好剪成长度只能为 $a,b,c$ 的若干段，最大化段数，保证存在合法方案。

## 识别信号

完全背包最值；同一段长可重复使用，且必须恰好用完。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[0]=0$，其余为负无穷；长度递增，枚举三种段长更新 $f[s]=\max(f[s],f[s-w]+1)$。

## 复杂度

时间 $O(n)$，空间 $O(n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：段长可以相同；不能把不可达位置初始化为 0；结果不是简单选最短长度取整。
- 一句话总结：待独立完成后填写。
