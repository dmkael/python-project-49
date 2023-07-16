import prompt
from brain_games.games.game_calc import run_calc
from brain_games.games.game_even import run_even
from brain_games.games.game_gcd import run_gcd
from brain_games.games.game_progression import run_progression
from brain_games.games.game_prime import run_prime


def choose_game():
    chosen_game = prompt.string("""\nSelect your game by number:
1 - Is the number even?
2 - Simple Math
3 - Max common divider
4 - Arithmetic progression
5 - Is the number prime?
Enter game number : """)
    match chosen_game:
        case "1":
            return run_even
        case "2":
            return run_calc
        case "3":
            return run_gcd
        case "4":
            return run_progression
        case "5":
            return run_prime
        case _:
            print("Unknown game number. Program stopped")
            return exit()
