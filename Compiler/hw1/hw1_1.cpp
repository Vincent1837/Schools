#include <iostream>
#include <string>
#include <cctype>
using namespace std;

enum TokenType { ID, STRLIT, LBR, RBR, DOT, INVALID, END };

struct Token {
    TokenType type;
    string value;
};

string input;
int pos = 0;

// Function to get the next character in the input
char peek() {
    if (pos < input.length())  // Check boundary
        return input[pos];
    return '\0';  // Return null character at the end of string
}

// Function to consume the next character in the input
char advance() {
    if (pos < input.length())  // Check boundary before incrementing
        return input[pos++];
    return '\0';  // Safeguard to avoid going beyond string bounds
}

// Function to skip whitespace
void skipWhitespace() {
    while (isspace(peek())) {
        advance();
    }
}

// Function to recognize identifiers (ID)
Token getID() {
    string result;
    if (isalpha(peek()) || peek() == '_') {
        result += advance();
        while (isalnum(peek()) || peek() == '_') {
            result += advance();
        }
        return { ID, result };
    }
    return { INVALID, "" };
}

// Function to recognize string literals (STRLIT)
Token getSTRLIT() {
    string result;
    if (peek() == '"') {
        result += advance();  // Consume opening quote
        while (peek() != '"' && peek() != '\0') {  // Protect against out-of-bounds
            result += advance();
        }
        if (peek() == '"') {
            result += advance();  // Consume closing quote
            return { STRLIT, result };
        }
    }
    return { INVALID, "" };
}

// Function to get the next token from input
Token getNextToken() {
    skipWhitespace();  // Skip whitespace before parsing tokens

    if (peek() == '\0') return { END, "" };  // End of input

    if (peek() == '(') {
        advance();
        return { LBR, "(" };
    }
    if (peek() == ')') {
        advance();
        return { RBR, ")" };
    }
    if (peek() == '.') {
        advance();
        return { DOT, "." };
    }
    if (peek() == '"') {
        return getSTRLIT();
    }
    if (isalpha(peek()) || peek() == '_') {
        return getID();
    }
    return { INVALID, "" };
}

// Recursive functions for parsing according to the given grammar
bool primary_tail();
bool stmt();
bool stmts();
bool program();

Token currentToken;

// Function to consume the current token and move to the next one
void advanceToken() {
    currentToken = getNextToken();
}

// Parsing functions
bool primary() {
    if (currentToken.type == ID) {
        advanceToken();
        return primary_tail();
    }
    return false;
}

bool primary_tail() {
    if (currentToken.type == DOT) {
        advanceToken();
        if (currentToken.type == ID) {
            advanceToken();
            return primary_tail();
        }
        return false;  // DOT must be followed by ID
    }
    if (currentToken.type == LBR) {
        advanceToken();
        if (stmt()) {
            if (currentToken.type == RBR) {
                advanceToken();
                return primary_tail();
            }
        }
        return false;  // '(' must be followed by stmt and ')'
    }
    return true;  // epsilon (λ)
}

bool stmt() {
    if (primary()) return true;
    if (currentToken.type == STRLIT) {
        advanceToken();
        return true;
    }
    return true;  // epsilon (λ)
}

bool stmts() {
    if (stmt()) {
        return stmts();  // Recursive stmts production
    }
    return true;  // epsilon (λ)
}

bool program() {
    return stmts();  // Start by parsing stmts
}

// Main function
int main() {
    getline(cin, input);

    if (input.empty()) {
        cout << "invalid input" << endl;
        return 1;
    }

    advanceToken();
    if (program() && currentToken.type == END) {
        pos = 0;  // Reset position for token output
        advanceToken();
        while (currentToken.type != END) {
            switch (currentToken.type) {
            case ID:
                cout << "ID " << currentToken.value << endl;
                break;
            case STRLIT:
                cout << "STRLIT " << currentToken.value << endl;
                break;
            case LBR:
                cout << "LBR " << currentToken.value << endl;
                break;
            case RBR:
                cout << "RBR " << currentToken.value << endl;
                break;
            case DOT:
                cout << "DOT " << currentToken.value << endl;
                break;
            default:
                break;
            }
            advanceToken();
        }
    } else {
        cout << "invalid input" << endl;
    }

    return 0;
}
