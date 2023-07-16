#!/usr/bin/env python3
from brain_games.play_one_game import play_one_game
from brain_games.games.game_progression import game_progression


def progression():
    play_one_game(game_progression)


if __name__ == "__main__":
    progression()
