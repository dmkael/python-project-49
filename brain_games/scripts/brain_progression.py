#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_progression import run_progression
from brain_games.games.game_progression import QUESTION


def progression():
    play_one_game(QUESTION, run_progression)


if __name__ == "__main__":
    progression()
