---
type: problem
platform: Codeforces
problem_id: 833B
title: The Bakery
rating: 2200
tags: [binary search, data structures, divide and conquer, dp, two pointers]
status: todo
priority: challenge
concepts: [DP优化, 分治优化]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 833B The Bakery

> [Codeforces 833B - The Bakery](https://codeforces.com/problemset/problem/833/B)

## 题意摘要

有 $n$ 个蛋糕排成一行，第 $i$ 个蛋糕的种类是 $a_i$。要把它们按顺序切成 $k$ 段连续的非空区间，分别装进 $k$ 个盒子。一个盒子的价值是盒内不同蛋糕种类的数量。求所有盒子价值之和的最大值（$n \le 35000$，$k \le 50$，保证 $k \le n$）。

## 识别信号

- 切分对象是连续区间，段数固定，先写朴素的 `dp[段数][前缀] = 枚举最后一段起点` 的 O(k n^2) 形式。
- 代价 `distinct(t + 1, i)` 只依赖区间，且随着 t 增大会单调不增，最优分割点具备单调性，可以用分治优化把一层优化到 O(n log n)。
- 分治优化要求代价能在移动端点时增量维护：种类计数用数组 + 当前窗口的不同种类数即可 O(1) 增删（类似莫队）。

## 状态与转移

令 `dp[j][i]` 表示前 i 个蛋糕装进 j 个盒子的最大总价值。

```text
dp[j][i] = max over t in [j - 1, i - 1] of (dp[j - 1][t] + distinct(t + 1, i))
```

优化部分用分治计算（对固定的 j，`dp[j-1][*]` 已知）：

```text
solve(j, l, r, optL, optR):
  mid = (l + r) / 2
  把窗口端点移动到 [*, mid]，枚举 t in [max(optL, j - 1), min(optR, mid - 1)]
    用 freq[] 维护 distinct(t + 1, mid)，取最大值得到 opt
  solve(j, l, mid - 1, optL, opt)
  solve(j, mid + 1, r, opt, optR)
```

- 分治本身给出 O(n log n) 次枚举；窗口指针在递归过程中只做增删，总移动量与枚举量同阶。
- 每层对 j 从小到大递推，答案在 `dp[k][n]`。

边界：`dp[0][0] = 0`，`dp[0][i > 0]` 不可达；第 j 段必须非空，所以 t 的下界是 j - 1。区间为空时 distinct 为 0，不能参与转移。

决策单调性与分治优化的推导见 [[03-算法/动态规划/08-DP优化|DP优化]]。

## 复杂度

- 时间：O(k * n log n)，指针回退与移动带来的常数较小。
- 空间：O(n)，需要 dp 的一层滚动数组与种类计数数组。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
