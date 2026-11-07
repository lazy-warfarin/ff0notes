# 题库说明

每道题只维护一张卡片：内容、状态、复盘都写在卡片里，题单和知识点笔记只引用卡片。

## 命名规则

`04-题库/{平台}/{contestId}{index}-{Slug}.md`

例如：`04-题库/Codeforces/455A-Boredom.md`。

## 字段约定

| 字段 | 说明 |
| --- | --- |
| `status` | `todo` / `doing` / `solved` / `redo` / `mastered` |
| `priority` | `core` / `important` / `challenge` |
| `concepts` | 关联的知识点，例如 `[线性DP]` |
| `code_path` | Rust 实现路径；留空表示尚未实现 |
| `first_solved` | 首次通过日期，格式 `YYYY-MM-DD` |
| `next_review` | 下次复习日期，格式 `YYYY-MM-DD` |
| `failure_reason` | 第一次失败的主要原因，一句话 |

## 更新流程

1. 从题单或状态看板进入对应卡片。
2. 先补全题意、识别信号、状态与转移，再写代码。
3. 通过后更新 `status`、`first_solved`、`code_path` 和 `next_review`。
4. 做错过的题，把原因写进 `failure_reason` 和"复盘"章节。
5. 同一类错误重复出现时，同步补充到对应专题笔记的"常见错误"。
