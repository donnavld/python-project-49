import random
import operator
# import re
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    # print(f'Welcome to the Calculator game, {name}!\n')
    print('What is the result of the expression?')
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    # used_simbols = re.compile(r'^-?\d+$')
    user_try = 0
    while user_try < 3:
        operation = random.choice(list(operations.keys()))
        num1 = random.randint(0, 10)
        num2 = random.randint(0, 10)
        result = operations[operation](num1, num2)
        user_result = input(f'Question: {num1} {operation} {num2} \nYour answer: ')
        # while not used_simbols.match(user_result):
        # ser_result = input('Please enter just numbers:')
        if result == int(user_result):
            print("Correct!")
            user_try += 1
        else:
            # print("Incorrect.")
            print(
                f"'{user_result}' is wrong answer ;(. "
                f"Correct answer was '{result}'."
            )
            break
    if user_try == 3:
        # print('Congratulations! You won!')
        print(f'Congratulations, {name}!')
    else:
        # print('You lose.')
        print(f"Let's try again, {name}!")
