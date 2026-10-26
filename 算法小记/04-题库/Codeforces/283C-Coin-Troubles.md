---
type: problem
platform: Codeforces
problem_id: 283C
title: "Coin Troubles"
rating: 2100
tags: ["dp"]
status: todo
priority: challenge
concepts: [完全背包, 图论]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 283C Coin Troubles

> [Codeforces 283C 原题](https://codeforces.com/problemset/problem/283/C)
>
> 元数据核对：2026-10-23，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

有 $n$ 种硬币，第 $i$ 种面值为 $a_i$；给出 $q$ 个约束 $\operatorname{cnt}(b_i)>\operatorname{cnt}(c_i)$，所有 $b_i$ 互不相同、所有 $c_i$ 互不相同。求总面值恰好为 $t$ 的硬币组合数，模 $10^9+7$；无解输出 0。

## 识别信号

完全背包计数 + 严格大于约束；约束图每个点的出度、入度都至多 1，因此每个连通分量是一条链或一个环；环无解；每条链扣掉最小配置后，把前缀和当作完全背包的物品。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01 背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 建图 $b_i\to c_i$。若存在环，严格大于无法同时满足，输出 0。对每条链 $v_1\to v_2\to\cdots\to v_k$（单点也算一条链）：最小配置为 $\operatorname{cnt}(v_i)=k-i$，基础花费为
> $$
> \text{base}=\sum_{i=1}^{k}(k-i)a_{v_i}.
> $$
> 令 $x_i=\operatorname{cnt}(v_i)-\operatorname{cnt}(v_{i+1})-1$（$i<k$）、$x_k=\operatorname{cnt}(v_k)$，则
> $$
> \operatorname{cnt}(v_i)=(k-i)+\sum_{j=i}^{k}x_j,
> $$
> 总面值 $=\text{base}+\sum_{j=1}^{k}x_j\left(a_{v_1}+\cdots+a_{v_j}\right)$。所以每个前缀和 $w_j=a_{v_1}+\cdots+a_{v_j}$ 是一件可无限使用的物品，做完全背包计数：`dp[0]=1`；先令 $t\leftarrow t-\text{base}$，再对每条链的每个 $j$，按 $s=w_j..t$ 正序累加 `dp[s] += dp[s-w_j]`。答案为 `dp[t]`。

## 复杂度

- 建图与找环：$O(n+q)$。
- 完全背包：$O(nt)$；$n\le 300$、$t\le 10^5$。
- 空间：$O(t)$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：环要输出 0；单点硬币也要作为链加入；`t - base < 0` 时无解；每个前缀和对应的是“同时增加链上一段前缀”，不是单个硬币。
- 一句话总结：待独立完成后填写。
