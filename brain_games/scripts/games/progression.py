import random

Task = 'What number is missing in the progression?'


def getRightAnswer():
    num1 = random.randint(1, 10)
    num2 = num1 + 20
    step = random.randint(2, 4)
    ap = list(range(num1, num2, step))
    index = random.randint(0, (len(ap) - 1))
    rightAnswer = ap[index]
    question_list = ap
    question_list[index] = ' .. '
    question_list = ' '.join(map(str, ap))
    ask_a_question = (f'Question: {(question_list)}')
    return rightAnswer, ask_a_question
