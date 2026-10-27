---
type: problem
platform: Codeforces
problem_id: 85D
title: Sum of Medians
rating: 2300
tags: [binary search, brute force, data structures, implementation]
status: todo
priority: challenge
concepts: [红黑树, 增广平衡树, 排名模分类, 信息合并]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 85D Sum of Medians

> [Codeforces 85D - Sum of Medians](https://codeforces.com/problemset/problem/85/D)
>
> 元数据核对：2026-10-26，title / rating / tags 来自 [Codeforces 官方 problemset API](https://codeforces.com/api/problemset.problems)，题意和约束按官方题面核对。作为手写增广红黑树的练习，不代表官方指定这一实现。

## 题意摘要

维护一个初始为空、元素互异的集合，支持 `add x`、`del x`、`sum`。把当前集合从小到大排为 $a_1,\ldots,a_s$，`sum` 查询的是 1-based 排名为 $3,8,13,\ldots$ 的元素之和，即：

$$
\sum_{\substack{1\le i\le s\\ i\bmod5=3}}a_i.
$$

最多 $10^5$ 次操作，$1\le x\le10^9$；插入前保证 $x$ 不在集合，删除前保证 $x$ 在集合。空集输出 $0$。并不是求整个集合的单个中位数；不足五个元素的尾部只要存在对应的第 $3$ 项，也按排名公式计入。

## 识别信号

- 插入或删除一个较小的键，会让后面所有元素的全局排名平移，不能把每个元素永久归入固定模类。
- 需要在子树中维护“按局部中序排名模 $5$ 分类的和”，合并时再调整偏移。
- 除了 `size`，还要增广一个长度为 $5$ 的数组；它检验的是旋转、删除和 `pull` 的配合，不只是第 $k$ 小。
- 可用增广红黑树；也可离散化后用维护相同分类信息的线段树。只反复调用 `kth` 再求和会使单次查询退化。

关联笔记：[[02-数据结构/树/01-红黑树|红黑树：自定义信息增广]]。

## 状态与转移

本题没有重复键，可以直接在基础 `RbTree` 上增加 `size` 与分类聚合，**不必增加 `cnt`**；每个真实结点的权重直接取 $1$。统一使用**0-based 局部排名**，定义 $f_u[r]$ 为子树 $u$ 中局部排名模 $5$ 等于 $r$ 的键之和，$0\le r<5$。

空子树 `size == 0`，五个和全为 $0$。设左右子树为 $L,R$，左子树大小为 $\ell$，当前键为 $x$。合并时清空 $f_u$，再执行：

1. 左子树局部排名不变：$f_u[r]\mathrel{+}=f_L[r]$。
2. 当前键排名为 $\ell$：$f_u[\ell\bmod5]\mathrel{+}=x$。
3. 右子树整体右移 $\ell+1$ 位：$f_u[(r+\ell+1)\bmod5]\mathrel{+}=f_R[r]$。
4. 更新 $\mathrm{size}[u]=\mathrm{size}[L]+1+\mathrm{size}[R]$。

这里第 1、3 步对所有 $r\in\{0,1,2,3,4\}$ 执行。查询答案为 $f_{\mathrm{root}}[2]$，因为题面的 1-based 第 $3$ 项对应 0-based 第 $2$ 项。

旋转时先 `pull` 下降结点，再 `pull` 上升结点；结构删除、搬后继键及祖先路径都要更新。染色本身不改变这些聚合值。

## 复杂度

设操作数为 $q$、当前集合大小为 $s$：每次插入 / 删除 $O(5\log(s+1))$，`sum` 为 $O(1)$；总时间 $O(q\log(q+1))$，结点池空间至多 $O(q)$，不计输入缓冲。

分类和使用 `i64`。当前元素数不超过 $10^5$，每个模类至多有 $2\cdot10^4$ 项，因此单个分类和的安全上界为 $2\cdot10^{13}$，不能用 32 位整数。

## Rust 实现

- 尚未实现，`code_path` 留空；本次不创建 Rust 源文件。
- 在基础 `RbTree` 稳定后，先加入 `size`，再添加 `sum_by_rank: [i64; 5]`；保持有序集合语义，不需要多重集合的 `cnt` / `remove_one`，也不要第一天就同时调试删除与这一合并式。
- 每次合并先初始化 `[0_i64; 5]`，避免把上一轮缓存再次累加。
- 小数据基准用排序 `Vec<i64>`，对 0-based 下标模 $5$ 等于 $2$ 的元素求和；每一步与根的聚合值对拍。

## 复盘

- 第一次错误：待完成后记录。
- 关键边界：空集；集合大小为 $1$、$2$、$3$、$4$；局部 / 全局排名的偏移；删除最小值使所有后继换模类；多次旋转后聚合值是否保持；大数累加。
- 一句话总结：维护子树局部排名模 $5$ 的分类和，合并时给右子树加上左子树大小与当前结点造成的偏移。
