---
type: problem
platform: Codeforces
problem_id: 1114D
title: "Flood Fill"
rating: 1900
tags: ["dp"]
status: todo
priority: important
concepts: [区间DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1114D Flood Fill

> [Codeforces 1114D 原题](https://codeforces.com/problemset/problem/1114/D)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

任选起点，不断将包含起点的同色连通段改色，使整条色带同色，求最少操作次数。

## 识别信号

先压缩相邻同色段，再做端点关系的区间 DP。

关联笔记：[[03-算法/动态规划/03-区间DP|区间DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 压缩后单点代价为 0；两端同色时 $f[l][r]=f[l+1][r-1]+1$，否则为 $\min(f[l+1][r],f[l][r-1])+1$。

## 复杂度

压缩后长度为 $m$，时间 $O(m^2)$，空间 $O(m^2)$，可滚动降到 $O(m)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：原序列全同色答案为 0；相同端点转移依赖中间区间；长度 1、2 单独处理。
- 一句话总结：待独立完成后填写。
