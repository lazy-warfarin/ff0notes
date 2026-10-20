---
type: problem
platform: Codeforces
problem_id: 455B
title: A Lot of Games
rating: 1900
tags: [dfs and similar, dp, games, implementation, strings, trees]
status: todo
priority: important
concepts: [博弈DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 455B A Lot of Games

> [Codeforces 455B - A Lot of Games](https://codeforces.com/problemset/problem/455/B)

## 题意摘要

给出 $n$ 个非空字符串（总长度不超过 $10^5$），用它们建一棵 trie。两人轮流走：从根出发，每步沿着一条边走一步，走过的路径必须始终是某个给定字符串的前缀；轮到自己却无路可走的人输掉这一局。两人要连续玩 $k$ 局，输掉一局的人获得下一局的先手，赢得最后一局的人赢得整场。问先手是否必胜。

## 识别信号

- 局面只由"当前停在 trie 的哪个节点"决定，是树上博弈，可以自底向上递推。
- 整场胜负只取决于最后一局，而先手可以利用"故意输掉前面几局来换取先手权"，因此必须同时算出"能否逼自己赢"和"能否逼自己输"两个标记。
- k 的作用只有奇偶性，不需要模拟 k 局。

## 状态与转移

在 trie 的每个节点 u 上定义两个布尔量（均以"轮到在 u 处走的人"为主语）：

- `win[u]`：此人能否迫使自己赢下这一局；
- `lose[u]`：此人能否迫使自己输掉这一局。

```text
叶子（无出边）：win = false, lose = true     // 无路可走，直接输
非叶子：
  win[u]  = 存在孩子 v，使 win[v]  == false
  lose[u] = 存在孩子 v，使 lose[v] == false
```

- 走到孩子 v 后轮到对手行动，所以 `win[u]` 要找"对手无法逼自己赢"的孩子，`lose[u]` 要找"对手无法逼自己输"的孩子。
- 两个标记都由孩子唯一决定，DFS 后序一遍即可全部算出。

整体胜负（设 trie 根为根节点）：

```text
若 win[1] == false            -> Second
否则若 lose[1] == true        -> First     // 两种结局都能选，总能赢下最后一局
否则（能赢不能输）            -> k 为奇数时 First，否则 Second
```

- `win[1]` 为假说明先手无论怎么下都赢不了这一局，只能输掉整场。
- 两种结局都能选时，先手可以按需要安排每一局的结果，从而确保自己是最后一局的胜者。
- "能赢不能输"时先手每局必胜，先手权因此在两人之间交替，只有 k 为奇数才轮到先手赢下最后一局。

trie 上的自底向上递推与 [[03-算法/动态规划/05-树形与图DP|树形与图DP]] 的子树合并思路一致。

## 复杂度

- 时间：O(总字符数)，建 trie 与一次 DFS。
- 空间：O(总字符数 * 26)，用 `Vec<[i32; 26]>` 或孩子链表存储。

## Rust 实现

- 实现状态：待补，本题解尚未提交到 Rust 项目。
- 计划位置：`D:\projects\Rust\algorithm-notes\algs\动态规划`

## 复盘

- 第一次错误：
- 关键边界：
- 一句话总结：
