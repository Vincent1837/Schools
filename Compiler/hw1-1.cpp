#include <iostream>
#include <regex>
#include <string>
#include <vector>

using namespace std;

// 定義正則表達式對應的 token 規則
regex id_regex("[A-Za-z_][A-Za-z0-9_]*");
regex strlit_regex("\"[^\"]*\"");
regex dot_regex("\\.");
regex lbr_regex("\\(");
regex rbr_regex("\\)");

// Token 及其類型結構
struct Token {
    string type;
    string value;
};

// 匹配並暫存 token 的函數
bool matchTokens(const string &input, vector<Token> &tokens) {
    smatch match;
    string s = input;

    while (!s.empty()) {
        // 忽略前導空白
        if (s[0] == ' ') {
            s = s.substr(1);
            continue;
        }

        // 嘗試匹配各種 token 類型
        if (regex_search(s, match, strlit_regex) && match.position() == 0) {
            tokens.push_back({"STRLIT", match.str()}); // 暫存 STRLIT
            s = s.substr(match.length());
        } else if (regex_search(s, match, id_regex) && match.position() == 0) {
            tokens.push_back({"ID", match.str()}); // 暫存 ID
            s = s.substr(match.length());
        } else if (regex_search(s, match, dot_regex) && match.position() == 0) {
            tokens.push_back({"DOT", match.str()}); // 暫存 DOT
            s = s.substr(match.length());
        } else if (regex_search(s, match, lbr_regex) && match.position() == 0) {
            tokens.push_back({"LBR", match.str()}); // 暫存 LBR
            s = s.substr(match.length());
        } else if (regex_search(s, match, rbr_regex) && match.position() == 0) {
            tokens.push_back({"RBR", match.str()}); // 暫存 RBR
            s = s.substr(match.length());
        } else {
            // 如果沒有匹配到任何 token，則為無效輸入
            return false;
        }
    }

    return true;
}

int main() {
    string input;

    // 從標準輸入讀取輸入
    while (getline(cin, input)) {
        vector<Token> tokens; // 暫存匹配的 token

        if (matchTokens(input, tokens)) {
            // 如果所有 token 匹配成功，才進行輸出
            for (const auto &token : tokens) {
                cout << token.type << " " << token.value << endl;
            }
        } else {
            cout << "invalid input" << endl; // 無效輸入，直接輸出 invalid input
        }
    }

    return 0;
}