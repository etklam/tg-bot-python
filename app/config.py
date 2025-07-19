import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", '5398594893:AAFvCbyDA4ZAoRy0nJ8dz_Vbja_HhSSwkhk')
    API_PASSWORD = os.getenv("API_PASSWORD", 'Ihave2jj')
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 8000))
    
    @classmethod
    def validate(cls):
        if not cls.TELEGRAM_BOT_TOKEN:
            raise ValueError("TELEGRAM_BOT_TOKEN is required")
        if not cls.API_PASSWORD:
            raise ValueError("API_PASSWORD is required")

settings = Settings()