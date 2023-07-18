import random
import operator
TASK = "What is the result of the expression?"


def get_operation(instruction):
    if instruction == '+':
        return operator.add
    if instruction == '-':
        return operator.sub
    if instruction == '*':
        return operator.mul


def run_calc():
    num1 = random.randint(0, 20)
    num2 = random.randint(0, 20)
    instruction = random.choice(['+', '-', '*'])
    task_phrase = f"{num1} {instruction} {num2}"
    result = get_operation(instruction)(num1, num2)
    result = str(result)
    return task_phrase, result
