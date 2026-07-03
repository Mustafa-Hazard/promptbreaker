import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    FLASK_ENV = os.getenv("FLASK_ENV", "production")
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")

    @staticmethod
    def validate():
        if not Config.GROQ_API_KEY:
            raise EnvironmentError("GROQ_API_KEY is not set")
