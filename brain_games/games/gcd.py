import random


QUIZ_RULES = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 20


def play():
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = gcd(number_1, number_2)
    task = "{} {}".format(number_1, number_2)
    return right_answer, task


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
