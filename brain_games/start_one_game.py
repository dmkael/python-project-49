from brain_games.cli import welcome_user
from brain_games.execute_game import execute_game


def play_one_game(question, game):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    execute_game(question, name, game)
