/****************************************************************************
 * Program that implements the game of Rock-Paper-Scissors to play with the *
 * computer. Game is played between only a Computer and a User.             *
 *                                                                          *
 * Program flow:                                                            *
 *  > Computer randomly generates an answer.                                *
 *  > Ask user for an answer.                                               *
 *  > Compare answers and display who wins that round.                      *
 *  > Most wins after 3 rounds wins the Game.                               *
 ****************************************************************************/

#include <iostream>
#include <vector>
#include <algorithm>
#include <random>

// The std namespace conatins a whole lot of functions. Dont want to load all that in the program.
// Hence using only what's required.
using std::cout;
using std::cin;
using std::endl;
using std::pair;
using std::vector;
using std::string;
using std::find;
using std::make_pair;
using std::random_device;
using std::mt19937;
using std::uniform_int_distribution;

typedef pair< string, string > StrPair;

vector < StrPair > rulePairsVec = {
    make_pair("Rock",   "Paper"  ),
    make_pair("Paper",  "Scissor"),
    make_pair("Scissor","Rock"   )
};

void printRules() {
    cout << endl << " ########### Rock - Paper - Scissor Game ###########" << endl;
    cout << endl << " Rules are simple," << endl;
    cout << "     Rock smashes Scissor | Scissor cuts Paper | Paper covers Rock" << endl;
    cout << endl << " 3 Rounds. Choices: Rock | Paper | Scissor" << endl;
}

int getRoundWinner(string ans1, string ans2) {
    vector< StrPair >::const_iterator vecIt = find(rulePairsVec.begin(), rulePairsVec.end(), make_pair(ans1, ans2));
    if( vecIt != rulePairsVec.end() )
        return 1;
    return 0;
}

int main() {
    printRules();
    string compCh = "", userCh = "", winner = "";
    size_t compWin = 0, userWin = 0, rnd = 0;
    vector< string > gameChoices = { "Rock", "Paper", "Scissor" };
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<> dis(0, 2);
    while (rnd < 3)
    {
        cout << endl;
        cout << " Round " << rnd << " : " << endl;
        compCh = gameChoices[dis(gen)];
        cout << " Computer's choice is generated ..." << endl;
        cout << " Your choice? : ";
        cin >> userCh;
        vector< string >::const_iterator vecIt = find(gameChoices.begin(), gameChoices.end(), userCh);
        if ( vecIt == gameChoices.end() ) {
            cout << "Wrong choice. Please choose among 'Rock', 'Paper', Or 'Scissor'" << endl;
            continue;
        }
        cout << " Computer's choice : " << compCh << endl;
        userWin += getRoundWinner(compCh, userCh);
        compWin += getRoundWinner(userCh, compCh);
        ++rnd;
    }
    if(compWin > userWin)
        winner = "Computer. Better luck next time";
    else if(userWin > compWin)
        winner = "You. Congrats";
    else
        winner = "no one. It's a Tie";
    cout << endl << " And the winner is : " << winner << " !!" << endl << endl;
    return 0;
}

