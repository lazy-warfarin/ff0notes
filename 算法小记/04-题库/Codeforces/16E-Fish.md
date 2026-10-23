---
type: problem
platform: Codeforces
problem_id: 16E
title: "Fish"
rating: 1900
tags: ["bitmasks","dp","probabilities"]
status: todo
priority: important
concepts: [状态压缩DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 16E Fish

> [Codeforces 16E 原题](https://codeforces.com/problemset/problem/16/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

每轮从现存鱼中等概率选一对，按给定概率一条吃掉另一条，直到剩一条，求每条鱼最终存活的概率。

## 识别信号

集合状态的概率 DP；状态大小严格递减。

关联笔记：[[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 满集合概率为 1；对活鱼集合 $S$，删去鱼 $j$ 的概率贡献为 $f[S]\sum_{i\in S\setminus\{j\}}a_{ij}/\binom{|S|}{2}$，从大集合转移到小集合。

## 复杂度

直接实现时间 $O(n^2 2^n)$，空间 $O(2^n)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：分母是当前鱼数的组合数；单鱼状态停止；各鱼最终概率之和应接近 1。
- 一句话总结：待独立完成后填写。
