import random
from brain_games.cli import welcome_user


def get_greatest_factor(num1, num2):
    while num1 != 0:
        num2, num1 = num1, num2 % num1
    return num2


def main():
    name = welcome_user()
    # print(f'Welcome to The Greatest Common Factor game, {name}!\n')
    print('Find the greatest common divisor of given numbers.')
    user_try = 0
    while user_try < 3:
        num1 = random.randint(0, 100)
        num2 = random.randint(0, 100)
        greatest_factor = get_greatest_factor(num1, num2)
        # print (greatest_factor)
        # user_answer = input(f'Enter the  Greatest Common Factor for {num1} and {num2} : ')
        user_answer = input(f'Question: {num1} {num2} \nYour answer: ')
        # while not user_answer.isdigit():
        # user_answer = input('Please enter just number:')
        if greatest_factor == int(user_answer):
            print("Correct!")
            user_try += 1
        else:
            # print("Incorrect.\n")
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{greatest_factor}'."
            )
            break

    if user_try == 3:
        # print('Congratulations! You won!')
        print(f'Congratulations, {name}!')
    else:
        # print('You lose.')
        print(f"Let's try again, {name}!")
