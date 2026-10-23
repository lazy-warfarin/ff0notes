---
type: problem
platform: Codeforces
problem_id: 453B
title: "Little Pony and Harmony Chest"
rating: 2000
tags: ["bitmasks","brute force","dp"]
status: todo
priority: important
concepts: [计数与方案, 状态压缩DP]
code_path:
first_solved:
last_review:
next_review:
failure_reason:
---

# 453B Little Pony and Harmony Chest

> [Codeforces 453B 原题](https://codeforces.com/problemset/problem/453/B)
>
> 元数据核对：2026-10-22，title / rating / tags 来自 Codeforces 官方 problemset API，题意按官方题面核对。

## 题意摘要

将给定序列改为正整数序列，使任意两个数互质，最小化逐项绝对差之和，并输出一组最优序列。

## 识别信号

质因子集合互斥；有限候选值配合位掩码和方案还原。

关联笔记：[[03-算法/动态规划/02-背包DP/05-计数与方案|计数与方案]]、[[03-算法/动态规划/06-状态压缩DP|状态压缩DP]]。

## 状态与转移

> [!tip]- 展开建模提示
> 由于原值不超过 30，只需枚举候选 1 到 59；用这一区间的 17 个质数构造掩码，只有与已用质数不相交的候选才可加入；分层保存所选值用于回溯。

## 复杂度

基础时间 $O(59n2^{17})$，滚动值表空间 $O(2^{17})$，保存选择需 $O(n2^{17})$。

## Rust 实现

尚未实现，`code_path` 留空；通过后再登记真实代码路径。

## 复盘

- 第一次错误：待练习后填写。
- 关键边界：1 的掩码为 0，可以重复出现；不能把“所有数 gcd 为 1”误作“两两互质”；回溯必须保存层信息。
- 一句话总结：待独立完成后填写。
