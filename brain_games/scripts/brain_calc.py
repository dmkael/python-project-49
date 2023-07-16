#!/usr/bin/env python3
from brain_games.play_one_game import play_one_game
from brain_games.games.game_calc import game_calc


def calculate():
    play_one_game(game_calc)


if __name__ == "__main__":
    calculate()
