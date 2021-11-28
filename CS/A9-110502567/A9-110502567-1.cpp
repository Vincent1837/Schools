/*
* Assignment 9
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
#include <iostream>
using namespace std;
int main(){
    int A[5][5], B[5][5];
    int rawA, rawB, colA, colB;
    cout << "Enter the size of A: "; cin >> rawA >> colA;
    cout << "Enter the size of B: "; cin >> rawB >> colB;
    if (colA == rawB){
        cout << "Enter A:\n";
        for (int i = 0; i < rawA; i++){
            for (int j = 0; j < colA; j++){
                cin >> A[i][j];
            }
        }
        cout << "Enter B:\n";
        for (int i = 0; i < rawB; i++){
            for (int j = 0; j < colB; j++){
                cin >> B[i][j];
            }
        }
        cout << "A x B =\n";
        for (int i = 0; i < rawA; i++){
            for (int j = 0; j < colB; j++){
                int number = 0;
                for (int k = 0; k < colA; k++){                    
                    number += A[i][k] * B[k][j];
                }
                cout << number << " ";
            }
            cout << "\n";
        }
    }
    else {
        cout << "Can't be multiplied.\n";
    }
    return 0;
}