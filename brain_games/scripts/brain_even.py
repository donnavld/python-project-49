import random
from brain_games.cli import welcome_user


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    user_try = 0
    while user_try < 3:
        set_number = random.randint(0, 100)
        is_even = 'y' if set_number % 2 == 0 else 'n'
        correct_answer = 'yes' if set_number % 2 == 0 else 'no'
        user_answer = input(f'Question: {set_number} \nYour answer: ').lower()
        # user_answer = input(f'Is this number {set_number} even? Enter y/n: ')
        # .lower()
        # while user_answer[0] not in ['y', 'n']:
        # user_answer = input('Please enter "yes" or "no" or just "y"
        # or "n":').lower()
        if is_even == user_answer[0]:
            print("Correct!")
            user_try += 1
        else:
            # print("Incorrect.\n")
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            break
    if user_try == 3:
        print(f'Congratulations, {name}!')
    else:
        # print('You lose.')
        print(f"Let's try again, {name}!")
