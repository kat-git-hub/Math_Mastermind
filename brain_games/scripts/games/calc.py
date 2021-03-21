
import operator
import random

Task = 'What is the result of the expression?'


def getRightAnswer():
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    op, fn = random.choice(operators)
    rightAnswer = fn(num1, num2)
    ask_a_question = ("Question: {} {} {}".format(num1, op, num2))
    return rightAnswer, ask_a_question
