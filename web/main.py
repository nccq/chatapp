from flask import session
from flask_socketio import SocketIO
from application import create_app


app = create_app()
socketio = SocketIO(app)

