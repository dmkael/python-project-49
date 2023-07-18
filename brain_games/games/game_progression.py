import random

TASK = "What number is missing in the progression?"


def generate_progression(prog_length, progressor, start_num):
    progression = [start_num]
    for index in range(1, prog_length):
        start_num += progressor
        progression.append(start_num)
    return progression


def run_progression():
    prog_length = random.randint(9, 11)
    progressor = random.randint(2, 10)
    start_num = random.randint(0, 50)
    progression = generate_progression(prog_length, progressor, start_num)

    result_index = random.randint(0, prog_length - 1)
    result = progression[result_index]
    progression[result_index] = ".."

    task_phrase = " ".join(str(i) for i in progression)
    result = str(result)
    return task_phrase, result
