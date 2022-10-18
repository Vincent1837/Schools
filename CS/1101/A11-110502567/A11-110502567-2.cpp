/*
* Assignment 11
* Name: 蔡淵丞
* Student Number: 11052567
* Course: 2021-CE1003-B
*/
# include <iostream>
# include <string>
using namespace std;
using namespace std::string_literals;

int main(){
    while (true){
        int len_palindrome;
        string str;
        string palindromes = "";
        cin >> str;
        if (str == "-1"){
            break;
        }
        // 遍歷一次找...a...型迴文
        for (int i = 0; i < str.size(); i++){
            int left = i-1;
            int right = i+1;
            // 對每一個字元向左右延伸並判斷是否相等
            while (left >= 0 and right <= str.size()){
                if (str[left] != str[right]){
                    break;
                }
                left--;
                right++;
            }
            // 判斷是否為所要的迴文
            if (str.substr(left+1, right-left-1).size() > 1 and str.substr(left+1, right-left-1).size() > palindromes.size()){
                palindromes.assign(str, left+1, right-left-1);
            }
        }
        // 再遍歷一次找...aa...型迴文
        for (int i = 0; i < str.size()-1; i++){
            int left = i-1;
            int j = i+1;
            int right = j+1;
            if (str[i] == str[j]){
                // 若找到aa則向左右延伸
                while (left >= 0 and right <= str.size()){
                    if (str[left] != str[right]){
                        break;
                    }
                    left--;
                    right++;
                }
                // 判斷是否為所要的迴文
                if (str.substr(left+1, right-left-1).size() > 1 and str.substr(left+1, right-left-1).size() > palindromes.size()){
                    palindromes.assign(str, left+1, right-left-1);
                }
            }
        }
        if (palindromes == ""){
            cout << "Palindrome not existed!\n";
        }
        else{
            cout << "Palindrome:" << palindromes << '\n';
            cout << "Length:" << palindromes.size() << '\n';
        }
        cout << '\n';
    }
    return 0;
}