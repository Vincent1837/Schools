/*
* Practice 9
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
# include <string>
using namespace std;

int main(){
    int num_of_strings;
    cin >> num_of_strings;
    cin.ignore();
    for (int i = 0; i < num_of_strings; i++){
        string str;
        getline(cin, str);
        char alphabat = str[0];
        int count = 1;
        str.append(" ");
        for (int i = 1; i < str.length(); i++){
            if (str[i] == alphabat){
                count++;
            }
            else {
                cout << alphabat << count;
                alphabat = str[i];
                count = 1;
            }
        }
        cout << '\n';
    }
    return 0;
}