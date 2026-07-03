from flask import Flask
from flask_cors import CORS

from .config import Config
from .routes.health import health_bp
from .routes.chat import chat_bp


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config())

    CORS(app, origins=[app.config["ALLOWED_ORIGINS"]])

    app.register_blueprint(health_bp, url_prefix="/api")
    app.register_blueprint(chat_bp, url_prefix="/api")

    return app
