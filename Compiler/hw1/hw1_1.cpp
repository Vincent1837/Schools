#include <iostream>
#include <vector>
#include <string>
#include <cctype>
using namespace std;



void parseStmt();
enum TokenType { ID, STRLIT, LBR, RBR, DOT, INVALID };
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
        // Skip whitespace
        if (isspace(input[pos])) {
            pos++;
            continue;
        }

        // Recognize string literals (STRLIT)
        if (input[pos] == '"') {
            string result;
            result += input[pos++];  // Add the opening quote
            while (pos < length && input[pos] != '"') {
                result += input[pos++];
            }
            if (pos < length && input[pos] == '"') {
                result += input[pos++];  // Add the closing quote
                tokens.push_back(Token(STRLIT, result));
            } else {
                tokens.push_back(Token(INVALID, result));  // Unterminated string literal
            }
            continue;
        }

        // Recognize identifiers (IDs)
        if (isalpha(input[pos]) || input[pos] == '_') {
            string result;
            while (pos < length && (isalnum(input[pos]) || input[pos] == '_')) {
                result += input[pos++];
            }
            tokens.push_back(Token(ID, result));
            continue;
        }

        // Recognize left parenthesis '('
        if (input[pos] == '(') {
            tokens.push_back(Token(LBR, "("));
            pos++;
            continue;
        }

        // Recognize right parenthesis ')'
        if (input[pos] == ')') {
            tokens.push_back(Token(RBR, ")"));
            pos++;
            continue;
        }

        // Recognize dot '.'
        if (input[pos] == '.') {
            tokens.push_back(Token(DOT, "."));
            pos++;
            continue;
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
