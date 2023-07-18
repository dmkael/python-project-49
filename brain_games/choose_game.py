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
    if chosen_game == "1":
        return TASK1, run_even
    if chosen_game == "2":
        return TASK2, run_calc
    if chosen_game == "3":
        return TASK3, run_gcd
    if chosen_game == "4":
        return TASK4, run_progression
    if chosen_game == "5":
        return TASK5, run_prime
    else:
        print("Unknown game number. Program stopped")
        exit()
