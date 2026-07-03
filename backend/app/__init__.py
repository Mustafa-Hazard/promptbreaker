from flask import Flask
from flask_cors import CORS

from .config import Config
from .routes.health import health_bp


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    CORS(app, origins=[app.config["ALLOWED_ORIGINS"]])

    app.register_blueprint(health_bp, url_prefix="/api")

    # NOTE: chat_bp is registered here starting in Phase 1
    # from .routes.chat import chat_bp
    # app.register_blueprint(chat_bp, url_prefix="/api")

    return app
