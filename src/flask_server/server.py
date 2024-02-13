from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on('game_input')
def handle_game_input(input_data):
    pass

if __name__ == "__main__":
    app.run(debug=True)