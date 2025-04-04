#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;



void parseStmt();
enum TokenType {PHONENUM, PATH, MAILDOMAIN, DOMAIN, SCHEME, COLON, AT, DOT, SLASH, INVALID};
string types[] = {"ID", "STRLIT", "LBR", "RBR", "DOT"};

// Structure to store a token with its type and value
struct Token {
    TokenType type;
    string value;

    Token(TokenType type, string value) : type(type), value(value) {}
};

// Scanner (Lexer) function to tokenize the input string
vector<Token> scanner(const string& input) {
    vector<Token> tokens;
    int pos = 0;
    int length = input.length();

    while (pos < length) {

        // Recognize COLON
        if (input[pos] == ':') {
            tokens.push_back(Token(COLON, ":"));
            pos++;
            continue;
        }

        // Recognize AT
        if (input[pos] == '@') {
            tokens.push_back(Token(AT, "@"));
            pos++;
            continue;
        }

        // Recognize DOT
        if (input[pos] == '.') {
            tokens.push_back(Token(DOT, "."));
            pos++;
            continue;
        }

        // Recognize SLASH
        if (input[pos] == '/') {
            tokens.push_back(Token(SLASH, "/"));
            pos++;
            continue;
        }

        if (isalnum(input[pos])) {
            if (pos + 7 >= length) {
                if (input.substr(pos, 7) == "outlook") {
                    tokens.push_back(Token(MAILDOMAIN, "outlook"));
                    pos += 7;
                    continue;
                }
            }
            if (pos + 6 >= length) {
                if (input.substr(pos, 6) == "iCloud") {
                    tokens.push_back(Token(MAILDOMAIN, "iCloud"));
                    pos += 6;
                    continue;
                } else if (input.substr(pos, 6) == "mailto") {
                    tokens.push_back(Token(SCHEME, "mailto"));
                    pos += 6;
                    continue;
                }
            }
            if (pos + 5 >= length) {
                if (input.substr(pos, 5) == "gmail") {
                    tokens.push_back(Token(MAILDOMAIN, "gmail"));
                    pos += 5;
                    continue;
                } else if (input.substr(pos, 5) == "yahoo") {
                    tokens.push_back(Token(MAILDOMAIN, "yahoo"));
                    pos += 5;
                    continue;
                } else if (input.substr(pos,5) == "https") {
                    tokens.push_back(Token(SCHEME, "https"));
                    pos += 5;
                    continue;
                }
            }
            if (pos + 3 >= length) {
                if (input.substr(pos, 3) == "org") {
                    tokens.push_back(Token(DOMAIN, "org"));
                    pos += 3;
                    continue;
                } else if (input.substr(pos, 3) == "com") {
                    tokens.push_back(Token(DOMAIN, "com"));
                    pos += 3;
                    continue;
                } else if (input.substr(pos, 3) == "tel") {
                    tokens.push_back(Token(SCHEME, "tel"));
                    pos += 3;
                    continue;
                }

            }

            // Recognize PHONENUM
            if (input.substr(pos, 2) == "09") {
                string result;
                if (pos + 10 >= length) {
                    bool valid = true;
                    for (int i = 0; i < 10; i++) {
                        if (isdigit(input[i])) {
                            result += input[i];
                        } else {
                            valid = false;
                        }
                        pos++;
                    }
                    if (valid) {
                        tokens.push_back(Token(PHONENUM, result));
                    }
                }
            }

        }

        // Invalid token (unrecognized character)
        tokens.push_back(Token(INVALID, string(1, input[pos])));
        pos++;
    }
    return tokens;
}

// Global variables for storing tokens and current token position
vector<Token> tokens;
int currentPos = 0;

// Function to get the current token
Token currentToken() {
    if (currentPos < tokens.size()) {
        return tokens[currentPos];
    }
    return Token(INVALID, "");  // Return END token if out of bounds
}

// Function to move to the next token
void advanceToken() {
    if (currentPos < tokens.size()) {
        currentPos++;
    }
}

// Function to match the expected token type and advance
void match(TokenType expectedType) {
    if (currentToken().type == expectedType) {
        advanceToken();
    } else {
        cout << "invalid input" << endl;
        exit(1);  // Exit on syntax error
    }
}

// Recursive function for parsing "primary_tail" (productions 8-10)
void parsePrimaryTail() {
    if (currentToken().type == DOT) {
        match(DOT);
        match(ID);
        parsePrimaryTail();
    } else if (currentToken().type == LBR) {
        match(LBR);
        parseStmt();
        match(RBR);
        parsePrimaryTail();
    }
    // ε (lambda) is automatically handled as we do nothing when there is no match
}

// Recursive function for parsing "primary" (production 7)
void parsePrimary() {
    if (currentToken().type == ID) {
        match(ID);
        parsePrimaryTail();
    } else {
        cout << "invalid input" << endl;
        exit(1);
    }
}

// Recursive function for parsing "stmt" (productions 4-6)
void parseStmt() {
    if (currentToken().type == ID) {
        parsePrimary();
    } else if (currentToken().type == STRLIT) {
        match(STRLIT);
    }
    // ε (lambda) is automatically handled by not doing anything if no stmt is found
}

// Recursive function for parsing "stmts" (productions 2-3)
void parseStmts() {
    if (currentToken().type == ID || currentToken().type == STRLIT) {
        parseStmt();
        parseStmts();
    }
    // ε (lambda) is automatically handled by not doing anything if no stmts are found
}

// Recursive function for parsing "program" (production 1)
void parseProgram() {
    parseStmts();
}

// Main function to drive the parser
int main() {
    // Input string
    string input;
    while (true){
        if (!getline(cin, input)) {
            break;
        } else {
            // Step 1: Scan the input and get the list of tokens
            tokens = scanner(input);

            // printTokens(tokens);
            bool inv = false;
            string outputString = "";
            for (Token token : tokens) {
                if (token.type == INVALID) {
                    cout << "invalid input" << endl;
                    inv = true;
                    break;
                } else {
                    outputString += types[token.type] + " " + token.value + "\n";
                }
            }
            if (!inv) {
                cout << outputString;  // Print the parsed tokens            
            }
            //if (inv) break;

            // Step 2: Start parsing the token list using recursive descent
            currentPos = 0;  // Reset token position
            parseProgram();  // Begin parsing from the root non-terminal 'program'

            // Check if all tokens were consumed (should end with END token)
            if (!tokens.empty()) {
                // cout << "invalid input2" << endl;
            }
        }
    }


    return 0;
}
