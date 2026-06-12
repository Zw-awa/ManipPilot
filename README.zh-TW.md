# ManipPilot

[English](./README.md) | [简体中文](./README.zh-CN.md) | [繁體中文](./README.zh-TW.md)

[![狀態](https://img.shields.io/badge/status-planning%20%2F%20prototyping-4c8bf5)](#目前狀態)
[![授權](https://img.shields.io/badge/license-Apache--2.0-1976d2)](./LICENSE)
![任務](https://img.shields.io/badge/tasking-declarative-2e7d32)
![中介軟體](https://img.shields.io/badge/middleware-ROS%202-1565c0)
![操作](https://img.shields.io/badge/manipulation-task%20executive-f57c00)

`ManipPilot` 是一個面向 `ROS 2` 機器人操作任務的宣告式任務執行工具，讓機器人任務從一次性腳本變成可安裝、可重用、可回放、可恢復的工作流程。

## 目錄

- [ManipPilot](#manippilot)
  - [目錄](#目錄)
  - [這個專案是什麼](#這個專案是什麼)
  - [它想做到什麼](#它想做到什麼)
  - [第一版重點聚焦什麼](#第一版重點聚焦什麼)
  - [目前狀態](#目前狀態)
  - [專案目錄結構](#專案目錄結構)
  - [快速開始](#快速開始)
    - [1. 複製倉庫](#1-複製倉庫)
    - [2. 閱讀總覽](#2-閱讀總覽)
    - [3. 關注文件](#3-關注文件)
    - [4. 如果想參與貢獻](#4-如果想參與貢獻)
  - [貢獻](#貢獻)
  - [安全提醒](#安全提醒)
  - [授權](#授權)

## 這個專案是什麼

這個倉庫是 `ManipPilot` 的首頁。

ManipPilot 的目標，是讓受支援的 `ROS 2` 機器人操作任務更容易安裝、重用、回放與恢復。

它更適合這樣一類使用者：

- 已經有或準備搭建機器人操作棧的開發者
- 想把臨時腳本整理成可重複執行任務的人
- 需要回放與檢視執行過程的人
- 希望在失敗時有明確恢復路徑的人

專案後續會圍繞下面這些使用者價值展開：

- 宣告式任務描述
- 面向操作任務的可重用執行流程
- 面向除錯與檢視的可回放執行紀錄
- 在受支援失敗場景下更清楚的恢復行為
- 具有清楚輸入輸出邊界的工作流程

`README` 主要描述專案範圍、使用方向與貢獻入口。

## 它想做到什麼

ManipPilot 面向的是一個更穩定的任務執行流程：

- 用結構化方式描述一個操作任務
- 透過受支援的 `ROS 2` 機器人操作棧執行這個任務
- 讓執行過程更容易觀察、檢視與定位問題
- 在任務步驟失敗時提供更明確的恢復路徑
- 幫助使用者把脆弱的一次性腳本升級為可重複使用的工作流程

常見示例包括：

- 從已知工作區抓取目標物體
- 把物體放到指定位置
- 執行一段多步驟桌面操作任務
- 在任務無法繼續時進行重試或安全退出
- 對歷史執行結果進行回放與檢視

## 第一版重點聚焦什麼

第一版會刻意收斂，目前主要聚焦這些事情：

- 一條面向 `ROS 2` 機器人操作任務的執行路徑
- 一套以命令列為主的工作流程
- 一種可回放的任務執行模型
- 一種可恢復的任務執行方式
- 一個以桌面機械臂為首個驗證場景的初始基線

這也代表第一版暫時不會同時覆蓋下面這些方向：

- 所有類型的機器人形態
- 寬泛的自主感知承諾
- 不受約束的自然語言互動
- 一次性覆蓋所有規劃或編排風格
- 在第一條可重現基線穩定前做過寬的支援承諾

第一條驗證路徑會先聚焦桌面機械臂，但專案身分本身並不只限定在桌面場景。

## 目前狀態

`規劃中 / 原型開發中`

目前倉庫重點放在：

- 專案識別
- 說明文件
- 貢獻流程
- 支援與安全入口
- 早期的倉庫結構

隨著專案從規劃進入第一條可重現基線，具體能力會逐步加入倉庫。

## 專案目錄結構

```text
.
|-- src/                      # ROS 2 工作區套件
|   |-- manippilot_msgs/      # 訊息、服務與動作定義
|   |-- manippilot_core/      # 共用執行領域與核心邏輯
|   |-- manippilot_bt/        # 行為樹節點與樹資源
|   |-- manippilot_executor/  # 任務執行執行期套件
|   |-- manippilot_bringup/   # 啟動檔與執行設定
|   |-- manippilot_cli/       # 命令列入口套件
|   `-- manippilot_examples/  # Demo 任務與示例場景
|-- tools/                    # 倉庫層級輔助工具與腳本
|-- tests/                    # 工作區層級整合與回放測試
|-- docs/                     # 專案文件
|-- .github/                  # Issue 模板、PR 模板、CI workflow
|-- README.md                 # 英文總覽
|-- README.zh-CN.md           # 簡體中文總覽
|-- README.zh-TW.md           # 繁體中文總覽
|-- CONTRIBUTING.md
|-- CODE_OF_CONDUCT.md
|-- SECURITY.md
|-- SUPPORT.md
|-- LICENSE
`-- NOTICE
```

## 快速開始

### 1. 複製倉庫

```bash
git clone https://github.com/Zw-awa/ManipPilot.git
cd ManipPilot
```

### 2. 閱讀總覽

建議先看：

- [`README.md`](./README.md)
- [`README.zh-CN.md`](./README.zh-CN.md)
- [`README.zh-TW.md`](./README.zh-TW.md)

### 3. 關注文件

目前仍處於規劃與原型階段，現階段建議重點關注 `README`、[`docs/README.md`](./docs/README.md)、`SUPPORT` 和 issue 模板。

### 4. 如果想參與貢獻

先閱讀：

- [`CONTRIBUTING.md`](./CONTRIBUTING.md)
- [`Issue 模板`](./.github/ISSUE_TEMPLATE/)
- [`SUPPORT.md`](./SUPPORT.md)

## 貢獻

歡迎圍繞操作工作流程、文件、可重現性與可用性展開貢獻。
請先閱讀 [`CONTRIBUTING.md`](./CONTRIBUTING.md)。

如果改動較大，建議先開 issue 討論，避免專案範圍和工作流程假設失去一致性。

## 安全提醒

這個倉庫面向的工作流程未來可能會控制真實的操作機器人。
即使是早期操作系統，也可能夾手、掉落物體、碰撞工裝，或者損壞硬體。
請把運動、電源、末端執行器測試和任務重試都當成硬體安全工作來對待。

## 授權

本專案採用 [Apache License 2.0](./LICENSE)。
版權歸屬：`2026` `Zw-awa`。
補充歸屬資訊見 [`NOTICE`](./NOTICE)。
