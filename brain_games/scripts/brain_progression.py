#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_progression import TASK, run_progression


def play_progression():
    play_one_game(TASK, run_progression)


if __name__ == "__main__":
    play_progression()
