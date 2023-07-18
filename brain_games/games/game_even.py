import random

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    result = num % 2 == 0
    return result


def run_even():
    num = random.randint(1, 99)
    result = "yes" if is_even(num) else "no"
    task_phrase = f"{num}"
    return task_phrase, result
