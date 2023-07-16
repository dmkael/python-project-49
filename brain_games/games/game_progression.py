import random

QUESTION = "What number is missing in the progression?"


def generate_progression(prog_length, progressor, start_num):
    progression = [start_num]
    for index in range(1, prog_length + 1):
        start_num += progressor
        progression.append(start_num)
    return progression


def game_progression():
    prog_length = random.randint(8, 13)
    progressor = random.randint(2, 10)
    start_num = random.randint(0, 50)
    task_phrase = generate_progression(prog_length, progressor, start_num)
    # random choice for result from task phrase progression
    result = task_phrase[random.randint(0, prog_length)]
    # replace chosen result with dots to 'hide' result
    task_phrase[task_phrase.index(result)] = ".."
    # convert task phrase list to str
    task_phrase = ' '.join(str(i) for i in task_phrase)
    result = str(result)
    return QUESTION, task_phrase, result
