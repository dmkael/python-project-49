#!/usr/bin/env python3
from brain_games.start_one_game import play_one_game
from brain_games.games.game_even import TASK, run_even


def play_even():
    play_one_game(TASK, run_even)


if __name__ == "__main__":
    play_even()
