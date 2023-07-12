import random


def prime():
    question = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    expression = random.randint(0, 99)
    if expression < 2:
        result = "no"
        return question, expression, result
    divider = 2
    while divider < expression // 2 + 1:
        if expression % divider == 0:
            result = "no"
            return question, expression, result
        divider += 1
    result = "yes"
    return question, expression, result


if __name__ == "__main__":
    prime()
