from src.princess_game.map import create_map
from src.princess_game.player import Player
from src.princess_game.game import Game

def print_state(game):
    state = game.get_state()
    room = state["room"]

    print("\n----------------------------")
    print(f"You are in: {room.name}")
    print(room.description)

    if room.items:
        print(f"Items here: {', '.join(room.items)}")

    if state["inventory"]:
        print(f"Your inventory: {', '.join(state['inventory'])}")
    else:
        print("Your inventory: Empty")

    print(f"Time left: {state['time_left']} seconds")
    print("----------------------------\n")


def main():
    rooms, starting_room = create_map()
    player = Player(starting_room)
    game = Game(player, starting_room, rooms)

    game.start()
    print("Welcome To Princess Game 👑")

    print_state(game)

    while True:
        command = input("Enter command: ")
        result = game.execute_command(command)
        print(result.message)

        if result.game_over:
            break

        print_state(game)


if __name__ == "__main__":
    main()
