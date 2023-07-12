#!/usr/bin/env python3
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print("What is the result of the expression?")
    play_game(name, "calc()")


if __name__ == "__main__":
    main()
