#!/usr/bin/env python3
from brain_games.games.game_prime import prime
from brain_games.play_game import play_game
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(prime()[0])
    play_game(name, "prime()")


if __name__ == "__main__":
    main()
