"""Initiate Flask App."""

from flask import Flask
from flask_socketio import SocketIO


socketio = SocketIO()


def create_app():
    """Create Flask app and add configurations.

    Returns:
        flask.app.Flask: Returns Flask app object.
    """
    from . import events

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mysecretkey"
    app.config.from_object('app.configuration.DevelopmentConfig')

    from .views.gateway import gateway_bp
    app.register_blueprint(gateway_bp)

    socketio.init_app(app)
    events.handles_events()
    return app
