import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.endpoints.messages import router as messages_router

# 配置日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# 驗證配置
settings.validate()

# 創建FastAPI應用
app = FastAPI(
    title="Telegram Bot API",
    description="簡單的Telegram Bot API，接收訊息並轉發到頻道",
    version="1.0.0"
)

# 添加CORS中間件
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 註冊路由
app.include_router(messages_router)

@app.get("/")
async def root():
    """健康檢查端點"""
    return {"status": "ok", "message": "Telegram Bot API is running"}

@app.get("/health")
async def health_check():
    """健康檢查端點"""
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )