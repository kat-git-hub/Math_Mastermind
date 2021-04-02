import random

QUIZ_RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20
PROGRESSION_LENGTH = 20
SIZE_MIN = 2
SIZE_MAX = 4


def get_right_answer():
    min_value = random.randint(MIN_NUMBER, MAX_NUMBER)
    max_value = min_value + PROGRESSION_LENGTH
    step = random.randint(SIZE_MIN, SIZE_MAX)
    progression_with_hidden = get_progression(min_value, max_value, step)
    index = random.randint(0, (len(progression_with_hidden) - 1))
    right_answer = progression_with_hidden[index]
    task = hide_element(progression_with_hidden, index)
    return right_answer, task


def get_progression(min_value, max_value, step):
    progression = list(range(min_value, max_value, step))
    return progression


def hide_element(progression, index):
    progression[index] = '..'
    question_string = ' '.join(map(str, progression))
    return question_string
