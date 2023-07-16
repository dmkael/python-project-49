import random
import operator
QUESTION = "What is the result of the expression?"


def action(instruction):
    if instruction == '+':
        return operator.add
    if instruction == '-':
        return operator.sub
    if instruction == '*':
        return operator.mul


def game_calc():
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    instruction = random.choice(['+', '-', '*'])
    task_phrase = f"{num1} {instruction} {num2}"
    result = action(instruction)(num1, num2)
    result = str(result)
    return QUESTION, task_phrase, result
