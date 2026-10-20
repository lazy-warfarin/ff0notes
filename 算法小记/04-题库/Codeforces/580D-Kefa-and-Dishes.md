---
type: problem
platform: Codeforces
problem_id: 580D
title: Kefa and Dishes
rating: 1800
tags: [bitmasks, dp]
status: solved
priority: core
concepts: [状态压缩DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf580d_kefa_and_dishes/main.rs
first_solved: 2026-10-20
last_review: 2026-10-20
next_review: 2026-10-27
failure_reason:
---

# 580D Kefa and Dishes

> [Codeforces 580D - Kefa and Dishes](https://codeforces.com/problemset/problem/580/D)

## 题意摘要

菜单上有 $n$ 道菜（$n \le 18$），第 $i$ 道菜本身的满意度是 $a_i$。Kefa 要选择并吃掉恰好 $m$ 道互不相同的菜（$m \le n$），另外有 $k$ 条形如"先吃 $x$ 紧接着吃 $y$"的加成规则，满足时额外获得 $c$（同一有序对 $(x,y)$ 至多一条规则）。求能获得的最大满意度总和。

## 识别信号

- $n \le 18$，状态天然是"已经吃掉了哪些菜"的集合，典型的状态压缩 DP。
- 加成只取决于"上一道菜是什么"，所以状态里必须额外记录最后一道菜。
- "恰好选 m 道"是集合大小的限制：集合大小达到 `m` 后不再向后转移，只在 `popcount(mask) == m` 的状态上取答案。

## 状态与转移

令 `dp[mask][last]` 表示已经吃掉的集合为 mask、最后一道菜是 last 时的最大满意度（mask 必须包含 last）。

```text
初始化：dp[1 << i][i] = a[i]
转移：对每个 mask 与 last in mask：
  for j not in mask:
    gain = a[j] + bonus[last][j]
    dp[mask | (1 << j)][j] = max(dp[mask | (1 << j)][j], dp[mask][last] + gain)
```

- 每次从集合外挑一道新菜接在后面，`bonus[last][j]` 就是题目给的加成（没有规则时为 0）。
- 起点是任意一道单菜集合，相当于枚举"第一道菜"，无需额外处理边界。
- 只从 `popcount(mask) < m` 的集合继续转移；集合大小达到 `m` 后停止扩展。按 `mask` 升序枚举即可，因为每次转移都在加入一个新元素。

边界：答案取所有 `popcount(mask) == m` 的 `dp[mask][last]` 的最大值。单道菜的 `a_i`、加成 `c` 最大为 $10^9$，总和需要 64 位整数。

集合作为状态的写法见 [[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。本题与 0/1 背包相同的地方是每道菜至多选一次，但收益还取决于相邻顺序，因此不能只记录集合。

## 复杂度

- 时间：O(2^n * n^2)。
- 空间：O(2^n * n)，代码把 `mask` 和 `last` 展平成一维 `i64` 数组。

## Rust 实现

- [examples/cf580d_kefa_and_dishes/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf580d_kefa_and_dishes/main.rs)
- 运行：`cargo run --example cf580d_kefa_and_dishes`
- 状态使用 `dp[mask][last]`，其中 `mask` 记录已吃过的菜，`last` 记录最后一道菜；代码以 `i64` 一维数组展平存放。
- 已通过官方两组样例，并与 400 组随机小数据的暴力枚举结果一致。

## 复盘

- 第一次错误：曾考虑只用 `dp[i][mask]` 表示前 `i` 道菜和已选集合，但这样无法区分同一集合的不同进食顺序。
- 关键边界：`mask` 必须包含 `last`；集合大小达到 `m` 后停止转移，答案只在大小为 `m` 的状态中取。
- 一句话总结：先按集合压缩“吃过哪些菜”，再用最后一道菜保留顺序带来的相邻加成。
