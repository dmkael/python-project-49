#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_calc import TASK, run_calc


def calculate():
    play_one_game(TASK, run_calc)


if __name__ == "__main__":
    calculate()
