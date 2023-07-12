#!/usr/bin/env python3
from brain_games.play_game import play_game
from brain_games.cli import welcome_user
from brain_games.games.game_calc import calc


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(calc()[0])
    play_game(name, "calc()")


if __name__ == "__main__":
    main()
