---
type: problem
platform: Codeforces
problem_id: 815C
title: "Karen and Supermarket"
rating: 2400
tags: ["brute force","dp","trees"]
status: todo
priority: challenge
concepts: [多维与依赖背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 815C Karen and Supermarket

> [Codeforces 815C 原题](https://codeforces.com/problemset/problem/815/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

每件商品最多买一次，优惠券有树形前置依赖：使用某券必须使用父券；在预算内最大化商品数量。

## 识别信号

依赖的是优惠券而不是商品购买本身；树形背包与优惠状态合并。

关联笔记：[[03-算法/动态规划/02-背包DP/04-多维与依赖背包|多维与依赖背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $f_u[k][0/1]$ 为子树买 $k$ 件且不使用或使用 $u$ 的优惠券的最小花费；状态 0 的孩子不能用券，状态 1 的孩子可用或不用；逐子树卷积，根处找预算内最大数量。

## 复杂度

按实际子树大小合并时间 $O(n^2)$，直接存表空间 $O(n^2)$，及时释放子表可降低实际内存。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：可以不买父商品而原价买孩子；只有使用孩子优惠券才有父券依赖；费用用 64 位。
- 一句话总结：待独立完成后填写。
