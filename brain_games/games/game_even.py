import random


def even():
    question = 'Answer "yes" if the number is even, otherwise answer "no".'
    expression = random.randint(1, 99)
    result = expression % 2 == 0 and "yes" or "no"
    return question, expression, result


if __name__ == "__main__":
    even()
