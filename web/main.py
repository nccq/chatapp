import config
from flask import sessionpy
from flask_socketio import SocketIO
from application import create_app
from application.database import DataBase
import time


app = create_app()
socketio = SocketIO(app)

@socketio.on('event')
def handle_my_custom_event(json, methods=['GET', 'POST']):

    data = dict(json)
    if "name" in data:
        db = DataBase()
        db.save_message(data["name"], data["message"])

    socketio.emit('message response', json)

    if __name__ == "__main__":  # start the web server
        socketio.run(app, debug=True, host=str(config.Config.SERVER))