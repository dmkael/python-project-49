from brain_games.choose_game import choose_game
from brain_games.choose_game import calc, even, gcd, progression, prime
from brain_games.cli import welcome_user
import prompt


def play_game(name, game):
    points = 0
    while points < 3:
        expression, result = eval(game)[1:3]
        answer = prompt.string(f"Question: {expression} ")
        print(f"Your answer is: {answer}")
        if answer == result:
            print("Correct!")
            points += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")


def brain_games():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    game = choose_game()
    play_game(name, game)


if __name__ == "__main__":
    calc()
    even()
    gcd()
    prime()
    progression()
    brain_games()
