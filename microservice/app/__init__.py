from flask import Flask
from flask_restful import Api


def create_app():
    """crear instancia de Flask app"""
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    return app


def init_api(app):
    from .resource.GetSandboxResponse import GetSandboxResponse

    api = Api(app)
    api.add_resource(GetSandboxResponse, '/run')
