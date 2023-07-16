import prompt
ROUNDS = 3


def execute_game(name, game):
    points = 0
    question = game()[0]
    print(question)
    while points < ROUNDS:
        task_phrase, result = game()[1:]
        answer = prompt.string(f"Question: {task_phrase} ")
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
