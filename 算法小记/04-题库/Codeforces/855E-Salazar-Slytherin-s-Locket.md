---
type: problem
platform: Codeforces
problem_id: 855E
title: "Salazar Slytherin's Locket"
rating: 2200
tags: ["bitmasks","dp"]
status: todo
priority: important
concepts: [数位DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 855E Salazar Slytherin's Locket

> [Codeforces 855E 原题](https://codeforces.com/problemset/problem/855/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

多组查询给定进制 $b$ 和闭区间，统计该进制下每种数字都出现偶数次的正整数个数，不计前导零。

## 识别信号

数位 DP 与数位出现次数奇偶掩码。

关联笔记：[[03-算法/动态规划/07-数位DP|数位DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 按进制预处理自由后缀的奇偶计数；逐位扫描上界，对更小候选首个分歧位加上对应后缀贡献，分长度排除前导零，做 $F(r)-F(l-1)$。

## 复杂度

设最长位数为 $L$，每种进制预处理 $O(Lb2^b)$，每次查询 $O(Lb)$；缓存空间 $O(L2^b)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：未出现数字计 0 次，属于偶数；前导零不能翻转 0 的奇偶位；预处理必须按进制区分。
- 一句话总结：待独立完成后填写。
