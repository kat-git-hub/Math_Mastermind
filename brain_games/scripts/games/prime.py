import random


QUIZ_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 2
MAX_NUMBER = 20


def get_right_answer():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    task = (f'{number}')
    right_answer = is_prime(number)
    return right_answer, task


def is_prime(value):
    if value > 1:
        for i in range(2, value):
            if (value % i) == 0:
                result = 'no'
                break
        else:
            result = 'yes'
        return result
