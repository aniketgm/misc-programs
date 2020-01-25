# Program that implements the game of Rock-Paper-Scissors to play with the
# computer. Game is played between only a Computer and a User.
#
# Program flow:
#  * Computer randomly generates an answer.
#  * Ask user for an answer.
#  * Compare answers and display who wins that round.
#  * Most wins after 3 rounds wins the Game.
#

import random

def printRules():
    print('')
    print(' ########### Rock - Paper - Scissor Game ###########')
    print('')
    print(' Rules are simple,')
    print('     Rock smashes Scissor | Scissor cuts Paper | Paper covers Rock')
    print('')
    print(' 3 Rounds. Choices: Rock | Paper | Scissor')

def getRoundWinner(ans1, ans2):
    gameRules = [ ['Rock','Paper'], ['Paper','Scissor'], ['Scissor','Rock'] ]
    try:
        return gameRules.index([ans1,ans2]) 
    except ValueError:
        return -1

def main():
    printRules()
    CompWin = 0
    UserWin = 0
    gameElems = ['Rock', 'Paper', 'Scissor']
    cntr = 0
    while cntr < 3:
        print('')
        print(' Round ' + str(cntr+1) + ' : ')
        CompAns = random.choice(gameElems)
        print(' Computer\'s choice is generated')
        UserAns = input(' Your choice?: ')
        if UserAns not in gameElems:
            print(' Wrong answer. Please choose among \'Rock\', \'Paper\', Or \'Scissor\'')
            continue
        print(' Computer\'s choice: ' + CompAns)
        if getRoundWinner(CompAns, UserAns) >= 0:
            UserWin += 1
        elif getRoundWinner(UserAns, CompAns) >= 0:
            CompWin += 1
        cntr += 1
    if CompWin > UserWin:
        winner = 'Computer. Better luck next time'
    elif UserWin > CompWin:
        winner = 'You. Congrats'
    else:
        winner = 'no one. It\'s a Tie'
    print('')
    print(' And the winner is : ' + winner + '!!')
    print('')

if __name__ == '__main__':
    main()
