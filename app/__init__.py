"""Initiate Flask App."""

from flask import Flask
from flask_socketio import SocketIO


socketio = SocketIO()


def create_app():
    from . import events

    app = Flask(__name__)
    app.config['SECRET_KEY'] = "mysecretkey"
    app.config.from_object('app.configuration.DevelopmentConfig')

    from .views.gateway import gateway_bp
    app.register_blueprint(gateway_bp)

    socketio.init_app(app)

    return app

# @socketio.on('message')
# def handlemessage(msg):
#     print("message received: "+str(msg))
#     emit('message', "{'message':'received message'}")


# @socketio.on('notification')
# def handlenotification(msg):
#     print("sending notification: "+str(msg))
#     emit('notification', "{'message':'received notification'}")
