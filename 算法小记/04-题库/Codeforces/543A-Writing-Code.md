---
type: problem
platform: Codeforces
problem_id: 543A
title: Writing Code
rating: 1800
tags: [dp]
status: solved
priority: core
concepts: [背包DP, 计数DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf543a_writing_code/main.rs
first_solved: 2026-10-16
last_review: 2026-10-16
next_review: 2026-10-23
failure_reason: "首次提交只输出恰好 b 个 bug 的方案数，忽略了题目的 bug <= b；修正为对所有 k=0..=b 求和。"
---

# 543A Writing Code

> [Codeforces 543A - Writing Code](https://codeforces.com/problemset/problem/543/A)

## 题意摘要

有 $n$ 个程序员合写 $m$ 行代码，第 $i$ 个程序员写的每一行都会引入 $a_i$ 个 bug（$n, m, b \le 500$，$a_i \le 500$）。两个方案不同当且仅当某个程序员写的行数不同。求总 bug 数不超过 $b$ 的方案数，对输入给出的 $\mathrm{mod}$ 取模（$1 \le \mathrm{mod} \le 10^9+7$，注意不是固定模数）。

## 识别信号

- 统计方案数，且限制有两个维度：总行数恰好 m、总 bug 数不超过 b，是二维背包计数。
- 同一个程序员写几行只能算一种选择，需要按人逐个加入，避免把人员顺序重复计成不同方案。
- 方案由每个程序员写了多少行决定，不区分具体代码行的排列顺序。
- 每个程序员可以写任意多行，因此按程序员处理时，代码行数这一维是完全背包式的正序转移。
- 模数 mod 由输入给出，取模时不要写死 10^9+7。

## 状态与转移

### 直观的三维 DP

令 `f[i][j][k]` 表示只使用前 `i` 个程序员，恰好写 `j` 行代码、产生恰好 `k` 个 bug 的方案数。

如果第 `i` 个程序员写 `t` 行，那么：

$$
f[i][j][k]
=
f[i-1][j-t][k-t a_i]
$$

枚举所有合法的 `t`：

$$
f[i][j][k]
=
\sum_{\substack{0\le t\le j\\t a_i\le k}}
f[i-1][j-t][k-t a_i]
$$

边界为：

```text
f[0][0][0] = 1
其余状态 = 0
```

也可以理解为 `f[i][0][0] = 1`：前 `i` 个程序员都写 0 行只有一种分配。

### 二维滚动优化

将三维转移按“当前程序员写 0 行 / 至少写 1 行”拆开：

$$
f[i][j][k]
=
f[i-1][j][k]
+
f[i][j-1][k-a_i]
$$

其中第二项要求 `k >= a_i`。它表示当前程序员至少写 1 行后，去掉当前程序员的一行，剩余状态仍然属于当前层 `i`。

因此可以压掉第一维。令 `dp[j][k]` 表示当前已处理程序员后，恰好写 `j` 行、产生 `k` 个 bug 的方案数：

```text
dp[0][0] = 1

for each programmer with a = a_i:
    for j from 1 to m:
        for k from a to b:
            dp[j][k] = (dp[j][k] + dp[j - 1][k - a]) % mod
```

- `dp[j][k]` 的旧值对应当前程序员写 0 行，即 `f[i-1][j][k]`。
- `dp[j-1][k-a]` 已经是当前程序员参与后的状态，因此 `j` 必须正序，才能允许同一个程序员写多行。
- 按程序员固定顺序加入，避免把同一个行数分配按不同处理顺序重复计数。
- `k` 也正序遍历；当 `a_i = 0` 时，`k` 从 0 开始仍然可以正确转移。

最终答案不是 `dp[m][b]`，而是 bug 数不超过 `b` 的所有状态：

$$
\text{answer}=\sum_{k=0}^{b}dp[m][k]\pmod{mod}
$$

分组与完全背包的组合见 [[03-算法/动态规划/02-背包DP/03-分组与混合背包|分组与混合背包]]，计数边界见 [[03-算法/动态规划/02-背包DP/05-计数与方案|计数与方案]]。

## 复杂度

- 时间：O(n * m * b)。
- 空间：O(m * b)。

## Rust 实现

- [examples/cf543a_writing_code/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf543a_writing_code/main.rs)
- 使用二维 `dp[行数][bug 数]`，外层枚举程序员，行数和 bug 数均正序。
- 通过题目样例和第三个边界样例：最后对 `dp[m][0..=b]` 求和，满足“bug 不超过 b”。

## 复盘

- 第一次错误：输出了 `dp[n][m][b]`，只统计恰好产生 `b` 个 bug 的方案；题目要求的是 `bug <= b`，应对 `k=0..=b` 求和。第三个样例中恰好 6 个 bug 的方案数为 5，但总方案数为 `5 + 6 = 11`，模 11 后答案为 0。
- 关键边界：`dp[0][0] = 1`；代码行数 `j` 正序；答案累加 `dp[m][0..=b]`；模数使用输入的 `mod`。
- 一句话总结：543A 是按程序员分组处理的二维完全背包式计数，先固定程序员顺序，再统计恰好写 `m` 行且 bug 数不超过 `b` 的行数分配。
