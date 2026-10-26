---
title: Windows与Ubuntu双系统问题
tags: [systems, windows, ubuntu, grub]
source_repo: notes
source_notes:
  - 双系统问题记录/ubuntu引导无windows.md
  - 双系统问题记录/win11取消登陆密码.md
  - 双系统问题记录/禁用默认的密钥环解锁提示.md
---

# Windows 与 Ubuntu 双系统问题

> [!warning] 历史排障记录
> 以下来自旧库，不代表已在当前系统验证。修改引导配置或登录方式前，先确认实际系统版本与恢复方式；本次迁移没有改动任何系统配置。

## GRUB 菜单没有 Windows

旧记录的第一步是在 Ubuntu 中刷新 GRUB 菜单：

```bash
sudo update-grub
```

若出现 `os-prober will not be executed to detect other bootable partitions` 警告，旧记录的排查顺序是：

1. 运行探测，确认能否找到 Windows：

   ```bash
   sudo os-prober
   ```

2. 如果确实探测到 Windows，再检查 `/etc/default/grub` 中的设置：

   ```text
   GRUB_DISABLE_OS_PROBER=false
   ```

3. 保存配置后重新生成菜单：

   ```bash
   sudo update-grub
   ```

这不是针对全部引导故障的通用修复。若探测不到 Windows，不应仅凭此笔记断言系统已丢失，也不要在未确认磁盘和启动方式前进行其他写入操作。

## Windows 11 登录设置：仅保留旧参考

原文件只有一个链接，没有记录实际采用的方法或结果：

- [Win11 取消登录密码图文教程（旧书签）](https://zhuanlan.zhihu.com/p/470573521)

“自动登录”“取消密码”和“更改 PIN/Windows Hello”不是同一操作；外部教程需结合当前版本再判断，不能把本节当成已执行步骤。

## Ubuntu 默认密钥环解锁提示：仅保留旧参考

原文件也只有一个链接：

- [禁用默认密钥环（旧书签）](https://linux.cn/article-5584-1.html)

迁移时未检查链接现状，也没有执行禁用。修改密钥环保护方式可能影响已保存凭据的安全性，使用前应先确认需求与后果。

返回 [[系统与运维/00-系统与运维索引|系统与运维索引]]。
