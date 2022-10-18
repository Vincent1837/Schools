/*
* Practice 13
* Name: 蔡淵丞
* Student Number: 110502567
* Course 2021-CE1003-B
*/
# include <iostream>
# include <fstream>
using namespace std;

string judge(string);

int main(){
    string files[3] = {"ox1.txt", "ox2.txt", "ox3.txt"};
    for (string fileName : files){
        ifstream inFile(fileName, ios::in);
        if (!inFile){
            cout << "file could not be opened!\n";
        }
        else {
            string oxStr, tmp;
            for (int i = 0; i < 3; i++){
                getline(inFile, tmp);
                oxStr += tmp;
            }
            cout << judge(oxStr) << '\n';
        }
    }
    return 0;
}

string judge(string str){
    for (int i = 0; i < 3; i++){
        if (str[i] == str[i+3] and str[i+3] == str[i+6]){
            if (str[i] == 'o') return "Owin\n";
            else return "Xwin\n";
        }
        if (str[3*i] == str[3*i+1] and str[3*i+1] == str[3*i+2]){
            if (str[i] == 'o') return "Owin\n";
            else return "Xwin\n";
        }
    }
    if (str[0] == str[4] and str[4] == str[8]){
        if (str[4] == 'o') return "Owin\n";
            else return "Xwin\n";
    }
    if (str[2] == str[4] and str[4] == str[6]){
        if (str[4] == 'o') return "Owin\n";
            else return "Xwin\n";
    }
    return "tie";
}