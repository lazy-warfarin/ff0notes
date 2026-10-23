---
type: problem
platform: Codeforces
problem_id: 706C
title: "Hard problem"
rating: 1600
tags: ["dp","strings"]
status: todo
priority: core
concepts: [线性DP, 序列DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 706C Hard problem

> [Codeforces 706C 原题](https://codeforces.com/problemset/problem/706/C)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

不改变字符串原顺序，可以付出对应费用将某些字符串反转，使整个序列字典序非降，求最小费用，无解输出 -1。

## 识别信号

沿位置递推，当前位置只需记录是否反转。

关联笔记：[[03-算法/动态规划/01-线性DP|线性DP]]、[[03-算法/动态规划/04-序列DP|序列DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $f_{i,0/1}$ 表示处理到第 $i$ 串且该串不反转或反转的最小费用；枚举前后两串的四种方向，仅在字典序合法时转移。

## 复杂度

设总字符数为 $L$，时间 $O(n+L)$，保存字符串空间 $O(n+L)$，DP 可滚动。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：相等字符串允许相邻；前缀长短影响字典序；费用和使用 64 位，不可达状态不能参与加法。
- 一句话总结：待独立完成后填写。
