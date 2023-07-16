#!/usr/bin/env python3
from brain_games.play_one_game import play_one_game
from brain_games.games.game_even import game_even


def even_or_no():
    play_one_game(game_even)


if __name__ == "__main__":
    even_or_no()
