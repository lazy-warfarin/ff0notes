---
title: frp内网穿透
tags: [operations, frp, ssh, networking]
status: historical-reference
source_repo: notes
source_notes:
  - 建站记录/frp内网穿透.md
---

# frp 内网穿透

> [!warning] 只保留连接模型，不直接用于公网部署
> 原笔记同时出现 0.57.0 的说明与 0.15.1 的解压命令，下载地址也没有写完整。本次去掉失配的安装命令和原服务器地址。以下保留 TOML 配置思路，尚未在当前版本实测，未包含认证、访问控制及完整安全配置。

## 连接模型

- 公网主机运行 `frps`，示例控制端口为 `7000`。
- 内网主机运行 `frpc`，主动连接公网主机。
- 内网主机上的 SSH 服务监听本地 `22` 端口，通过公网主机的 `6000` 端口访问。

`remotePort` 是配置中明确指定的端口，不是连接时自动随机分配的端口。同一公网监听端口不能重复分给多个代理。

## 版本与安装

先选择同一版本、与两端操作系统和 CPU 架构对应的发布包，再核对该版本的配置语法。旧记录未留下可复用的完整安装步骤，不保留看起来能直接运行的伪下载地址。

## 服务端配置：frps.toml

```toml
bindPort = 7000
```

这是端口关系的最小片段，不是安全完整配置。

## 客户端配置：frpc.toml

```toml
serverAddr = "frp.example.com"
serverPort = 7000

[[proxies]]
name = "ssh-home"
type = "tcp"
localIP = "127.0.0.1"
localPort = 22
remotePort = 6000
```

`frp.example.com` 是占位地址，使用前必须替换。客户端应连接内网目标服务，不能把公网地址填到 `localIP`。

## 启动与检查

Linux 前台运行：

```bash
# 公网主机
./frps -c ./frps.toml

# 内网主机
./frpc -c ./frpc.toml
```

旧记录的临时后台方式为：

```bash
nohup ./frps -c ./frps.toml > frps.log 2>&1 &
```

保留日志比直接重定向到 `/dev/null` 更便于排障。停止进程前先确认进程号，通常先发送正常终止信号，不默认使用旧笔记中的 `kill -9`。

## 通过公网入口连接内网 SSH

```bash
ssh -p 6000 user@frp.example.com
```

这里的 `user` 是**内网 SSH 服务所在机器**上的用户，不是 frps 主机的用户。frp 的转发端口与 SSH 服务本身是两个不同层次。

## Windows 登录后启动 frpc

旧记录采用当前用户的“启动”文件夹：按 `Win + R`，输入 `shell:startup`，放入批处理文件。

```bat
@echo off
start "" /b "C:\path\to\frpc.exe" -c "C:\path\to\frpc.toml"
```

路径均为占位示例。双引号用于含空格路径，`start` 后的第一个空字符串用于窗口标题。此方式是**用户登录后启动**，不是系统服务，也不等于无需登录就能后台运行。

## 排障与安全检查

- [ ] 确认实际版本与配置格式匹配。
- [ ] 确认公网主机的安全组及主机防火墙只放行确有需要的端口。
- [ ] 确认内网目标机器的 OpenSSH Server 正在监听；frps 主机不因做 TCP 转发就必须运行目标 SSH 服务。
- [ ] 确认要使用的账户能直接登录目标 SSH 服务，再排查转发链路。
- [ ] 配置该版本支持的认证与访问控制，避免把最小示例直接暴露到公网。

原有参考：[frp 内网穿透（旧参考）](https://blog.csdn.net/weixin_42265958/article/details/106008837)。

返回 [[系统与运维/00-系统与运维索引|系统与运维索引]]。
