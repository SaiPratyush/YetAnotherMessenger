"""All SocketIO events used by the sever."""
from flask_socketio import emit, join_room, leave_room
from . import socketio
from .models import user


def handles_events():
    """Print all events handled."""
    events = ['connect', 'disconnect', 'join', 'leave',
              'message', 'incoming-msg', 'is-active', 'active-devices']
    print("Handles events: " + ", ".join(events))


# Connections

@socketio.on('connect')
def on_connect():
    """Handle incomming connections."""
    print("device connected")
    emit('connected', "{'message':'device connected'}")


@socketio.on('disconnect')
def on_disconnect():
    """Handle client disconnection."""
    print("device disconnected")


# Rooms

@socketio.on('join')
def on_join(data):
    """User joins a room.

    Args:
        data (JSON): Message sent by client as a JSON object.
    """
    room = data["room"]
    join_room(room)
    emit('join', "{'message':'joined room'}", room=room)


@socketio.on('leave')
def on_leave(data):
    """User leaves a room.

    Args:
        data (JSON): JSON object consisting user id that left the room.
    """
    room = data["room"]
    leave_room(room)
    print(room+' left the room')


# Messages

@socketio.on('message')
def on_message(msg):
    """Handle unnamed messages.

    Args:
        msg (JSON): Message sent by client as a JSON object.
    """
    print("message received: "+str(msg))
    emit('message', "{'message':'received message'}")


@socketio.on('incoming-msg')
def on_incoming_message(data):
    """Broadcast messages to specific user.

    Args:
        data (JSON): Message sent by client as a JSON object.
    """
    msg = data["msg"]
    username = data["username"]
    room = data["room"]
    emit('incoming-msg', "{'username': '"+username +
         "','message':'"+msg+"'}", room=room)


# Sign up and Login

@socketio.on('signup')
def on_signup(data):
    """Register new user.

    Args:
        data (JSON): Data requested by client as a JSON object.
    """
    username = data["username"]
    email = data["email"]
    password = data["password"]
    userid = user.User(email, password, username)
    success = userid.register_user()
    message = "User already exists"
    if(success):
        print("registered user: "+userid.get_email())
        message = "User Registered"
    emit('signup', "{'success': '"+str(success) +
         "','message':'"+message+"'}")


@socketio.on('login')
def on_login(data):
    """Login user.

    Args:
        data (JSON): Data requested by client as a JSON object.
    """
    email = data["email"]
    password = data["password"]
    userid = user.User(email, password)
    success = userid.check_password(password)
    print("login success:"+success+", user: "+userid.get_email())
    emit('signup', "{'success': '"+success +
         "','message':'User logged in'}")


# Status queries

@socketio.on('is-active')
def on_is_active(data):
    """Return active/inactive status of a specific user.

    Args:
        data (JSON): Data requested by client as a JSON object.
    """
    pass
    # TODO


@socketio.on('active-devices')
def on_active_devices(data):
    """Return list of devices the user is active on.

    Args:
        data (JSON): Data requested by client as a JSON object.
    """
    pass
    # TODO
