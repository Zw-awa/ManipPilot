# ManipPilot

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md)

[![状态](https://img.shields.io/badge/status-planning%20%2F%20prototyping-4c8bf5)](#当前状态)
[![许可证](https://img.shields.io/badge/license-Apache--2.0-1976d2)](./LICENSE)
![任务](https://img.shields.io/badge/tasking-declarative-2e7d32)
![中间件](https://img.shields.io/badge/middleware-ROS%202-1565c0)
![操作](https://img.shields.io/badge/manipulation-task%20executive-f57c00)

`ManipPilot` 是一个面向 `ROS 2` 机器人操作任务的声明式任务执行工具，让机器人任务从一次性脚本变成可安装、可复用、可回放、可恢复的工作流。

## 目录

- [ManipPilot](#manippilot)
  - [目录](#目录)
  - [这个项目是什么](#这个项目是什么)
  - [它想做到什么](#它想做到什么)
  - [第一版重点聚焦什么](#第一版重点聚焦什么)
  - [当前状态](#当前状态)
  - [项目目录结构](#项目目录结构)
  - [快速开始](#快速开始)
    - [1. 克隆仓库](#1-克隆仓库)
    - [2. 阅读总览](#2-阅读总览)
    - [3. 关注文档](#3-关注文档)
    - [4. 如果想参与贡献](#4-如果想参与贡献)
  - [贡献](#贡献)
  - [安全提示](#安全提示)
  - [许可证](#许可证)

## 这个项目是什么

这个仓库是 `ManipPilot` 的主页。

ManipPilot 的目标，是让受支持的 `ROS 2` 机器人操作任务更容易安装、复用、回放和恢复。

它更适合这样一类使用者：

- 已经有或准备搭建机器人操作栈的开发者
- 希望把临时脚本整理成可重复执行任务的人
- 需要回放和复盘执行过程的人
- 希望在失败时有清晰恢复路径的人

项目后续会围绕下面这些用户价值展开：

- 声明式任务描述
- 面向操作任务的可复用执行流程
- 面向调试与复盘的可回放运行记录
- 在受支持失败场景下更清晰的恢复行为
- 具有清楚输入输出边界的工作流

`README` 主要描述项目范围、使用方向与贡献入口。

## 它想做到什么

ManipPilot 面向的是一个更稳定的任务执行流程：

- 用结构化方式描述一个操作任务
- 通过受支持的 `ROS 2` 机器人操作栈执行这个任务
- 让执行过程更容易观察、复盘和定位问题
- 在任务步骤失败时提供更明确的恢复路径
- 帮助用户把脆弱的一次性脚本升级为可重复使用的工作流

常见示例包括：

- 从已知工作区抓取目标物体
- 把物体放到指定位置
- 运行一段多步骤桌面操作任务
- 在任务无法继续时进行重试或安全退出
- 对历史执行结果进行回放与复盘

## 第一版重点聚焦什么

第一版会刻意收敛，当前主要聚焦这些事情：

- 一条面向 `ROS 2` 机器人操作任务的执行路径
- 一套以命令行为主的工作流
- 一种可回放的任务运行模型
- 一种可恢复的任务执行方式
- 一个以桌面机械臂为首个验证场景的初始基线

这也意味着，第一版暂时不会同时覆盖下面这些方向：

- 所有类型的机器人形态
- 宽泛的自主感知承诺
- 不受约束的自然语言交互
- 一次性覆盖所有规划或编排风格
- 在第一条可复现基线稳定前做过宽的支持承诺

第一条验证路径会先聚焦桌面机械臂，但项目身份本身并不只限定在桌面场景。

## 当前状态

`规划中 / 原型开发中`

当前仓库重点放在：

- 项目标识
- 说明文档
- 贡献流程
- 支持与安全入口
- 早期的仓库结构

随着项目从规划进入第一条可复现基线，具体能力会逐步加入仓库。

## 项目目录结构

```text
.
|-- src/                      # ROS 2 工作区包
|   |-- manippilot_msgs/      # 消息、服务与动作定义
|   |-- manippilot_core/      # 共享执行领域与核心逻辑
|   |-- manippilot_bt/        # 行为树节点与树资源
|   |-- manippilot_executor/  # 任务执行运行时包
|   |-- manippilot_bringup/   # 启动文件与运行配置
|   |-- manippilot_cli/       # 命令行入口包
|   `-- manippilot_examples/  # Demo 任务与示例场景
|-- tools/                    # 仓库级辅助工具与脚本
|-- tests/                    # 工作区级集成与回放测试
|-- docs/                     # 项目文档
|-- .github/                  # Issue 模板、PR 模板、CI 工作流
|-- README.md                 # 英文总览
|-- README.zh-CN.md           # 简体中文总览
|-- README.zh-TW.md           # 繁體中文总览
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- SUPPORT.md
|-- LICENSE
`-- NOTICE
```

## 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/Zw-awa/ManipPilot.git
cd ManipPilot
```

### 2. 阅读总览

建议先看：

- [`README.md`](./README.md)
- [`README.zh-CN.md`](./README.zh-CN.md)
- [`README.zh-TW.md`](./README.zh-TW.md)

### 3. 关注文档

当前仍处于规划与原型阶段，现阶段建议重点关注 `README`、[`docs/README.md`](./docs/README.md)、`SUPPORT` 和 issue 模板。

### 4. 如果想参与贡献

先阅读：

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`Issue 模板`](./.github/ISSUE_TEMPLATE/)
- [`SUPPORT.md`](./SUPPORT.md)

## 贡献

欢迎围绕操作工作流、文档、可复现性和可用性展开贡献。
请先阅读 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

如果改动较大，建议先开 issue 讨论，避免项目范围和工作流假设失去一致性。

## 安全提示

这个仓库面向的工作流未来可能会控制真实的操作机器人。
即使是早期操作系统，也可能夹手、掉落物体、碰撞工装，或者损坏硬件。
请把运动、电源、末端执行器测试和任务重试都当成硬件安全工作来对待。

## 许可证

本项目采用 [Apache License 2.0](./LICENSE)。
版权归属：`2026` `Zw-awa`。
补充归属信息见 [`NOTICE`](./NOTICE)。
