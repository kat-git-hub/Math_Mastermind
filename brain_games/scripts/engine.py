
from brain_games import cli


def getCheck(game):
    name = cli.welcome_user()
    print(game.Task)
    count = 0
    while count <= 3:
        rightAnswer, ask_a_question = game.getRightAnswer()
        print(ask_a_question)
        usr_answer = input('Your answer: ')
        if str(rightAnswer) == usr_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f""" '{usr_answer}' is wrong answer. \
Correct answer was '{rightAnswer}'.
Let's try again, {name}!""")
            break
