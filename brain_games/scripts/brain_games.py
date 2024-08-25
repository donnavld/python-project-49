#from brain_games.scripts.game_calculator import run_calculator_game
#from brain_games.scripts.game_progression import run_progression_game
#from brain_games.scripts.game_even import run_even_number_game
#from brain_games.scripts.game_greatest_factor import run_greatest_factor_game
#from brain_games.scripts.game_prime import run_prime_number_game
from brain_games.cli import welcome_user

def main():
    name = welcome_user()


if __name__ == '__main__':
    main()
