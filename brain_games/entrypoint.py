import prompt


ATTEMPTS_NUMBER = 3


def start(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUIZ_RULES)
    for i in range(ATTEMPTS_NUMBER):
        right_answer, task = game.game_round()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if str(right_answer) == answer:
            print('Correct!')
        else:
            print(f""" '{answer}' is wrong answer. \
Correct answer was '{right_answer}'.
Let's try again, {name}!""")
            return
    print(f'Congratulations, {name}!')
