import random

QUIZ_RULES = 'What number is missing in the progression?'
MIN_NUMBER = 1
MAX_NUMBER = 20
PROGRESSION_LENGTH = 20
STEP_MIN = 2
STEP_MAX = 4


def game_round():
    min = random.randint(MIN_NUMBER, MAX_NUMBER)
    length = min + PROGRESSION_LENGTH
    step = random.randint(STEP_MIN, STEP_MAX)
    progression = get_progression(min, length, step)
    index = random.randint(0, (len(progression) - 1))
    right_answer = progression[index]
    task = hide_element(progression, index)
    return right_answer, task


def get_progression(min, length, step):
    progression = list(range(min, length, step))
    return progression


def hide_element(progression, index):
    progression[index] = '..'
    question_string = ' '.join(map(str, progression))
    return question_string
