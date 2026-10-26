---
type: problem
platform: Codeforces
problem_id: 1716D
title: "Chip Move"
rating: 2000
tags: ["brute force","dp","math"]
status: todo
priority: important
concepts: [完全背包, 计数DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 1716D Chip Move

> [Codeforces 1716D 原题](https://codeforces.com/problemset/problem/1716/D)
>
> 元数据核对：2026-10-23，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

芯片初始在 0；第 $i$ 次移动的长度必须是 $k+i-1$ 的正倍数。对每个 $x\in[1,n]$，求到达 $x$ 的路径数（两条路径不同当且仅当访问过的位置集合不同），模 $998244353$。

## 识别信号

每一步的可选长度是一个无限集合（某个数的倍数），转移带“同一步可以继续走”的完全背包特征；步数 $i$ 有上限，因为走 $i$ 步的最小总距离是 $k+(k+1)+\cdots+(k+i-1)=ik+\frac{i(i-1)}{2}\le n$，所以 $i=O(\sqrt n)$。

关联笔记：[[03-算法/动态规划/02-背包DP/01-01背包与完全背包|01 背包与完全背包]]。

## 状态与转移

> [!tip]- 展开建模提示
> 令 $f[i][j]$ 表示用恰好 $i$ 步到达 $j$ 的方案数，$w=k+i-1$。转移为
> $$
> f[i][j]=f[i][j-w]+f[i-1][j-w],
> $$
> 第一项表示继续使用当前步长的另一个倍数，第二项表示当前步长第一次出现。初始 $f[0][0]=1$，答案为 $\sum_i f[i][x]$。按 $i$ 分层滚动两行，$j$ 正序；$i$ 只枚举到 $ik+\frac{i(i-1)}{2}\le n$。

## 复杂度

- 时间：$O(n\sqrt n)$。
- 空间：$O(n)$（滚动两行）。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：步数上界按最小总距离算；滚动数组每层要清空；$j$ 必须正序才能继续使用当前步长；取模。
- 一句话总结：待独立完成后填写。
