from brain_games.cli import welcome_user
from brain_games.choose_game import choose_game
from brain_games.execute_game import execute_game
import prompt


def play_all_games():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    while True:
        game = choose_game()
        execute_game(name, game)
        run_again = prompt.string("Play new game? y/n ")
        if run_again != 'y':
            break
