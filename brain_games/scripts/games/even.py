import random

Task = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def getRightAnswer():
    generateNum = random.randint(1, 100)
    ask_a_question = (f'Question: {generateNum}')

    if generateNum % 2 == 0:
        rightAnswer = 'yes'
        return rightAnswer, ask_a_question
    else:
        rightAnswer = 'no'
        return rightAnswer, ask_a_question


def bool_to_string(value):
    if value is True:
        return 'yes'
    if value is False:
        return 'no'
