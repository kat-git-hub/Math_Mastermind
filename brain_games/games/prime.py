import random


QUIZ_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 20


def game_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    task = str(number)
    right_answer = get_prime(number)
    return right_answer, task


def get_prime(number):
    for divisor in range(2, number):
        if (number % divisor) == 0:
            return 'no'
    return 'yes'
