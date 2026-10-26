---
title: Docker部署MySQL
tags: [operations, docker, mysql]
status: historical-reference
source_repo: notes
source_notes:
  - 建站记录/docker-mysql.md
---

# Docker 部署 MySQL

> [!warning] 历史配置，使用前复核
> 旧笔记混用了普通实例与测试实例的宿主机路径，并写入过明文口令。本次已统一示例路径、移除口令；下列示例未在当前 Docker/MySQL 环境执行，不是生产部署方案。

## 目录对应关系

以宿主机 `/docker/mysql` 为例：

| 用途 | 宿主机目录 | 容器内目录 |
| --- | --- | --- |
| 数据 | `/docker/mysql/data` | `/var/lib/mysql` |
| 配置 | `/docker/mysql/conf` | `/etc/mysql/conf.d` |
| 日志挂载位置 | `/docker/mysql/log` | `/var/log/mysql` |

日志是否写入该目录还取决于 MySQL 的日志配置，不能仅凭挂载就认为日志已启用。

```bash
mkdir -p /docker/mysql/log /docker/mysql/data /docker/mysql/conf
```

## 原有字符集配置

配置文件为 `/docker/mysql/conf/custom.cnf`：

```ini
[mysqld]
init-connect="SET collation_connection=utf8mb4_0900_ai_ci"
init_connect="SET NAMES utf8mb4"
```

这是旧笔记保存的配置片段，`utf8mb4_0900_ai_ci` 需与实际 MySQL 版本兼容；两个 `init_connect` 写法是否重复、实际生效结果如何，应按目标版本复核。这里不把它当成已经验证的字符集配置，也不照搬到其他数据库版本。

## 启动示例

先按所需版本确认镜像标签，并通过安全方式准备环境变量 `MYSQL_ROOT_PASSWORD`；笔记和脚本中不要填写真实密码。下面的标签是明确选用的示例，不代表已检查当前支持周期。

```bash
# 在 Linux shell 中执行；环境变量未设置时停止。
: "${MYSQL_ROOT_PASSWORD:?请先通过安全方式设置 MYSQL_ROOT_PASSWORD}"
export MYSQL_ROOT_PASSWORD

docker run \
  --restart=always \
  --name mysql \
  -v /docker/mysql/log:/var/log/mysql \
  -v /docker/mysql/data:/var/lib/mysql \
  -v /docker/mysql/conf:/etc/mysql/conf.d \
  -p 127.0.0.1:3306:3306 \
  -e MYSQL_ROOT_PASSWORD \
  -d mysql:8.0
```

- 只把端口绑定到宿主机回环地址，避免沿用旧例中的默认对外监听；远程访问需另外设计网络与权限。
- 环境变量传参只是避免把口令直接写进笔记或命令行参数，不等于完整的密钥管理方案。
- 数据目录应单独备份；容器能重启不等于数据库已经有可恢复备份。

## 测试实例的对应改动

旧笔记另有 `mysql-test`、宿主机端口 `33060` 的例子，整理后应保持：

- 宿主机目录统一使用 `/docker/mysql-test/{log,data,conf}`，配置文件也写入该目录。
- 容器名称改为 `mysql-test`。
- 容器内部仍使用 `/var/lib/mysql`、`/etc/mysql/conf.d`、`/var/log/mysql`，不要跟着改成 `mysql-test`。
- 端口按需要改为 `127.0.0.1:33060:3306`。
- 单独准备测试口令，不复用旧笔记中的值。

## 原有参考

- [Docker 安装 MySQL（旧参考）](https://blog.csdn.net/u014282578/article/details/127920419)
- [[系统与运维/00-系统与运维索引|系统与运维索引]]
