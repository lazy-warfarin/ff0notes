---
type: problem
platform: Codeforces
problem_id: 628D
title: Magic Numbers
rating: 2200
tags: [dp]
status: todo
priority: important
concepts: [数位DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 628D Magic Numbers

> [Codeforces 628D - Magic Numbers](https://codeforces.com/problemset/problem/628/D)

## 题意摘要

给定 $m$ 和 $d$（$1 \le m \le 2000$，$0 \le d \le 9$）。一个数如果同时满足下面两个条件，就称为 magic 数：

1. 从左往右编号为偶数位的位置上，数字全部等于 d；
2. 从左往右编号为奇数位的位置上，数字全部不等于 d；
3. 这个数能被 m 整除。

给出两个很长的十进制数 $a$、$b$（长度不超过 2000 位，$a \le b$），求 $[a, b]$ 内 magic 数的个数，答案对 $10^9+7$ 取模。

## 识别信号

- 限制按"数字的每一位"给出，且要统计区间内的个数，是数位 DP。
- 位置奇偶决定了当前位能填什么，位置本身已经包含在递推参数里，不需要额外的状态维。
- 还要判断整除性，加一维"前缀模 m 的余数"即可，m <= 2000 时状态量可以接受。
- 数字长度达到 2000，只能按位 DP + 滚动数组，不能把整个数转成整数。

## 状态与转移

令 `dp[pos][rem]` 表示从高位到低位处理到第 pos 位（1-indexed，从左往右）、当前前缀模 m 的余数为 rem 的方案数，同时用一个标记区分"是否仍贴着上界"。

```text
第 pos 位若为偶数位：候选数字只有 d
第 pos 位若为奇数位：候选数字是 0..9 中除去 d 的所有数字
转移：rem' = (rem * 10 + cur) % m
      dp[pos + 1][rem'] += dp[pos][rem]
```

- 从高位往低位推进，每一位只按位置的奇偶决定候选集合，天然满足题目的位置约束。
- 贴着上界的那一条路径单独维护（上界不可能取到 d 之外的候选时直接断开），其余部分用滚动数组批量递推。
- 统计区间时对 $[a, b]$ 做一次区间版 DP：维护 `lo`、`hi` 两个上界标记，或者分别求 `f(b) - f(a - 1)`（$a$ 需要高精度减一）。

边界：位置编号从左往右从 1 开始，第 2、4、6 ... 位必须是 d；a 减一时要处理借位。所有计数对 10^9+7 取模。

数位 DP 的位置与上界处理见 [[03-算法/动态规划/07-数位DP|数位DP]]。

## 复杂度

- 时间：O(len * m * 10)，len <= 2000。
- 空间：O(m)（滚动数组），贴着上界的那一路额外 O(1) 状态。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
