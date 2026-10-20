---
type: problem
platform: Codeforces
problem_id: 1036C
title: Classy Numbers
rating: 1900
tags: [combinatorics, dp]
status: todo
priority: core
concepts: [数位DP, 组合计数]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1036C Classy Numbers

> [Codeforces 1036C - Classy Numbers](https://codeforces.com/problemset/problem/1036/C)

## 题意摘要

如果一个十进制数的非零数字个数不超过 3，就称它是 classy 数。给出 $t$ 组询问 $(L, R)$，其中 $1 \le L \le R \le 10^{18}$，求区间 $[L, R]$ 内 classy 数的个数。

## 识别信号

- 统计区间内满足"数字组成限制"的数，标准做法是数位 DP + 前缀差分 `count(R) - count(L - 1)`。
- 限制只和非零数字的个数有关，而且上限只有 3，状态非常小（0..3，超过直接剪枝）。
- 位数不超过 19，状态数与位数同阶，可以直接记忆化。

## 状态与转移

令 `dfs(pos, cnt, tight)` 表示从高位到低位填到第 pos 位、已经填了 cnt 个非零数字、tight 表示前缀是否仍与上界相等时的计数。对 `tight = false`（后续位可任取）的状态做记忆化，用 `-1` 表示尚未计算。

```text
dfs(pos, cnt, tight):
  若 cnt > 3：返回 0
  若 pos 越界：返回 1
  limit = tight ? digit[pos] : 9
  返回 sum over d in 0..=limit of
       dfs(pos + 1, cnt + (d != 0), tight && (d == limit))
```

- `tight` 只在"贴着上界"时为真，此时当前位不能超过 `digit[pos]`；一旦放松，剩下的位可以任取，正好用记忆化复用。
- `cnt` 超过 3 的分支直接剪枝，这是本题状态量很小的原因。
- 前导零不影响计数：本题统计的是整数，补前导零不会改变非零数字的个数，所以不需要额外的 `started` 维。

边界：`count(x)` 统计 [0, x]，答案为 `count(R) - count(L - 1)`，注意 L = 1 时 `count(0) = 1`。

数位 DP 的通用框架见 [[03-算法/动态规划/07-数位DP|数位DP]]。

## 复杂度

- 时间：O(19 * 4 * 10)，每个询问一次差分，常数极小。
- 空间：O(19 * 4)，记忆化数组只有 76 个状态。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
