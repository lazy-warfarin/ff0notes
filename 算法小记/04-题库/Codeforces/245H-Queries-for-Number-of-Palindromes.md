---
type: problem
platform: Codeforces
problem_id: 245H
title: Queries for Number of Palindromes
rating: 1800
tags: [dp, hashing, strings]
status: todo
priority: important
concepts: [区间DP, 回文]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 245H Queries for Number of Palindromes

> [Codeforces 245H - Queries for Number of Palindromes](https://codeforces.com/problemset/problem/245/H)

## 题意摘要

给定长度不超过 5000 的小写字符串 $s$，以及 $Q$ 次询问（$Q \le 10^6$）。每次询问给出 $l, r$，要求回答 $s[l..r]$ 这段子串中包含多少个回文子串（单个字符也算回文串，按下标计数）。

## 识别信号

- 询问"某个区间内有多少个回文子串"，需要先有回文判定表，再做区间计数合并。
- 回文判定 is_pal[l][r] 依赖 is_pal[l+1][r-1]，是区间 DP 的典型递推。
- 询问次数高达 10^6，必须 O(n^2) 预处理、O(1) 回答每次询问。

## 状态与转移

令 `is_pal[l][r]` 表示子串 s[l..r] 是否回文，`cnt[l][r]` 表示 s[l..r] 内回文子串的个数。

```text
is_pal[l][r] = (s[l] == s[r]) and (r - l <= 1 or is_pal[l + 1][r - 1])
cnt[l][r] = cnt[l + 1][r] + cnt[l][r - 1] - cnt[l + 1][r - 1] + is_pal[l][r]
```

- 按区间长度从小到大枚举 (l, r)，即可保证右边用到的子区间都已算好。
- cnt 的式子就是容斥：左半部分 + 右半部分 - 中间重复 + 当前区间自身是否为回文。
- 单字符区间 is_pal 恒为 true，cnt 为 1。

边界：空区间 is_pal = false、cnt = 0（用于长度为 2 时查 is_pal[l+1][r-1]）。每次询问直接输出 cnt[l][r]。

回文与区间的整理见 [[03-算法/动态规划/03-区间DP|区间DP]]。

## 复杂度

- 时间：O(n^2 + Q)。
- 空间：O(n^2)，is_pal 可用位压缩降低常数。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
