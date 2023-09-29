import random


def choose_options():
    options = ('stone', 'paper', 'scissor')

    print(' ')
    user_option = input('choose: ')
    user_option = user_option.lower()
    print(' ')

    if user_option == 'exit':
        return None, None
    if user_option not in options:
        print('That option is not valid')
        print(' ')
        return None, None

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    print(' ')
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print('Tie!')
    elif user_option == 'stone':
        if computer_option == 'scissor':
            print('stone beats scissor')
            print('You Win!')
            user_wins += 1
        else:
            print('paper beats stone')
            print('Computer Win!')
            computer_wins += 1

    elif user_option == 'paper':
        if computer_option == 'stone':
            print('paper beats stone')
            print('You Win!')
            user_wins += 1
        else:
            print('scissor beats paper')
            print('Computer Wins!')
            computer_wins += 1

    elif user_option == 'scissor':
        if computer_option == 'paper':
            print('scissor beats paper')
            print('You Win!')
            user_wins += 1
        else:
            print('stone beats scissor')
            print('Computer Wins!')
            computer_wins += 1
    return user_wins, computer_wins


def run_game():
    computer_wins = 0
    user_wins = 0

    rounds = 1

    while True:
        print('*' * 30)
        print(' ' * 10, 'Round:', rounds)
        print('*' * 30)

        print('You:', user_wins, ' ' * 10, 'Computer:', computer_wins)
        print(' ')

        print('We´re gonna play scissor, paper, stone to decide.')

        rounds += 1

        user_option, computer_option = choose_options()
        if user_option is None or computer_option is None:
            break

        user_wins, computer_wins = check_rules(
            user_option, computer_option, user_wins, computer_wins)

        if computer_wins == 2:
            print(' ')
            print(
                f'The winner of the game is the Computer! in {rounds - 1} rounds.')
            break
        if user_wins == 2:
            print(' ')
            print(f'You are the winner of the game! in {rounds - 1} rounds.')
            break

        print(' ')


run_game()
