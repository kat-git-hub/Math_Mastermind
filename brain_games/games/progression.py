import random

QUIZ_RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20
MIN_STEP = 2
MAX_STEP = 4
MIN_LENGTH = 5
MAX_LENGTH = 5


def play():
    first_term = random.randint(MIN_NUMBER, MAX_NUMBER)
    step = random.randint(MIN_STEP, MAX_STEP)
    progression_length = random.randint(MIN_LENGTH, MAX_LENGTH)
    progression = get_progression(first_term, progression_length, step)
    index = random.randint(0, (len(progression) - 1))
    right_answer = progression[index]
    task = hide_element(progression, index)
    return right_answer, task


def get_progression(first_term, progression_length, step):
    last_term = first_term + (progression_length - 1) * step
    progression = list(range(first_term, last_term + 1, step))
    return progression


def hide_element(progression, index):
    progression[index] = '..'
    question_string = ' '.join(map(str, progression))
    return question_string
