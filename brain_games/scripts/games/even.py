import random

TASK = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'
MIN_NUM = 1
MAX_NUM = 100


def getRightAnswer():
    generateNum = random.randint(MIN_NUM, MAX_NUM)
    ask_a_question = (f'Question: {generateNum}')

    if generateNum % 2 == 0:
        rightAnswer = 'yes'
        return rightAnswer, ask_a_question
    else:
        rightAnswer = 'no'
        return rightAnswer, ask_a_question
