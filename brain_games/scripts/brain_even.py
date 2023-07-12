#!/usr/bin/env python3
from brain_games.games.game_even import even
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(even()[0])
    play_game(name, "even()")


if __name__ == "__main__":
    main()
