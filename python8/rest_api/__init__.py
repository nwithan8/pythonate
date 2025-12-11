from python8.rest_api.utils import (
    build_api_response as build_api_response
)
import python8.rest_api.constants as constants

def _create_flask_app(name: str) -> 'flask.Flask':
    # local import prevents forcing Flask as a core dependency
    from flask import Flask
    return Flask(name)

class FlaskApp:
    def __init__(self, name: str):
        self._app: 'flask.Flask' = _create_flask_app(name)

    def register_blueprint(self, blueprint: 'flask.Blueprint'):
        self._app.register_blueprint(blueprint)

    def run(self, host: str = "127.0.0.1", port: int = 5000):
        self._app.run(host=host, port=port)

    def edit_config(self, key: str, value):
        self._app.config[key] = value
