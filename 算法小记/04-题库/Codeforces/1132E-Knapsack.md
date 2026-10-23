---
type: problem
platform: Codeforces
problem_id: 1132E
title: "Knapsack"
rating: 2300
tags: ["dfs and similar","dp","greedy"]
status: todo
priority: challenge
concepts: [多重背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1132E Knapsack

> [Codeforces 1132E 原题](https://codeforces.com/problemset/problem/1132/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

重量只有 1 到 8，每种重量给出极大库存，容量也很大，求不超过容量的最大可选总重量。

## 识别信号

小重量、大库存的多重背包；不能对原始容量做 DP。

关联笔记：[[03-算法/动态规划/02-背包DP/02-多重背包|多重背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 取 $L=\operatorname{lcm}(1,\ldots,8)=840$。每类最多留不足两个整块的物品做小规模有界 DP，其余每 $L/i$ 件合成重 $L$ 的整块；枚举残余可达重量，再贪心加入尽量多整块。

## 复杂度

残余总重量 $R<16L$，对残余二进制拆分可做 $O(R\sum_i\log(2L/i+1))$ 时间、$O(R)$ 空间。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：库存不足一整块时全部保留，足够时至少留一整块供拆散，不能只保留除以整块后的余数；容量为 0；库存和总重量使用 64 位。
- 一句话总结：待独立完成后填写。
