# CapRover 環境變量使用指南

## 📋 重要說明

**CapRover 不使用 .env 文件！**  
CapRover 通過管理界面設置環境變量，而不是讀取 .env 文件。

## 🎯 正確使用方法

### 方法1：使用 `caprover.env` 作為參考
1. 打開 [`caprover.env`](caprover.env) 文件
2. 複製其中的變量名稱和值
3. 在 CapRover 管理界面中設置

### 方法2：直接設置環境變量

#### 步驟1：獲取 Telegram Bot Token
1. 在 Telegram 中搜索 @BotFather
2. 創建新機器人或獲取現有機器人的 Token
3. 複製 Token（格式：`123456789:ABCdefGHIjklMNOpqrSTUvwxyz`）

#### 步驟2：設置 CapRover 環境變量
1. 登入 CapRover 管理界面：`https://captain.your-domain.com`
2. 進入你的應用
3. 點擊 "App Configs"
4. 在 "Environmental Variables" 區塊添加：

```
TELEGRAM_BOT_TOKEN=你的實際token
API_PASSWORD=你選擇的密碼
```

## ⚠️ 常見誤區

### ❌ 錯誤做法
- 將 `.env` 文件上傳到倉庫
- 期望 CapRover 讀取 `.env` 文件
- 在 Dockerfile 中複製 `.env` 文件

### ✅ 正確做法
- 在 CapRover 管理界面設置環境變量
- 使用 `caprover.env` 作為參考模板
- 將敏感信息保存在 CapRover 中，而不是代碼中

## 🚀 快速設置步驟

