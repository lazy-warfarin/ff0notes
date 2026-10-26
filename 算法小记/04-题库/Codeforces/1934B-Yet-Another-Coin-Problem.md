---
type: problem
platform: Codeforces
problem_id: 1934B
title: "Yet Another Coin Problem"
rating: 1200
tags: ["brute force","dp","greedy","math"]
status: todo
priority: core
concepts: [完全背包]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1934B Yet Another Coin Problem

> [Codeforces 1934B 原题](https://codeforces.com/problemset/problem/1934/B)
>
> 元数据核对：2026-10-23，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

有面值为 $1,3,6,10,15$ 的五种硬币，每种数量无限；每个询问给出 $n$（$n \le 10^9$），求恰好凑出 $n$ 的最少硬币数。

## 识别信号

完全背包/硬币找零；$n$ 很大，不能直接开 $O(n)$ 的容量数组；面值里有 15，最优解中非 15 硬币的数量有常数上界，可以只在小范围做完全背包，再按 15 的个数调整。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01 背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 先预处理 $dp[i]$（$0 \le i \le 15 \times 14 + 14$）为凑出 $i$ 的最少硬币数。对每个 $n$，令 $q=\lfloor n/15 \rfloor$、$r=n \bmod 15$，枚举少用 $j$ 个 15（$0 \le j \le \min(14,q)$）：
> $$
> \text{ans}=\min_{0\le j\le \min(14,q)}\left(q-j+dp[r+15j]\right).
> $$
> 最优解中非 15 硬币不超过 14 枚：若有 15 枚非 15 硬币，其总面值不超过 $15\cdot 10=150$，可换成 10 枚 15，硬币数反而更少。因此枚举 $j\le\min(14,q)$ 不会漏掉最优解（$j$ 不能超过 $q$）。

## 复杂度

- 预处理：容量约 $15\cdot 14+14=224$，每种面值扫一遍，$O(224\cdot 5)$。
- 每个询问：枚举 15 个调整量，$O(15)$；总时间 $O(224\cdot 5+15t)$。
- 空间：$O(224)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：$n<15$；不能直接写 $q+dp[r]$（$n=20$ 会得到 4，正确是 2）；调整量 $j$ 不超过 $\min(14,q)$；答案用 64 位。
- 一句话总结：待独立完成后填写。
