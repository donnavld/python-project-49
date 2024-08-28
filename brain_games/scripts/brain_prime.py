import random
from brain_games.cli import welcome_user


def check_prime(n):
    if n <= 1:
        return 'n'

    for i in range(2, n):
        if n % i == 0:
            return 'n'

    return 'y'


def main():
    name = welcome_user()
    # print(f'Welcome to The Prime Number game, {name}!\n')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    user_try = 0
    while user_try < 3:
        num_random = random.randint(0, 100)
        is_prime = check_prime(num_random)
        # user_answer = input(f'Is this number {num_random} prime? Enter y/n :').lower()
        user_answer = input(f'Question: {num_random} \nYour answer: ').lower()
        # while user_answer[0] not in ['y', 'n']:
        # user_answer = input('Please enter "yes" or "no" or just "y" or "n":').lower()
        if is_prime == user_answer[0]:
            print("Correct!")
            user_try += 1
        else:
            # print("Incorrect.\n")
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{is_prime}'."
            )
            break

    if user_try == 3:
        # print('Congratulations! You won!')
        print(f'Congratulations, {name}!')
    else:
        # print('You lose.')
        print(f"Let's try again, {name}!")
