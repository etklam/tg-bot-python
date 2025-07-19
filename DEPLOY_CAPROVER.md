# CapRover 部署指南

## 🚀 快速部署步驟

### 1. 準備CapRover
確保您已經：
- 安裝了CapRover CLI：`npm install -g caprover`
- 有CapRover伺服器運行中
- 知道您的CapRover域名和密碼

### 2. 配置環境變數
在CapRover管理界面中設置環境變數：
```bash
TELEGRAM_BOT_TOKEN=your_bot_token_here
API_PASSWORD=your_chosen_password
```

### 3. 部署命令

#### 方法一：使用CapRover CLI
```bash
# 登入CapRover
caprover login

# 部署
caprover deploy
```

#### 方法二：手動部署
1. 推送代碼到Git倉庫
2. 在CapRover管理界面 → Apps → 創建新應用
3. 選擇 "Method 4: Deploy from Github/Bitbucket/Gitlab"
4. 填寫倉庫資訊

### 4. 配置應用
在CapRover管理界面：
- **App Name**: telegram-bot
- **Port**: 8000
- **Persistent Directories**: 不需要
- **Environment Variables**: 添加TELEGRAM_BOT_TOKEN和API_PASSWORD

### 5. 驗證部署
部署完成後，訪問：
```
https://your-app-name.your-domain.com/docs
```

## 📋 完整部署流程

### 步驟1：本地測試
```bash
python run.py
```

### 步驟2：推送代碼
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin your-repo-url
git push -u origin main
```

### 步驟3：CapRover設置
```bash
# 安裝CLI
npm install -g caprover

# 登入
caprover login

# 創建應用
caprover create

# 部署
caprover deploy
```

### 步驟4：環境變數配置
在CapRover管理界面：
1. 進入您的應用
2. 點擊 "App Configs"
3. 添加環境變數：
   - `TELEGRAM_BOT_TOKEN`: 您的機器人Token
   - `API_PASSWORD`: 您選擇的API密碼

## 🔧 故障排除

### 部署失敗
1. 檢查Dockerfile是否正確
2. 確認端口8000已暴露
3. 查看應用日誌獲取詳細錯誤

### 環境變數問題
1. 確認變數名稱正確
2. 重啟應用使變數生效

### 網絡問題
1. 確認域名解析正確
2. 檢查HTTPS證書

## 🎯 部署後測試
```bash
curl -X POST https://your-app-name.your-domain.com/send-message \
  -H "Content-Type: application/json" \
  -d '{
    "password": "your_password",
    "message": "Hello from CapRover!",
    "channel_id": "585426653"
  }'
```

## 📱 CapRover管理界面
訪問：https://captain.your-domain.com
- 查看應用狀態
- 查看日誌
- 管理環境變數
- 設置自動部署