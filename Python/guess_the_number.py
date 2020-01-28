# Program for the user to guess the number which is randomly
# generated number by computer

from random import randint

def printdata():
    print('')
    print(" ############ Guess The Number Game ############")
    print('')
    print(" The computer has generated a random number between 0 and 20 ...")
    print('')
    print(' The game is simple')
    print(' Try guessing the number in 5 guesses. Let\'s begin ...')
    print('')

def main():
    randomNum = randint(0, 20)
    printdata()
    cnt = 1
    guessed = False
    while (cnt <= 5):
        guess = int(input(" Guess %d : " % (cnt)))
        if guess > randomNum:
            print(" Your guess is high.")
            print('')
        elif guess < randomNum:
            print(" Your guess is low.")
            print('')
        else:
            guessed = True
            break
        cnt = cnt + 1
    if not guessed:
        print(" Better luck next time !!..")
    else:
        print(" Yay!! you guessed it in %d guesses !!.. " % (cnt))
    print('')

if __name__ == '__main__':
    main()
