---
type: problem
platform: Codeforces
problem_id: 55D
title: Beautiful numbers
rating: 2500
tags: [dp, number theory]
status: todo
priority: challenge
concepts: [数位DP, 数论]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 55D Beautiful numbers

> [Codeforces 55D - Beautiful numbers](https://codeforces.com/problemset/problem/55/D)

## 题意摘要

如果一个正整数能被它自己的每一个非零数字整除，就称它是 beautiful 数（例如 24 能被 2 和 4 整除）。给出 $t$ 组询问 $(l, r)$，$r \le 9 \times 10^{18}$，求 $[l, r]$ 内 beautiful 数的个数。

## 识别信号

- 条件说的是"能否被自己的每一位非零数字整除"，即能否被这些数字的 lcm 整除，直接逼近需要记录 lcm。
- 数字的 lcm 一定是 `lcm(1..9) = 2520` 的约数，而 2520 的约数只有 48 个，可以把 lcm 压成下标。
- 同时还要判断整除性，需要一维"前缀模 2520 的余数"；因为 lcm 整除 2520，用 `rem % lcm == 0` 判断就够。
- 位数不超过 19、状态数约 19 * 2520 * 48，记忆化搜索可以承受。

## 状态与转移

令 `dfs(pos, rem, lcmIdx, tight)` 表示填到第 pos 位、前缀模 2520 的余数为 rem、当前非零数字的 lcm 是第 lcmIdx 个约数、且 tight 表示是否贴着上界时的方案数。

```text
枚举当前位数字 d：
  rem'    = (rem * 10 + d) % 2520
  lcm'    = lcm(lcm(d), d)        // d == 0 时不变
  继续 dfs(pos + 1, rem', index(lcm'), tight && d == limit)
终止：处理完所有位后，返回 rem % lcm == 0
```

- lcm 维只取 2520 的 48 个约数，用下标代替具体数值，记忆化数组才开得下。
- `rem` 取模 2520 而不是直接对 lcm 取模，是为了让状态与具体的 lcm 无关，能被所有分支复用。
- 前导零不会带来麻烦：补前导零不改变数值，也不影响非零数字的 lcm。

边界：答案为 `count(r) - count(l - 1)`；lcmIdx 的初值为 1（空集的 lcm 记为 1）。需要预先枚举 2520 的所有约数并建立"约数 -> 下标"的映射表。

数位 DP 的状态设计与取模维度见 [[03-算法/动态规划/07-数位DP|数位DP]]。

## 复杂度

- 时间：O(19 * 2520 * 48 * 10)，约 2.3 * 10^7 次转移。
- 空间：O(19 * 2520 * 48)，用 64 位整数记忆化约 18 MB。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
