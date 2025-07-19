# CapRover 環境變量設置詳細指南

## 🔧 環境變量列表

根據 `.env.example`，你需要在 CapRover 中設置以下環境變量：

### 必需變量
| 變量名稱 | 說明 | 示例 |
|---------|------|------|
| `TELEGRAM_BOT_TOKEN` | Telegram Bot 的 API Token | `123456789:ABCdefGHIjklMNOpqrSTUvwxyz` |
| `API_PASSWORD` | API 訪問密碼 | `your_secure_password_123` |

### 可選變量
| 變量名稱 | 說明 | 預設值 |
|---------|------|--------|
| `HOST` | 服務器綁定地址 | `0.0.0.0` |
| `PORT` | 服務器端口 | `8000` |

## 🚀 設置方法

### 方法一：使用 CapRover Web 界面（推薦）

1. **登入 CapRover 管理界面**
   - 訪問 `https://captain.your-domain.com`
   - 使用你的管理員密碼登入

2. **進入應用設置**
   - 點擊左側菜單的 "Apps"
   - 選擇你的 Telegram Bot 應用
   - 點擊 "App Configs" 標籤

3. **添加環境變量**
   - 在 "Environmental Variables" 區塊
   - 點擊 "Add Environmental Variable"
   - 輸入以下內容：

   ```
   Key: TELEGRAM_BOT_TOKEN
   Value: 你的實際機器人Token
   ```

   ```
   Key: API_PASSWORD
   Value: 你選擇的API密碼
   ```

4. **保存並重啟**
   - 點擊 "Save & Update"
   - 等待應用自動重啟

### 方法二：使用 CapRover CLI

1. **安裝 CLI 工具**
   ```bash
   npm install -g caprover
   ```

2. **登入 CapRover**
   ```bash
   caprover login
   # 輸入你的 CapRover 域名和管理員密碼
   ```

3. **設置環境變量**
   ```bash
   # 設置 Telegram Bot Token
   caprover env TELEGRAM_BOT_TOKEN="123456789:ABCdefGHIjklMNOpqrSTUvwxyz" --appName telegram-bot

   # 設置 API 密碼
   caprover env API_PASSWORD="your_secure_password_123" --appName telegram-bot
   ```

4. **驗證設置**
   ```bash
   # 查看當前環境變量
   caprover env --appName telegram-bot
   ```

## ✅ 驗證環境變量

### 方法一：通過 API 測試
部署完成後，使用以下命令測試：

```bash
curl -X POST https://your-app-name.your-domain.com/send-message \
  -H "Content-Type: application/json" \
  -d '{
    "password": "你設置的API密碼",
    "message": "測試消息",
    "channel_id": "你的頻道ID"
  }'
```

### 方法二：查看應用日誌
1. 在 CapRover 管理界面
2. 進入你的應用
3. 點擊 "Logs" 查看日誌輸出
4. 確認應用正常啟動且沒有環境變量錯誤

### 方法三：健康檢查
訪問健康檢查端點：
```
https://your-app-name.your-domain.com/health
```

## ⚠️ 關於 Build Args 警告

你看到的警告：
```
[Warning] One or more build-args [API_PASSWORD CAPROVER_GIT_COMMIT_SHA HOST PORT TELEGRAM_BOT_TOKEN] were not consumed
```

這是正常的，因為：
- **CapRover 自動傳遞**這些 build-args
- **我們的 Dockerfile 不需要**在構建時使用這些變量
- **環境變量在運行時**才會被應用使用

這個警告不會影響應用的正常運行。

## 🎯 快速檢查清單

部署完成後，確認以下事項：

- [ ] 應用狀態顯示 "Running"
- [ ] 環境變量已正確設置
- [ ] 健康檢查端點可訪問
- [ ] API 測試成功
- [ ] Telegram Bot 能夠接收和發送消息

## 🆘 常見問題

### Q: 環境變量設置後沒有生效？
A: 確保點擊了 "Save & Update" 並等待應用重啟完成。

### Q: 忘記設置某個環境變量？
A: 可以隨時在 "App Configs" 中添加或修改，應用會自動重啟。

### Q: 如何查看當前設置的環境變量？
A: 在 CapRover 管理界面的 "App Configs" 中查看，或使用 CLI 命令 `caprover env --appName telegram-bot`。