import prompt
from brain_games.games.game_even import run_even, TASK as TASK1
from brain_games.games.game_calc import run_calc, TASK as TASK2
from brain_games.games.game_gcd import run_gcd, TASK as TASK3
from brain_games.games.game_progression import run_progression, TASK as TASK4
from brain_games.games.game_prime import run_prime, TASK as TASK5


def choose_game():
    chosen_game = prompt.string("""\nSelect your game by number:
1 - Is the number even?
2 - Simple Math
3 - Max common divider
4 - Arithmetic progression
5 - Is the number prime?
Enter game number : """)
    game_base = {
        "1": (TASK1, run_even),
        "2": (TASK2, run_calc),
        "3": (TASK3, run_gcd),
        "4": (TASK4, run_progression),
        "5": (TASK5, run_prime)
    }
    if game_base.get(chosen_game) is None:
        print("Unknown game number. Program stopped")
        exit()
    else:
        task, run_game = game_base.get(chosen_game)
    return task, run_game
