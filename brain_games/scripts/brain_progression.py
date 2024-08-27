import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    #print(f'Welcome to The Progression game, {name}!\n')
    print('What number is missing in the progression?')

    user_try = 0
    while user_try < 3:
        step = random.randint(0, 10)
        start = random.randint(0, 10)
        length = 10
        progression = [start + step * i for i in range(length)]
        missing_number = random.choice(progression)
        index = progression.index(missing_number)
        progression[index] = '..'
        # print('Look at a progression')
        # print(progression)
        # print(missing_number)
        # user_number = input('Enter the missing : ')
        question = ' '.join(map(str, progression))
        user_number = input(f'Question: {question} \nYour answer: ')
        # while not user_number.isdigit():
        # user_number = input('Please enter just numbers:')
        if int(user_number) == int(missing_number):
            print("Correct!")
            user_try += 1
        else:
            # print("Incorrect.\n")
            print(f"'{user_number}' is wrong answer ;(. Correct answer was '{missing_number}'.")
            break

    if user_try == 3:
        # print('Congratulations! You won!')
        print(f'Congratulations, {name}!')
    else:
        # print('You lose.')
        print(f"Let's try again, {name}!")

