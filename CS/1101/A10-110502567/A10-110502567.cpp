/*
* Assignment 10
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
# include <vector>
using namespace std;

int main (){
    vector<int> stack;
    while (true){
        string get;
        cin >> get;
        if (get == "push"){
            char get_element;
            cin >> get_element;
            stack.push_back(int(get_element));
        }
        else if (get == "pop"){
            if (stack.empty()){
                cout << "empty\n";
            }
            else{
                cout << char(stack.back()) << "\n";
                stack.pop_back();
            }
        }
        else if (get == "list"){
            for (int i = 0; i < stack.size(); i++){
                cout << char(stack[i]) << " ";
            }
            cout << "\n";
        }
        else{
            break;
        }
    }
    return 0;
}