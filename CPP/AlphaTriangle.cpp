/*
 *  Program to print the following output:
 *
 *	A B C D E F G F E D C B A
 *	A B C D E F   F E D C B A
 *	A B C D E       E D C B A
 *	A B C D           D C B A
 *	A B C               C B A
 *	A B                   B A
 *	A                       A
 */

#include <iostream>

// std is a big namespace. only using what's required from it.
using std::cout;
using std::endl;

int main(){
    int i, cnt = 0, j = 71, k = 0;
    cout << endl;
    while(cnt < 8){
        cout << " ";
        for( i = 65; i <= j; i++)	cout << " " << (char)i;
        for( i = 0; i < k; i++ )	cout << " ";
        for( i = j; i >= 65; i--){
            if( i == 71 ){
                cout << " ";
                continue;
            }
            cout << (char)i << " ";
        }
        cout << endl;
        j--;
        cnt++;
        k = (cnt * 3) + (cnt - 1);
    }
}
