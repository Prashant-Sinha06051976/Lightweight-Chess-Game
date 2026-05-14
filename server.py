
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "dynamic_chess_secret"

socketio = SocketIO(app, cors_allowed_origins="*")

game_state = {
    "moves": []
}

@socketio.on("connect")
def on_connect():
    emit("game_state", game_state, broadcast=True)

@socketio.on("move")
def on_move(data):
    move = data.get("move")

    if move:
        game_state["moves"].append(move)

    emit("game_state", game_state, broadcast=True)

if __name__ == "__main__":
    socketio.run(
        app,
        host="0.0.0.0",
        port=5000
    )
