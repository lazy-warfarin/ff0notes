---
type: problem
platform: Codeforces
problem_id: 687C
title: The Values You Can Make
rating: 1900
tags: [dp]
status: solved
priority: important
concepts: [背包DP, 子集DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf687c_values_you_can_make/main.rs
first_solved: 2026-10-19
last_review: 2026-10-19
next_review: 2026-10-26
failure_reason:
---

# 687C The Values You Can Make

> [Codeforces 687C - The Values You Can Make](https://codeforces.com/problemset/problem/687/C)

## 题意摘要

有 $n$ 枚硬币，第 $i$ 枚价值 $c_i$，巧克力价格为 $k$（$n, k \le 500$，$c_i \le 500$，保证存在总价值恰好为 $k$ 的硬币组合）。求所有满足如下条件的 $x$：存在一个总价值为 $k$ 的硬币集合，它的某个子集总价值恰好为 $x$。先输出 $x$ 的个数，再升序输出所有 $x$。

## 识别信号

- 问题嵌套了两层"子集和"：外层选出和为 k 的集合，内层再从中选出和为 x 的子集，需要二维布尔状态。
- 每枚硬币只有三种去处：不选 / 只选进外层集合 / 同时算进内层子集。
- 值域很小（$k <= 500$），$O(n * k^2)$ 的布尔 DP 可以直接跑。

## 状态与转移

令 `dp[j][x]` 表示能否选出总价值为 j 的硬币集合，并且该集合的某个子集总价值为 x。

```text
对每枚硬币 c：
for j from k down to c:
  for x from j down to 0:
    dp[j][x] |= dp[j - c][x] || (x >= c && dp[j - c][x - c])
```

- `dp[j - c][x]`：c 只选进外层集合；`dp[j - c][x - c]`：c 同时选进内层子集。
- `j` 必须倒序，保证每枚硬币只被使用一次；`x` 维的倒序不是正确性的关键。
- 因为内层子集和值不可能大于外层集合和值，只需遍历 `0 <= x <= j`。
- 状态合并用布尔或；`x` 维代表"被标记的硬币之和"。

边界：`dp[0][0] = true`。所有 `dp[k][x]` 为 true 的 x 就是答案（包含 x = 0，即内层子集为空的情况），升序输出。

二维 01 背包的整理见 [[03-算法/动态规划/02-背包DP/04-多维与依赖背包|多维与依赖背包]]。

## 复杂度

- 时间：O(n * k^2)。
- 空间：O(k^2)，可用 bitset 进一步压缩。

## Rust 实现

- [examples/cf687c_values_you_can_make/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf687c_values_you_can_make/main.rs)
- 使用压掉物品维度的二维布尔 DP；外层按硬币处理，`j` 倒序，`x` 只扫描有效的三角区域 `0..=j`。

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
