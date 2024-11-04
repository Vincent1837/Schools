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

// bool charinstr(char c, string str);

string tostr(char c) {
    string str;
    str += c;
    return str;
}
bool charinstr(char c, string str) {
    for (char ch : str) {
        if (ch == c) {
            return true;
        }
    }
    return false;
}

// Scanner (Lexer) function to tokenize the input string
vector<Token> scanner(const string& input) {
    vector<Token> tokens;
    int pos = 0;
    int length = input.length();

    while (pos < length) {
        // Skip whitespace
        if (isspace(input[pos])) {
            pos++;
            continue;
        }

        // Recognize NUM
        if (isdigit(input[pos])) {
            string result;
            if (input[pos] == '0') {
                tokens.push_back(Token(NUM, "0"));
                pos++;
                /*if (isalnum(input[++pos])) {
                    while (isalnum(input[pos])) {
                        pos++;
                    }
                    tokens.push_back(Token(INVALID, ""));
                } else {
                    tokens.push_back(Token(NUM, "0"));
                }*/
            } /*else if (isalpha(input[++pos])) {
                while (isalnum(input[pos])) {
                    pos++;
                }
                tokens.push_back(Token(INVALID, ""));
            } */else {
                // pos--;
                while (pos < length && isdigit(input[pos])) {
                    result += input[pos++];
                }
                tokens.push_back(Token(NUM, result));
            }
            continue;
        }

        // Recognize IDENTIFIER
        if (isalpha(input[pos])) {
            string result;

            if (input[pos] == 'i') {
                if (pos+1 < input.length()) {
                    if (input[pos+1] == 'f') {
                        result += input.substr(pos, 2);
                        pos += 2;
                        tokens.push_back(Token(KEYWORD, result));
                        continue;
                    }
                }
            }

            if (input[pos] == 'w') {
                if (pos + 5 < input.length()) {
                    if (input.substr(pos, 5) == "while") {
                        result += input.substr(pos, 5);
                        pos += 5;
                        tokens.push_back(Token(KEYWORD, result));
                        continue;
                    }
                }
            }
            while (pos < length && isalnum(input[pos])) {
                result += input[pos++];
            }
            tokens.push_back(Token(IDENTIFIER, result));
            continue;
        }

        if (input[pos] == '+') {
            tokens.push_back(Token(SYMBOL, "+"));
            pos++;
            continue;
        }

        if (input[pos] == '-') {
            tokens.push_back(Token(SYMBOL, "-"));
            pos++;
            continue;
        }

        if (input[pos] == '*') {
            tokens.push_back(Token(SYMBOL, "*"));
            pos++;
            continue;
        }

        if (input[pos] == '/') {
            tokens.push_back(Token(SYMBOL, "/"));
            pos++;
            continue;
        }

        if (input[pos] == '=') {
            tokens.push_back(Token(SYMBOL, "="));
            pos++;
            continue;
        }

        if (input[pos] == '(') {
            tokens.push_back(Token(SYMBOL, "("));
            pos++;
            continue;
        }

        if (input[pos] == ')') {
            tokens.push_back(Token(SYMBOL, ")"));
            pos++;
            continue;
        }

        if (input[pos] == '{') {
            tokens.push_back(Token(SYMBOL, "{"));
            pos++;
            continue;
        }

        if (input[pos] == '}') {
            tokens.push_back(Token(SYMBOL, "}"));
            pos++;
            continue;
        }

        if (input[pos] == '<') {
            tokens.push_back(Token(SYMBOL, "<"));
            pos++;
            continue;
        }

        if (input[pos] == '>') {
            tokens.push_back(Token(SYMBOL, ">"));
            pos++;
            continue;
        }

        if (input[pos] == ';') {
            tokens.push_back(Token(SYMBOL, ";"));
            pos++;
            continue;
        }

        // Invalid token (unrecognized character)
        tokens.push_back(Token(INVALID, ""));
        pos++;
    }
    return tokens;
}

int main(){
    string line;
    string input_line;
    while (cin >> line) {
        input_line += line;
    }

    vector<Token> tokens = scanner(input_line);

    int invcount = 0;
    for (Token token : tokens) {
        if (token.type == TokenType::INVALID) {
            cout << "Invalid" << endl;
            invcount++;
        } else {
            if (invcount != 0) {
                
                invcount = 0;
            }
            cout << types[token.type] << " " << '\"' << token.value << '\"' << endl;
        }
    }

    return 0;
}
