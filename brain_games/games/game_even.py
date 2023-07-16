import random
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def run_even():
    task_phrase = random.randint(1, 99)
    result = is_even(task_phrase) and "yes" or "no"
    return QUESTION, task_phrase, result
