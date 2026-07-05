from flask import Flask

from app.routes.agent_routes import agent_routes

def register_routes(app: Flask):
    app.register_blueprint(agent_routes)