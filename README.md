# 👑 Princess Game

Welcome to **Princess Game**, a fun Python text adventure game where your goal is to escape the castle and save the princess! The game can be played either via **web interface** or **CLI (Command Line Interface)**.

---

## 🕹 Features

- Interactive gameplay with room navigation.
- Pick up items to complete your quest.
- Timer-based challenge – finish before time runs out.
- Playable via **CLI** or **Web (Flask app)**.
- Includes **unit tests** for all main components.

---

## 📦 Project Structure

princess_web/
├── app.py # Flask web app
├── cli.py # Command-line interface
├── requirements.txt # Dependencies
├── src/princess_game/ # Game logic
│ ├── game.py
│ ├── player.py
│ ├── room.py
│ ├── map.py
│ ├── lexicon.py
│ └── timer.py
├── templates/ # HTML templates
│ └── index.html
└── tests/ # Unit tests


---

## ⚡ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/RadwaNagy44/princess-game.git
cd princess-game

### 2. Create a virtual environment (recommended)

python -m venv venv

Activate it:
Windows (cmd): venv\Scripts\activate

Windows (PowerShell): venv\Scripts\Activate.ps1

Linux / macOS: source venv/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

---

## 🕹 How to Play
CLI Version
python -m src.princess_game.cli

Commands:
go north – move between rooms

take key – pick up items

help – list commands

quit – exit game

Web Version
python app.py

Open http://127.0.0.1:5000 in your browser.

Use the input box to type commands and navigate the castle.

---

## ⏳ Game Rules

Collect map, key, and crown.

Reach the castle gate to win.

Beat the timer (90 seconds) or you lose.

Inventory and time remaining are displayed in the game.

---

## ✅ Run Tests
pytest
All main components (Game, Player, Room, Timer, Lexicon) are fully tested.

---

## 🎨 Customize Your Game

Add new rooms: src/princess_game/map.py

Add new items: src/princess_game/lexicon.py and map rooms

Adjust timer: src/princess_game/timer.py

---

## 📄 License
Open-source & free to use.






