from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate

from app.config import Config
from app.persist import db
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_object('app.config.Config')

    register_routes(app)

    db.init_app(app)

    Migrate(app, db)

    return app