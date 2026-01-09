from flask import Flask, render_template, request, redirect, url_for

from src.princess_game.game import Game
from src.princess_game.map import create_map
from src.princess_game.player import Player

app = Flask(__name__)


# Game initialization
rooms, starting_room = create_map()
player = Player(starting_room)
game = Game(player, starting_room, rooms)


# Routes
@app.route("/", methods=["GET", "POST"])
def index():
    game.start()

    message = None
    end_message = None
    result_type = None
    game_over = False

    if request.method == "POST":
        command = request.form.get("command", "")
        result = game.execute_command(command)

        message = result.message
        game_over = result.game_over
        result_type = result.result_type

        if game_over:
            end_message = result.message
            message = None

    state = game.get_state()

    return render_template(
        "index.html",
        room=state["room"],
        inventory=state["inventory"],
        time_left=state["time_left"],
        message=message,
        end_message=end_message,
        game_over=game_over,
        result_type=result_type
    )


@app.route("/reset", methods=["POST"])
def reset():
    game.reset()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
