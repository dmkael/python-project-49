import random
import math
TASK = "Find the greatest common divisor of given numbers."


def run_gcd():
    num1 = random.randint(0, 50)
    num2 = random.randint(0, 50)
    task_phrase = f"{num1} {num2}"
    result = math.gcd(num1, num2)
    result = str(result)
    return task_phrase, result
