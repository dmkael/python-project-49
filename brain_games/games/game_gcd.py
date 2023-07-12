import random


def gcd():
    question = "Find the greatest common divisor of given numbers."
    num1 = random.randint(2, 50)
    divs1 = []
    for div1 in range(1, int(num1 // 2 + 1)):
        if num1 % div1 == 0:
            divs1.append(div1)
    num2 = divs1[random.randint(0, len(divs1) - 1)] * random.randint(2, 10)
    while num2 == num1:
        num2 = divs1[random.randint(0, len(divs1) - 1)] * random.randint(2, 10)
    expression = f"{num1} {num2}"
    result = []
    for common_div in range(1, min(num1, num2) + 1):
        if num1 % common_div == 0 and num2 % common_div == 0:
            result.append(common_div)
    result = str(max(result))
    return question, expression, result


if __name__ == "__main__":
    gcd()
