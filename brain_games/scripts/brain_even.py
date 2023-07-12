#!/usr/bin/env python3
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def is_even():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(name, "even()")


if __name__ == "__main__":
    is_even()
