---
type: problem
platform: Codeforces
problem_id: 8C
title: "Looking for Order"
rating: 2000
tags: ["bitmasks","dp"]
status: todo
priority: important
concepts: [状态压缩DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 8C Looking for Order

> [Codeforces 8C 原题](https://codeforces.com/problemset/problem/8/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

从固定的手提包位置出发收集所有物品，每趟最多拿两个且必须送回手提包（输出中把手提包记为 0）；两点间耗时为欧氏距离平方，输出最小总耗时和路线。

## 识别信号

集合 DP；固定第一个未收集物品消除趟次顺序重复。

关联笔记：[[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 对未完成集合取固定物品 $i$，选择单独取回或再与一个 $j$ 同趟取回；记录最优的单点或配对选择，再输出每趟的 $0,i,(j),0$。

## 复杂度

保守时间上界 $O(n2^n)$，空间 $O(2^n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：使用距离平方，不要开根号；每趟至多两个；$n=24$ 时须估算 DP 与回溯表内存。
- 一句话总结：待独立完成后填写。
