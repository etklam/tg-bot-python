# CapRover 端口配置指南

## 🔍 是否需要配置端口？

**簡短回答：不需要額外配置，使用默認設置即可。**

## 📋 當前配置分析

### 1. Dockerfile 配置
- **暴露端口**: 8000 (已在 Dockerfile 中設置)
- **綁定地址**: 0.0.0.0 (監聽所有網絡接口)

### 2. CapRover 默認行為
- CapRover 會自動檢測 Dockerfile 中的 `EXPOSE 8000`
- 會自動將容器的 8000 端口映射到外部訪問

### 3. 需要做的端口配置

**在 CapRover 管理界面中：**
1. 進入你的應用
2. 點擊 "App Configs"
3. **HTTP Settings** 區塊：
   - **Container Port**: 8000 (應該已經自動檢測)
   - **Port Mapping**: 不需要手動設置
   - **Domain**: 會自動分配 `https://your-app-name.your-domain.com`

## ✅ 驗證端口配置

### 方法一：檢查應用詳情
1. 在 CapRover 管理界面
2. 進入你的應用
3. 查看 "App Configs" → "HTTP Settings"
4. 確認顯示類似：
   ```
   Container Port: 8000
   Published Port: 80 (自動映射)
   ```

### 方法二：測試訪問
部署完成後直接訪問：
```
https://your-app-name.your-domain.com/health
```

## ⚠️ 什麼情況下需要手動配置端口？

**以下情況才需要手動配置：**

1. **使用非 80/443 端口**
   - 如果你想通過 `https://your-app-name.your-domain.com:8080` 訪問
   - 需要在 "App Configs" → "Port Mapping" 中添加

2. **使用 TCP 端口**
   - 對於非 HTTP 服務
   - 需要在 "App Configs" → "Port Mapping" 中設置

## 🎯 當前項目結論

**你的 Telegram Bot 項目：**
- ✅ 使用標準的 8000 端口
- ✅ 是 HTTP 服務
- ✅ CapRover 會自動處理端口映射
- ❌ **不需要額外端口配置**

## 📱 快速檢查清單

部署後確認：
- [ ] 應用狀態顯示 "Running"
- [ ] 訪問 `https://your-app-name.your-domain.com/health` 成功
- [ ] 顯示 `{"status":"healthy"}` 或類似響應