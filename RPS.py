import random


def rps_winner(choice1, choice2):
    if choice1 == choice2:
        return choice1
    elif choice1 in ['rock', 'paper'] and choice2 in ['rock', 'paper']:
        return 'paper'
    elif choice1 in ['rock', 'scissors'] and choice2 in ['rock', 'scissors']:
        return 'rock'
    elif choice1 in ['scissors', 'paper'] and choice2 in ['scissors', 'paper']:
        return 'scissors'
    else:
        print('''invalid choice
choose from [r, p, s] ''')


shortcut = {'r': 'rock',
            'p': 'paper',
            's': 'scissors'
            }
your_score = 0
computer_score = 0
points_to_win = int(input('points to win : '))
while your_score < points_to_win and computer_score < points_to_win:
    your_choice = shortcut.get(input('your turn :').lower(), 'error')
    computer_choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_choices)
    winning_choice = rps_winner(your_choice, computer_choice)
    if your_choice == computer_choice:
        print('computer_turn:' + computer_choice)
        print('draw!')

    elif winning_choice == your_choice:
        print('computer_turn:' + computer_choice)
        print('you won this round')
        your_score += 1
        if your_score == points_to_win:
            print('You won the game!')
    elif winning_choice == computer_choice:
        print('computer_turn:' + computer_choice)
        print('you lost this round')
        computer_score += 1
        if computer_score == points_to_win:
            print('you lost the game!')
    else:
        print('try again')
    print('your score : ' + str(your_score))
    print('computer score : ' + str(computer_score))
