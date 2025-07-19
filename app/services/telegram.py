import httpx
import logging
from typing import Dict, Any
from app.config import settings

logger = logging.getLogger(__name__)

class TelegramService:
    def __init__(self):
        self.base_url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}"
    
    async def send_message(
        self, 
        chat_id: str, 
        text: str, 
        parse_mode: str = "HTML",
        disable_notification: bool = False
    ) -> Dict[str, Any]:
        """發送訊息到Telegram"""
        url = f"{self.base_url}/sendMessage"
        
        payload = {
            "chat_id": chat_id,
            "text": text,
            "parse_mode": parse_mode,
            "disable_notification": disable_notification
        }
        
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(url, json=payload)
                response.raise_for_status()
                
                result = response.json()
                if not result.get("ok"):
                    raise Exception(f"Telegram API error: {result}")
                
                logger.info(f"Message sent successfully to {chat_id}")
                return result
                
        except httpx.HTTPError as e:
            logger.error(f"HTTP error sending message: {e}")
            raise
        except Exception as e:
            logger.error(f"Error sending message: {e}")
            raise

telegram_service = TelegramService()