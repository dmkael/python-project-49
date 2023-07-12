import prompt
from brain_games.games.game_calc import calc
from brain_games.games.game_even import even
from brain_games.games.game_gcd import gcd
from brain_games.games.game_progression import progression
from brain_games.games.game_prime import prime


def choose_game():
    chosen_game = prompt.string("""\nSelect your game by number:
1 - Is number even?
2 - Simple math
3 - Max common divider
4 - Arithmetic progression
5 - Is number prime?
Your game: """)
    match chosen_game:
        case "1":
            print(even()[0])
            return 'even()'
        case "2":
            print(calc()[0])
            return 'calc()'
        case "3":
            print(gcd()[0])
            return 'gcd()'
        case "4":
            print(progression()[0])
            return 'progression()'
        case "5":
            print(prime()[0])
            return 'prime()'
        case _:
            print("Unknown game number. Program stopped")
            return exit()


if __name__ == "__main__":
    choose_game()
