import prompt
from brain_games.games.game_even import run_even
from brain_games.games.game_even import QUESTION as QUESTION1
from brain_games.games.game_calc import run_calc
from brain_games.games.game_calc import QUESTION as QUESTION2
from brain_games.games.game_gcd import run_gcd
from brain_games.games.game_gcd import QUESTION as QUESTION3
from brain_games.games.game_progression import run_progression
from brain_games.games.game_progression import QUESTION as QUESTION4
from brain_games.games.game_prime import run_prime
from brain_games.games.game_prime import QUESTION as QUESTION5


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
            return QUESTION1, run_even
        case "2":
            return QUESTION2, run_calc
        case "3":
            return QUESTION3, run_gcd
        case "4":
            return QUESTION4, run_progression
        case "5":
            return QUESTION5, run_prime
        case _:
            print("Unknown game number. Program stopped")
            return exit()
