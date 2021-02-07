from flask import Flask, request, current_app
from config import Config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    db.init_app(app)

    with app.app_context():
        db.Model.metadata.reflect(db.engine)

    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    return app

from app import models