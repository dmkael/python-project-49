import random


def calc():
    question = "What is the result of the expression?"
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-', '*'])

    expression = f"{num1} {operator} {num2}"

    if operator == '+':
        result = num1 + num2
    if operator == '-':
        result = num1 - num2
    if operator == '*':
        result = num1 * num2
    result = str(result)
    return question, expression, result


if __name__ == "__main__":
    print(calc())
