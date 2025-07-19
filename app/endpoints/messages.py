from fastapi import APIRouter, HTTPException
from app.models.schemas import SendMessageRequest, SendMessageResponse
from app.services.telegram import telegram_service
from app.config import settings
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

@router.post("/send-message", response_model=SendMessageResponse)
async def send_message(request: SendMessageRequest):
    """接收訊息並發送到Telegram"""
    
    # 驗證密碼
    if request.password != settings.API_PASSWORD:
        logger.warning(f"Invalid password attempt")
        raise HTTPException(status_code=401, detail="Invalid password")
    
    try:
        # 發送訊息到Telegram
        telegram_response = await telegram_service.send_message(
            chat_id=request.channel_id,
            text=request.message,
            parse_mode=request.parse_mode,
            disable_notification=request.disable_notification
        )
        
        return SendMessageResponse(
            success=True,
            message="Message sent successfully",
            telegram_response=telegram_response
        )
        
    except Exception as e:
        logger.error(f"Error sending message: {e}")
        raise HTTPException(status_code=500, detail=str(e))