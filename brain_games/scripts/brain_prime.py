#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_prime import TASK, run_prime


def play_prime():
    play_one_game(TASK, run_prime)


if __name__ == "__main__":
    play_prime()
