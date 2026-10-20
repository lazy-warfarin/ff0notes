---
type: problem
platform: Codeforces
problem_id: 1195C
title: Basketball Exercise
rating: 1400
tags: [dp]
status: solved
priority: core
concepts: [线性DP]
code_path: D:/projects/Rust/algorithm-notes/examples/cf1195c_basketball_exercise/main.rs
first_solved: 2026-10-13
last_review: 2026-10-13
next_review: 2026-10-20
failure_reason:
---

# 1195C Basketball Exercise

> [Codeforces 1195C - Basketball Exercise](https://codeforces.com/problemset/problem/1195/C)

## 题意摘要

两排各 $n$ 名学生，第 1 排第 $i$ 人的身高是 $h_{1,i}$，第 2 排是 $h_{2,i}$（$n \le 10^5$，$h_{1,i}, h_{2,i} \le 10^9$）。要从两排中挑选学生：选择的列号必须严格递增，且不允许连续两次选择来自同一排；可以整列跳过。求被选学生身高总和的最大值。

## 识别信号

- 选择有天然顺序（列号递增），限制只和"上次选的是哪一排"有关，状态里带上末状态标记即可。
- 每列最多选一人，也可以整列不选，所以每列有三种情况：不选 / 选第 1 排 / 选第 2 排。
- n 很大但状态数极少，O(n) 线性 DP 即可通过。

## 状态与转移

令 `dp[i][0/1/2]` 表示考虑前 i 列，第 i 列分别（0）不选、（1）选第 1 排、（2）选第 2 排时的最大总身高。

```text
dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + h1[i]
dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + h2[i]
```

- dp\[i]\[0]：第 i 列跳过，前一列任何状态都能接。
- dp\[i]\[1] / dp\[i]\[2]：相邻列不能选同一排，所以不能从 dp\[i-1]\[1] / dp\[i-1]\[2] 转移。
- 身高都是正数：两个同排选择之间只要隔了至少一列，在中间插入一个另一排的球员一定更优，因此转移只需在相邻列之间禁止同排。

边界：`dp[0][0] = dp[0][1] = dp[0][2] = 0`。按 i 递增遍历，答案是 `max(dp[n][0], dp[n][1], dp[n][2])`。

### 两状态压缩

也可以不单独维护“第 i 列不选”的状态，而把它隐藏在 `dp1[i - 1]` / `dp2[i - 1]` 的保留分支中。定义：

- `dp1[i]`：考虑前 i 列，最后一次选择来自第 1 排（允许第 i 列跳过）时的最大总身高。
- `dp2[i]`：考虑前 i 列，最后一次选择来自第 2 排（允许第 i 列跳过）时的最大总身高。

选择第 i 列第 1 排的学生时，前一个选择有两种合法来源：第 i - 1 列来自第 2 排，或第 i - 2 列来自第 1 排。若直接跳过第 i 列，则保留原状态：

```text
dp1[i] = max(dp1[i - 1], max(dp1[i - 2], dp2[i - 1]) + h1[i])
dp2[i] = max(dp2[i - 1], max(dp2[i - 2], dp1[i - 1]) + h2[i])
```

其中：

- `dp1[i - 1]` / `dp2[i - 1]`：跳过当前列，沿用之前的最优解；
- `dp1[i - 2] + h1[i]`、`dp2[i - 2] + h2[i]`：同一排至少间隔一列；
- `dp2[i - 1] + h1[i]`、`dp1[i - 1] + h2[i]`：相邻列切换到另一排。

因此，三状态和两状态只是两种状态定义：三状态把“跳过当前列”显式列出，两状态把它作为 carry 分支保留下来。两状态滚动实现时必须先保存上一轮的两个旧值，避免更新 `dp1` 后污染 `dp2` 的转移。

基本模型见 [[03-算法/动态规划/01-线性DP|线性DP]]。

## 复杂度

- 时间：O(n)。
- 空间：O(n)，滚动三个变量后为 O(1)。

## Rust 实现

- [examples/cf1195c_basketball_exercise/main.rs](file:///D:/projects/Rust/algorithm-notes/examples/cf1195c_basketball_exercise/main.rs)
- 使用两状态 DP；`dp1[i - 1]` / `dp2[i - 1]` 隐含跳过当前列，时间 O(n)，数组空间 O(n)，滚动后可压到 O(1)。
- 代码已通过 `cargo check --example cf1195c_basketball_exercise`。

## 复盘

- 第一次错误：最初把“不选当前列”单独列成第三个状态，后来确认它可以通过两状态的 carry 分支隐含。
- 关键边界：第 1 列初始化为 `h1[1]`、`h2[1]`；转移时必须使用上一轮的 `dp1[i - 1]` 和 `dp2[i - 1]`。
- 一句话总结：状态定义允许“最后一次选该排但当前列可以跳过”时，不选状态可以被压进两状态转移。
