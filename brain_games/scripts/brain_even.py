import random
from brain_games.cli import welcome_user


def main():
    print('wellcome')
    name = welcome_user()
    print(f'Welcome to The Even Number game, {name}!\n')

    user_try = 0
    while user_try < 3:
        set_number = random.randint(0, 100)
        is_even = 'y' if set_number % 2 == 0 else 'n'
        user_answer = input(f'Is this number {set_number} even? Enter y/n: ').lower()
        while user_answer[0] not in ['y', 'n']:
            user_answer = input('Please enter "yes" or "no" or just "y" or "n":').lower()
        if is_even == user_answer[0]:
            print("Correct!\n")
            user_try += 1
        else:
            print("Incorrect.\n")
            break
    if user_try == 3:
        print('Congratulations! You won!')
    else:
        print('You lose.')
