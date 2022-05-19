import os
from flask import Flask
from dotenv import load_dotenv
from config.config import config

from api.routing import api_v1


load_dotenv()
ENV = os.getenv('ENV', 'default')

if ENV not in config:
    raise Exception('Invalid ENV: %s' % ENV)


def create_app():
    app = Flask(__name__)
    app.config.from_object(config[ENV]())
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    """Register extensions."""
    return None


def register_blueprints(app):
    """Register blueprints."""
    app.register_blueprint(api_v1)

    return None
