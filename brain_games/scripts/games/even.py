import random

QUIZ_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUM = 1
MAX_NUM = 100


def get_right_answer():
    generate_number = random.randint(MIN_NUM, MAX_NUM)
    task = (f'{generate_number}')

    if generate_number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, task
