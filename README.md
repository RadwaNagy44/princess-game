# 👑 Princess Game

Welcome to **Princess Game**, a fun Python text adventure game where your goal is to escape the castle and save the princess! The game can be played either via **web interface** or **CLI (Command Line Interface)**.

## 🎮 Gameplay Preview

Navigate through castle rooms, collect essential items (map, key, crown), and reach the castle gate before time runs out to save the princess!

## 🚀 Features

- **Dual Interface**: Play via **CLI** or **Web** (Flask app)
- **Time Challenge**: 90-second timer to complete your quest
- **Interactive Rooms**: Explore different castle locations
- **Inventory System**: Collect and use items
- **Full Test Suite**: Comprehensive unit tests for all components
- **Extensible Design**: Easy to modify rooms, items, and game rules

## 📁 Project Structure

```
princess_web/
├── app.py                 # Flask web application
├── cli.py                 # Command-line interface
├── requirements.txt       # Python dependencies
├── src/princess_game/     # Core game logic
│   ├── game.py           # Main game controller
│   ├── player.py         # Player class and inventory
│   ├── room.py           # Room definitions and connections
│   ├── map.py            # Castle layout and navigation
│   ├── lexicon.py        # Game vocabulary and commands
│   └── timer.py          # Countdown timer
├── templates/            # HTML templates
│   └── index.html        # Web game interface
└── tests/                # Unit tests
    ├── test_game.py
    ├── test_player.py
    ├── test_room.py
    ├── test_map.py
    └── test_timer.py
```

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/RadwaNagy44/princess-game.git
cd princess-game
```

### 2. Set Up Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate it
# Windows (Command Prompt):
venv\Scripts\activate

# Windows (PowerShell):
venv\Scripts\Activate.ps1

# Linux / macOS:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🕹️ How to Play

### CLI Version

```bash
python -m src.princess_game.cli
```

**Available Commands:**
- `go north` / `go south` / `go east` / `go west` – Move between rooms
- `take [item]` – Pick up items (key, map, crown)
- `inventory` – Check your collected items
- `help` – Show available commands
- `quit` – Exit the game

### Web Version

```bash
python app.py
```

Then open your browser and navigate to:  
👉 **http://127.0.0.1:5000**

Use the input box to type commands just like in the CLI version.

## 🏆 Game Rules

1. **Objective**: Escape the castle with the princess
2. **Required Items**: 
   - 🗺️ Map (to navigate)
   - 🔑 Key (to unlock doors)
   - 👑 Crown (to prove your royalty)
3. **Win Condition**: Reach the "Castle Gate" with all items
4. **Time Limit**: 90 seconds
5. **Display**: Your inventory and remaining time are shown during gameplay

## 🧪 Running Tests

Ensure all game components work correctly:

```bash
pytest
```

Test coverage includes:
- ✅ Game mechanics and logic
- ✅ Player inventory management
- ✅ Room navigation and connections
- ✅ Timer functionality
- ✅ Command parsing

## 🎨 Customization

Want to modify the game? Here's how:

### Add New Rooms
Edit `src/princess_game/map.py` to add new locations and connections.

### Add New Items
1. Update `src/princess_game/lexicon.py` with new item names
2. Place items in rooms within `map.py`

### Adjust Difficulty
- Modify timer duration in `src/princess_game/timer.py`
- Change required items in `src/princess_game/game.py`

### Change Castle Layout
Edit the room connections in `src/princess_game/map.py` to create new paths and challenges.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open-source and free to use under the MIT License.

## 🙏 Acknowledgements

- Built with Python and Flask
- Inspired by classic text adventure games
- Thanks to all contributors and testers

---

**Ready for adventure?** Save the princess before time runs out! 👑⚔️🏰

---

*Created with ❤️ by Radwa Nagy*
