import random

QUIZ_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def play():
    number = random.randint(MIN_NUM, MAX_NUM)
    task = str(number)

    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, task
