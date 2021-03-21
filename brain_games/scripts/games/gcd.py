import random
import math
Task = 'Find the greatest common divisor of given numbers.'


def getRightAnswer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    rightAnswer = math.gcd(num1, num2)
    ask_a_question = ("Question: {} {}".format(num1, num2))
    return rightAnswer, ask_a_question
