#include <iostream>
#include <string>
#include <vector>

using namespace std;

enum TokenType {NUM, IDENTIFIER, SYMBOL, KEYWORD, INVALID};
string types[] = {"NUM", "IDENTIFIER", "SYMBOL", "KEYWORD", "Invalid"};

// Structure to store a token with its type and value
struct Token {
    TokenType type;
    string value;

    Token(TokenType type, string value) : type(type), value(value) {}
};

vector<Token> test(string input) {
    vector<Token> tokens;
    int pos = 0;
    int length = input.length();

    // Recognize NUM
        if (isdigit(input[pos])) {
            string result;
            if (input[pos] == '0') {
                if (isdigit(input[++pos])) {
                    tokens.push_back(Token(INVALID, ""));
                } else {
                    tokens.push_back(Token(NUM, "0"));
                }
            } else {
                while (pos < length && isdigit(input[pos])) {
                    result += input[pos++];
                }
                tokens.push_back(Token(NUM, result));
            }
        }

        if (input[pos] == 'w') {
                if (pos + 5 < input.length()) {
                    cout << input.substr(pos, 5) << endl;
                    if (input.substr(pos, 5) == "hile") {
                        string result;
                        result += input.substr(pos, 5);
                        pos += 5;
                        tokens.push_back(Token(KEYWORD, result));
                    }
                }
            }
    return tokens;
}   

int main() {
    string input = "whiletrue";
    vector<Token> tokens;

     tokens = test(input);

    for (Token token : tokens) {
        cout << types[token.type] << ": " << token.value << endl;
    }
    return 0;

}