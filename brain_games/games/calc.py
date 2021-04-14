
import operator
import random

QUIZ_RULES = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10


def play():
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    number_1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign, operation = random.choice(operators)
    right_answer = operation(number_1, number_2)
    task = "{} {} {}".format(number_1, sign, number_2)
    return right_answer, task
