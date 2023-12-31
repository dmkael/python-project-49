import prompt
MAX_ROUNDS = 3


def execute_game(task, name, run_game):
    current_round = 1
    print(task)
    while current_round <= MAX_ROUNDS:
        task_phrase, result = run_game()
        answer = prompt.string(f"Question: {task_phrase} ")
        print(f"Your answer is: {answer}")
        if answer == result:
            print("Correct!")
            current_round += 1
        else:
            print(f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{result}'\n"
                  f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
