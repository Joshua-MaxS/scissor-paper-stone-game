import random


options = ('stone', 'paper', 'scissor')

computer_wins = 0
user_wins = 0

rounds = 1

while True:

    print('*' * 30)
    print(' ' * 10, 'Round:', rounds)
    print('*' * 30)

    print('You:', user_wins, ' ' * 10, 'Computer:', computer_wins)
    print(' ')

    print('We´re gonna play scissor, paper, stone to decide')

    print(' ')
    user_option = input('choose: ')
    user_option = user_option.lower()
    print(' ')

    rounds += 1

    if user_option == 'salir':
        break
    if not user_option in options:
        print('That option is not valid')
        print(' ')
        continue

    computer_option = random.choice(options)

    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    print(' ')

    if user_option == computer_option:
        print('Tie!')
    elif user_option == 'stone':
        if computer_option == 'scissor':
            print('stone beats scissor')
            print('You Win!')
            user_wins += 1
        else:
            print('paper beats scissor')
            print('Computer Win!')
            computer_wins += 1

    elif user_option == 'paper':
        if computer_option == 'stone ':
            print('paper beats scissor')
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
            print('stone  beats scissor')
            print('Computer Wins!')
            computer_wins += 1

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
