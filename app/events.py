from flask_socketio import emit
from . import socketio


@socketio.on('message')
def handlemessage(msg):
    print("message received: "+str(msg))
    emit('message', "{'message':'received message'}")


@socketio.on('connect')
def handle_connection():
    print("device connected")
    emit('connected', "{'message':'device connected'}")


@socketio.on('disconnect')
def handle_disconnection():
    print("device disconnected")
