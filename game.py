from random import choice


def get_score(player):

    file = open('rating.txt', 'r')
    for line in file:
        if player == line.split()[0]:
            file.close()
            return int(line.split()[1])
    file.close()
    return 0


def get_wins(options):

    if options == '':
        wins = {'rock': ['paper'],
                'scissors': ['rock'],
                'paper': ['scissors']}
    else:
        wins = {}
        options = options.split(',')
        number = len(options)
        options += options
        #print(options)
        for i in range(number):
            wins[options.pop(0)] = options[1:number // 2 + 1]
    return wins


def rock_paper_scissors(score, wins):

    players_choice = choice(list(wins))
    while players_choice != '!exit':
        players_choice = input()
        if players_choice == '!exit':
            continue
        if players_choice == '!rating':
            print('Your rating: {}'.format(score))
            continue
        if players_choice not in wins:
            print('Invalid input')
            continue
        computers_choice = choice(list(wins))
        if players_choice == computers_choice:
            print('There is a draw ({})'.format(players_choice))
            score += 50
        elif players_choice in wins[computers_choice]:
            print('Well done. Computer chose {} and failed'.format(computers_choice))
            score += 100
        else:
            print('Sorry, but computer chose ' + computers_choice)
    print('Bye!')


def play_game():
    name = input('Enter your name: ')
    print('Hello,', name)
    score = get_score(name)
    wins = get_wins(input())
    print("Okay, let\'s start")
    rock_paper_scissors(score, wins)

play_game()
