import json
import os

SCOREBOARD_FILE = "scoreboard.json"

def load_scoreboard():
    if os.path.exists(SCOREBOARD_FILE):
        with open(SCOREBOARD_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

def save_scoreboard(scoreboard):
    with open(SCOREBOARD_FILE, "w") as f:
        json.dump(scoreboard, f, indent=4)

def update_score(scoreboard, player_name):
    if player_name in scoreboard:
        scoreboard[player_name] += 1
    else:
        scoreboard[player_name] = 1
