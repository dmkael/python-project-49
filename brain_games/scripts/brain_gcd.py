#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_gcd import TASK, run_gcd


def find_gcd():
    play_one_game(TASK, run_gcd)


if __name__ == "__main__":
    find_gcd()
