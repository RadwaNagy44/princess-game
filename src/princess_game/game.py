from src.princess_game.lexicon import Lexicon
from src.princess_game.timer import Timer


class CommandResult(object):
    def __init__(self, message="", game_over=False, result_type=None):
        self.message = message
        self.game_over = game_over
        self.result_type = result_type


class Game(object):
    def __init__(self, player, starting_room = None, rooms = None):
        self.player = player
        self.starting_room = starting_room or player.current_room
        self.rooms = rooms or {}
        self.lex = Lexicon()
        self.timer = Timer()

    
    # Game state checks
    def has_won(self):
        required_items = ["crown", "map", "key"]
        return (
            all(item in self.player.inventory for item in required_items)
            and self.player.current_room.name == "castle gate"
        )

    def has_lost(self):
        return self.timer.is_time_over()


    # Public API (used by Flask / CLI)
    def start(self):
        if self.timer.start_time is None:
            self.timer.start()

    def get_state(self):
        return {
            "room": self.player.current_room,
            "inventory": self.player.inventory,
            "time_left": int(self.timer.time_left())
        }

    def reset(self):
        # reset rooms items
        self.rooms["hall"].items = ["map"]
        self.rooms["storage"].items = ["key"]
        self.rooms["castle gate"].items = ["crown"]

        # reset player
        self.player.current_room = self.starting_room
        self.player.inventory = []

        # reset timer
        self.timer.start_time = None
        self.timer.start()

    
    # Command handling
    def execute_command(self, command):
        tokens = self.lex.scan(command)
        verb = next((w for t, w in tokens if t == "verb"), None)
        obj = next((w for t, w in tokens if t in ("direction", "item")), None)

        if verb in ("move", "go") and obj:
            if self.player.move(obj):
                result = CommandResult(
                    f"You move {obj} to the {self.player.current_room.name}."
                )
            else:
                result = CommandResult("You can't go that way.")

        elif verb in ("take", "pick") and obj:
            if self.player.pick_item(obj):
                result = CommandResult(f"You picked up the {obj}.")
            else:
                result = CommandResult(f"There is no {obj} here.")

        elif verb == "help":
            result = CommandResult(
                "Commands: go (direction), take (item), quit"
            )

        elif verb == "quit":
            return CommandResult(
                "Thanks for playing!",
                game_over=True
            )

        else:
            result = CommandResult(
                "Invalid command. Type 'help' to see available commands."
            )

        # ---- end conditions ----
        if self.has_won():
            return CommandResult(
                "You escaped the castle 🎉\nYou saved the princess!",
                game_over=True,
                result_type="win"
            )

        if self.has_lost():
            return CommandResult(
                "⏰ Time's up! You failed to escape the castle.",
                game_over=True,
                result_type="lose"
            )

        return result
