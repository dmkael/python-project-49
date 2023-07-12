import random


def progression():
    question = "What number is missing in the progression?"
    prog_length = random.randint(8, 13)
    progressor = random.randint(2, 10)
    start_num = random.randint(0, 50)
    expression = [start_num]
    for index in range(1, prog_length + 1):
        start_num += progressor
        expression.append(start_num)
    result = expression[random.randint(0, prog_length)]
    expression[expression.index(result)] = ".."
    expression = ' '.join(str(i) for i in expression)
    result = str(result)
    return question, expression, result


if __name__ == "__main__":
    progression()
