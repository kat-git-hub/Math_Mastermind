import prompt


ATTEMPTS = 3


def play_on(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.QUIZ_RULES)
    for i in range(ATTEMPTS):
        right_answer, task = game.get_right_answer()
        print(f'Question: {task}')
        answer = prompt.string('Your answer: ')
        if str(right_answer) == answer:
            print('Correct!')
            if i == ATTEMPTS - 1:
                print(f'Congratulations, {name}!')
                break
            i += 1
        else:
            print(f""" '{answer}' is wrong answer. \
Correct answer was '{right_answer}'.
Let's try again, {name}!""")
            break
