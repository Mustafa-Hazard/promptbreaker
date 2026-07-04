import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    NOTE: these are read as properties, not class attributes, so that
    os.environ is consulted fresh every time create_app() runs (important
    for tests that monkeypatch env vars after this module has already been
    imported).
    """

    @property
    def GROQ_API_KEY(self):
        return os.getenv("GROQ_API_KEY")

    @property
    def FLASK_ENV(self):
        return os.getenv("FLASK_ENV", "production")

    @property
    def ALLOWED_ORIGINS(self):
        origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000")
        return [o.strip() for o in origins.split(",")]

    def validate(self):
        if not self.GROQ_API_KEY:
            raise EnvironmentError("GROQ_API_KEY is not set")
