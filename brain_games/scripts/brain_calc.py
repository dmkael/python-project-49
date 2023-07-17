#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_calc import run_calc
from brain_games.games.game_calc import QUESTION


def calculate():
    play_one_game(QUESTION, run_calc)


if __name__ == "__main__":
    calculate()
