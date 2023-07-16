import random
QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    divider = 2
    while divider < num // 2 + 1:
        if num % divider == 0:
            return False
        divider += 1
    return True


def game_prime():
    task_phrase = random.randint(0, 99)
    result = is_prime(task_phrase) and 'yes' or 'no'
    return QUESTION, task_phrase, result
