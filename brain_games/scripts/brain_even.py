import random

from brain_games import cli
name = cli.welcome_user()


def main():
    even_check()


if __name__ == '__main__':
    main()


def user_replies(usr_answer):
    if usr_answer == 'yes':
        return True
    if usr_answer == 'no':
        return False


def is_even(generateNum):
    if generateNum % 2 == 0:
        return True
    else:
        return False


def bool_to_string(value):
    if value is True:
        return 'yes'
    if value is False:
        return 'no'


def even_check():
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    count = 0
    while count <= 3:
        generateNum = random.randint(1, 100)
        print(f'Question: {generateNum}')
        usr_answer = input('Your answer: ')
        if is_even(generateNum) == user_replies(usr_answer):
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {name}!')
                break
        else:
            print(f""" '{usr_answer}' is wrong answer. \
Correct answer was '{bool_to_string(is_even(generateNum))}'.
Let's try again, {name}!""")
            break
