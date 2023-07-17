#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_prime import run_prime
from brain_games.games.game_prime import QUESTION


def prime_or_no():
    play_one_game(QUESTION, run_prime)


if __name__ == "__main__":
    prime_or_no()
