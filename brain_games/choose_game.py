import prompt
from brain_games.games.game_calc import game_calc
from brain_games.games.game_even import game_even
from brain_games.games.game_gcd import game_gcd
from brain_games.games.game_progression import game_progression
from brain_games.games.game_prime import game_prime


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
            return game_even
        case "2":
            return game_calc
        case "3":
            return game_gcd
        case "4":
            return game_progression
        case "5":
            return game_prime
        case _:
            print("Unknown game number. Program stopped")
            return exit()
