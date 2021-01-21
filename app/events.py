"""All SocketIO events used by the sever."""
from flask_socketio import emit
from . import socketio


def handles_events():
    """Print all events handled."""
    events = ['message', 'connect', 'disconnect']
    print("Handles events: " + ", ".join(events))


@socketio.on('message')
def handle_message(msg):
    """Handle unnamed messages.

    Args:
        msg (JSON): Message sent by client as a JSON object.
    """
    print("message received: "+str(msg))
    emit('message', "{'message':'received message'}")


@socketio.on('connect')
def handle_connection():
    """Handle incomming connections."""
    print("device connected")
    emit('connected', "{'message':'device connected'}")


@socketio.on('disconnect')
def handle_disconnection():
    """Handle client disconnection."""
    print("device disconnected")
