import random
QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    result = num % 2 == 0
    return result


def run_even():
    task_phrase = random.randint(1, 99)
    result = is_even(task_phrase) and "yes" or "no"
    return task_phrase, result
