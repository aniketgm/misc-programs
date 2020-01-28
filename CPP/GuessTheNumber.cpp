/**************************************************************
 * Program for the user to guess the number which is randomly *
 * generated number by computer                               *
 **************************************************************/

#include <iostream>
#include <random>

using std::cout;
using std::cin;
using std::endl;
using std::random_device;
using std::mt19937;
using std::uniform_int_distribution;

void printdata() {
    cout << endl << " ############ Guess The Number Game ############" << endl;
    cout << endl << " The computer has generated a random number between 0 and 20 ..." << endl;
    cout << endl << " The game is simple";
    cout << endl << " Try guessing the number in 5 guesses. Let's begin ..." << endl;
}

int main() {
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 20);
    printdata();
    size_t cnt = 1, guess, randomNum = dis(gen);
    bool guessed = false;
    while (cnt <= 5) {
        cout << endl << " Guess " << cnt << " : ";
        cin >> guess;
        if (guess > randomNum)
            cout << " Your guess is high." << endl;
        else if (guess < randomNum)
            cout << " Your guess is low." << endl;
        else {
            guessed = true;
            break;
        }
        cnt += 1;
    }
    if (!guessed)
        cout << " Better luck next time !!.." << endl;
    else
        cout << " Yay!! you guessed it in " << cnt << " guesses !!.. " << endl;
    cout << endl;
}
