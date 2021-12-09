/*
* Assignment 11
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
using namespace std;
int size;
int matrix[100][100];

bool is_symmetric(){
    for (int i = 0; i < size; i++){
        for (int j = 0; j < size; j++)
        {
            if (matrix[i][j] != matrix[size-i-1][size-j-1]){
                return false;
            }
        }
    }
    return true;
}

int main(){
    while(true){
        cout << "Input Size: ";
        cin >> size;
        if (size == -1){
            break;
        }

        for (int i = 0; i < size; i++){
            for (int j = 0; j < size; j++)
            {
                cin >> matrix[i][j];
            }
        }

        if (is_symmetric()){
            cout << "Symmetric!\n";
        }
        else {
            cout << "Non-Symmetric!\n";
        }
    }
    return 0;
}