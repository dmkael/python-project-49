import random
TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    if num < 2:
        return False
    divider = 2
    while divider < num // 2 + 1:
        if num % divider == 0:
            return False
        divider += 1
    return True


def run_prime():
    num = random.randint(0, 99)
    task_phrase = f"{num}"
    result = 'yes' if is_prime(num) else 'no'
    return task_phrase, result
