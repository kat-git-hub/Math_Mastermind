import random
import math
TASK = 'Find the greatest common divisor of given numbers.'
MIN_NUM = 1
MAX_NUM = 20


def getRightAnswer():
    num1 = random.randint(MIN_NUM, MAX_NUM)
    num2 = random.randint(MIN_NUM, MAX_NUM)
    rightAnswer = math.gcd(num1, num2)
    ask_a_question = ("Question: {} {}".format(num1, num2))
    return rightAnswer, ask_a_question
