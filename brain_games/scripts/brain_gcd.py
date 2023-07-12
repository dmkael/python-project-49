#!/usr/bin/env python3
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def find_gcd():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    play_game(name, "gcd()")


if __name__ == "__main__":
    find_gcd()
