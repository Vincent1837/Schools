#include <bits/stdc++.h>
using namespace std;
map<char, vector<string>> mp;
map<char, set<char>> ans;

set<char> first(char A) {
    if (!ans[A].empty()) return ans[A];

    bool isEmpty = false;
    set<char> ret;
    
    for (auto s : mp[A]) {
        bool tmpemp = true;
        for (auto c : s) {
            if (!isupper(c)) {
                ret.insert(c);
                if (c != ';') tmpemp = false;
                break;
            } else {
                auto tmp = first(c);
                ret.insert(tmp.begin(), tmp.end());
                if (tmp.find(';') == tmp.end()) {
                    tmpemp = false;
                    break;
                }
            }
        }
        isEmpty |= tmpemp;
    }
    if (!isEmpty and ret.find(';') != ret.end()) ret.erase(';');
    return ret;
}

int main() {
    string string;
    while (getline(cin, string) and string != "END_OF_GRAMMAR") {
        char A = string[0];
        stringstream ss(string.substr(2));
        while (getline(ss, string, '|')) mp[A].push_back(string);
    }
    for (auto tmp : mp)
        if (ans[tmp.first].empty())
            ans[tmp.first] = first(tmp.first);

    for (auto tmp : ans) {
        cout << tmp.first << " ";
        for (auto c : tmp.second) cout << c;
        cout << "\n";
    }

    cout << "END_OF_FIRST\n";
}