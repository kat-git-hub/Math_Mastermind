import random


TASK = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
MIN_NUM = 2
MAX_NUM = 20


def getRightAnswer():
    num = random.randint(MIN_NUM, MAX_NUM)
    ask_a_question = (f'Question: {num}')
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                rightAnswer = 'no'
                return rightAnswer, ask_a_question
        else:
            rightAnswer = 'yes'
            return rightAnswer, ask_a_question
