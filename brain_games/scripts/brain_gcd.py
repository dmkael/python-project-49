#!/usr/bin/env python3
from brain_games.play_one_game import play_one_game
from brain_games.games.game_gcd import game_gcd


def find_gcd():
    play_one_game(game_gcd)


if __name__ == "__main__":
    find_gcd()
