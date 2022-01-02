/*
* Assignment 14
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/

# include <iostream>
# include <string>
# include <cmath>
using namespace std;

int convert62(char);
int func(string, int);
string input_string;

int convert62(char c){
    if ((int)c >= 48 && (int)c < 58){
        return (int)c - 48;
    }
    else if ((int)c >= 65 && (int)c < 91){
        return (int)c - 55;
    }
    else return (int)c - 61;
}

int func(string str, int idx){
    int decnum = 0;
    for (int i = 0; i < str.size(); i++){
        decnum += pow(idx, i) * convert62(input_string[i]);
    }
    return decnum;
}

int main(){
    while (true){
        cin >> input_string;

        if (input_string == "-1"){
            break;
        }

        char max_char = '1';
        for (char c : input_string){
            if (c > max_char){
                max_char = c;
            }
        }

        bool flg = true;
        for(int i = convert62(max_char)+1; i < 63; i++){
            if (func(input_string, i) % (i-1) == 0){
                cout << i << '\n';
                flg = false;
                break;
            }
        }
        if (flg){
            cout << "such number is impossible!\n"; 
        }
    }
    return 0;
}