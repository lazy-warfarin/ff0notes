---
type: problem
platform: Codeforces
problem_id: 598E
title: "Chocolate Bar"
rating: 2000
tags: ["brute force","dp"]
status: todo
priority: important
concepts: [区间DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 598E Chocolate Bar

> [Codeforces 598E 原题](https://codeforces.com/problemset/problem/598/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

矩形巧克力只能沿格线切成两个矩形，每刀费用为切割长度的平方，求能取走恰好 $k$ 格的最小总切割费用。

## 识别信号

二维区间切分与容量分配；子问题还需记录要取多少格。

关联笔记：[[03-算法/动态规划/03-区间DP|区间DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> $f[h][w][k]$ 枚举横切或竖切位置，再枚举分配给两块的格数；加该刀的长度平方；$k=0$ 或 $k=hw$ 时费用为 0。

## 复杂度

预处理宽松上界 $O(HW(H+W)K^2)$，空间 $O(HWK)$；多组询问复用表。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：剩余巧克力不必连成一块；分给子矩形的格数不能超过其面积；横切费用是宽度平方。
- 一句话总结：待独立完成后填写。
