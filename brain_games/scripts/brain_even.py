#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_even import run_even
from brain_games.games.game_even import QUESTION


def even_or_no():
    play_one_game(QUESTION, run_even)


if __name__ == "__main__":
    even_or_no()
