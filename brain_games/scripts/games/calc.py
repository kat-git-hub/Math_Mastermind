
import operator
import random

TASK = 'What is the result of the expression?'
MIN_NUM = 1
MAX_NUM = 10


def getRightAnswer():
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    op, fn = random.choice(operators)
    rightAnswer = fn(num1, num2)
    ask_a_question = ("Question: {} {} {}".format(num1, op, num2))
    return rightAnswer, ask_a_question
