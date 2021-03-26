import random


Task = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'
min = 2
max = 20


def getRightAnswer():
    num = random.randint(min, max)
    ask_a_question = (f'Question: {num}')
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                rightAnswer = 'no'
                return rightAnswer, ask_a_question
        else:
            rightAnswer = 'yes'
            return rightAnswer, ask_a_question
