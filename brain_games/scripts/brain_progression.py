#!/usr/bin/env python3
from brain_games.games.game_progression import progression
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(progression()[0])
    play_game(name, "progression()")


if __name__ == "__main__":
    main()
