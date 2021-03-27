import random

TASK = 'What number is missing in the progression?'
MIN_NUM = 1
MAX_NUM = 20
PROGRESSION_LENGTH = 20


def getRightAnswer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = num1 + PROGRESSION_LENGTH
    step = random.randint(2, 4)
    progression = list(range(num1, num2, step))
    index = random.randint(0, (len(progression) - 1))
    rightAnswer = progression[index]
    question_string = progression
    question_string[index] = ' .. '
    question_string = ' '.join(map(str, progression))
    ask_a_question = (f'Question: {(question_string)}')
    return rightAnswer, ask_a_question
