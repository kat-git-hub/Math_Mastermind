import random
from math import sqrt

QUIZ_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def play():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    task = str(number)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, task


def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, int(sqrt(number) + 1)):
        if (number % divisor) == 0:
            return False
    return True
