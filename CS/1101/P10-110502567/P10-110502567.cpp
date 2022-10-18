/*
* Practice 10
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
using namespace std;

int main(){
    while (1){
        string input_str, reversed_str;
        cin >> input_str;
        for (int i = 0; i < input_str.length(); i++){
            reversed_str = input_str[i] + reversed_str;
        } 
        if (input_str == "-1"){
            break;
        }
        else if (input_str == reversed_str){
            cout << "Palindrome!\n";
        }
        else{
            cout << "Not Palindrome!\n";
        }
    }
    return 0;
}