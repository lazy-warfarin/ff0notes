---
type: problem
platform: Codeforces
problem_id: 977F
title: Consecutive Subsequence
rating: 1700
tags: [dp]
status: todo
priority: important
concepts: [序列DP, 哈希]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 977F Consecutive Subsequence

> [Codeforces 977F - Consecutive Subsequence](https://codeforces.com/problemset/problem/977/F)

## 题意摘要

给定长度 $n$ 的数组 $a$（$n \le 2 \times 10^5$，$1 \le a_i \le 10^9$）。要选出最长的子序列，使它的值恰好是连续的整数序列 $[x, x+1, \ldots, x+k-1]$，元素在原数组中不必相邻，但下标必须保持递增。输出长度 $k$，以及任意一组合法方案的 1-based 下标序列（输出的是下标，不是元素值）。

例如样例一输出下标 `2 3 5 6`，对应的元素值是 `3 4 5 6`；值每次加 1，而下标不要求连续。

## 识别信号

- 要求子序列的值连续递增；从左到右扫描时，只需查询已扫描前缀中以值 `a_i - 1` 结尾的最长链，适合以值为下标的 DP。
- 值域到 10^9，不能开数组，需要用哈希表（HashMap）维护 dp 值。
- 需要输出方案，所以还要记录每个值对应的下标，方便回溯。

## 状态与转移

令 `dp[x]` 表示当前已扫描前缀中，以值 x 结尾的最长连续子序列长度，`last[x]` 表示当前达成 `dp[x]` 的元素下标，`pre[i]` 表示下标 i 在恢复链上的前驱。

```text
从左到右扫描 a[i]：
newLen = dp[a[i] - 1] + 1          // dp[a[i] - 1] 不存在时视为 0
若 newLen > dp[a[i]]：
    dp[a[i]]   = newLen
    pre[i]     = last[a[i] - 1]    // 当前链尾下标，0 表示没有前驱
    last[a[i]] = i
    若 newLen 刷新了全局最大值：best = i
```

- 每个元素只贡献一次扩展，等价于在"值维度"上做最长路。
- `pre[i]` 在算出 `dp[a[i]]` 的那一刻冻结前驱，之后 `last[a[i]-1]` 再变化也不会破坏恢复链。
- 回溯：从 `best` 出发沿 `pre` 一路向前，收集 1-based 下标后反转，得到严格递增的答案。

边界：缺失的 dp 值按 0 处理。答案长度是 dp 的全局最大值，方案下标沿 `pre` 链得到。

更完整的序列模型整理见 [[03-算法/动态规划/04-序列DP|序列DP]]。

## 复杂度

- 时间：O(n)（哈希表均摊）。
- 空间：O(n)。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
