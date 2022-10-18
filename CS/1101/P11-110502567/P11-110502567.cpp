/*
* Practice 11
* Name: 蔡淵丞
* Student Number: 110502567
* Course 2021-CE1003-B
*/
# include <iostream>
# include <set>
using namespace std;

int main(){
    while(true){
        int size;
        cin >> size;
        if (size == -1){
            break;
        }
        char input[100];
        set<char> set;
        for (int i = 0; i < size; i++){
            cin >> input[i];
            set.insert(input[i]);
        }
        // cout the set
        for (char c:set){
            cout << c << " ";
        }
        cout << '\n';
        // cin the char to search
        char search;
        cin >> search;
        if (set.count(search)){
            // iteration
            int index = 0;
            for (char c:set){
                if (c == search){
                    break;
                }
                index++;
            }
            cout << index << '\n';
        }
        else cout << "-1\n";
        cout << '\n';
    }
    return 0;
}