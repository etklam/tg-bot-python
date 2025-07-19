from pydantic import BaseModel, Field

class SendMessageRequest(BaseModel):
    password: str = Field(..., description="API密碼")
    message: str = Field(..., description="要發送的訊息內容")
    channel_id: str = Field(..., description="Telegram頻道ID或群組ID")
    parse_mode: str = Field(default="HTML", description="訊息解析模式")
    disable_notification: bool = Field(default=False, description="是否禁用通知")

class SendMessageResponse(BaseModel):
    success: bool
    message: str
    telegram_response: dict = None