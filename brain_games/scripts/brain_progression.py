#!/usr/bin/env python3
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def progression():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What number is missing in the progression?")
    play_game(name, "progression()")


if __name__ == "__main__":
    progression()