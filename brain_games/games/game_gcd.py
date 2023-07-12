import random


def get_numbers():
    num1 = random.randint(2, 50)
    divs1 = []
    for div1 in range(1, int(num1 // 2 + 1)):
        if num1 % div1 == 0:
            divs1.append(div1)
    num2 = divs1[random.randint(0, len(divs1) - 1)] * random.randint(2, 10)
    while num2 == num1:
        num2 = divs1[random.randint(0, len(divs1) - 1)] * random.randint(2, 10)
    return num1, num2


def gcd():
    question = "Find the greatest common divisor of given numbers."
    num1, num2 = get_numbers()
    expression = f"{num1} {num2}"
    divs = []
    for common_div in range(1, min(num1, num2) + 1):
        if num1 % common_div == 0 and num2 % common_div == 0:
            divs.append(common_div)
    result = str(max(divs))
    return question, expression, result


if __name__ == "__main__":
    gcd()
