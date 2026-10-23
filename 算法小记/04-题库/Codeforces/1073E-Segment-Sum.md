---
type: problem
platform: Codeforces
problem_id: 1073E
title: "Segment Sum"
rating: 2300
tags: ["bitmasks","combinatorics","dp","math"]
status: todo
priority: challenge
concepts: [数位DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1073E Segment Sum

> [Codeforces 1073E 原题](https://codeforces.com/problemset/problem/1073/E)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

对区间内最多使用 $k$ 种十进制数字的整数求数值之和，模 $998244353$。

## 识别信号

数位 DP 不仅统计数量，还需要维护数值总和。

关联笔记：[[03-算法/动态规划/07-数位DP|数位DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 状态包括位置、已出现数字掩码、贴上界和是否开始，保存数量 $cnt$ 与总和 $sum$；追加数字 $d$ 时贡献为 $10sum+d\cdot cnt$，最终做区间前缀和之差。

## 复杂度

设位数为 $L$，时间 $O(L\cdot10\cdot2^{10})$，滚动空间 $O(2^{10})$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：前导零不占数字种类；数值中真正的 0 需要计入掩码；输出的是和而非数量。
- 一句话总结：待独立完成后填写。
