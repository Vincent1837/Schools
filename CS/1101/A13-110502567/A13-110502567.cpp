/*
* Assignment 13
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
# include <fstream>
using namespace std;

char judge(char[9][9]);

int main(){
    for (string file_name : {"sudo1", "sudo2", "sudo3"}){
        char sudoku[9][9];
        ifstream inFile(file_name+".txt", ios::in);
        if (!inFile){
            cout << "No such file!\n";
        }
        else{
            for (int i = 0; i < 9; i++){
                for (int j = 0; j < 9; j++){
                    inFile >> sudoku[i][j];
                }
            }
            cout << file_name << ':' << judge(sudoku) << '\n';
        }
    }
    return 0;
}

char judge(char matrix[9][9]){
    for (int i = 0; i < 9; i++){
        string row_nums = "";
        string col_nums = "";
        for (int j = 0; j < 9; j++){
            if (row_nums.find_first_of(matrix[i][j]) >= row_nums.size()){
                row_nums.push_back(matrix[i][j]);
            }
            if (col_nums.find_first_of(matrix[j][i]) >= col_nums.size()){
                col_nums.push_back(matrix[j][i]);
            }
        }
        if (row_nums.size() < 9){
            return 'N';
        }
        if (col_nums.size() < 9){
            return 'N';
        }
    }
    return 'Y';
}