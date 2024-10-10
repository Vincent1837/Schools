#include <iostream>
#include <string>
#include <regex>
#include <vector>

using namespace std;

// Token types
enum TokenType {
    TOKEN_ID,
    TOKEN_STRLIT,
    TOKEN_LBR,
    TOKEN_RBR,
    TOKEN_DOT,
    TOKEN_INVALID,
    TOKEN_END
};

// Token structure
struct Token {
    TokenType type;
    string value;
};

// Global variables for tokens and current token index
vector<Token> tokens;
size_t current_token_index = 0;

// Function prototypes
void getNextToken();
void program();
void stmts();
void stmt();
void primary();
void primary_tail();
void error(const string& message);

// Helper functions to determine token type
TokenType getTokenType(const string& token_str) {
    if (regex_match(token_str, regex("[A-Za-z_][A-Za-z0-9_]*"))) {
        return TOKEN_ID;
    }
    if (regex_match(token_str, regex("\"[^\"]*\""))) {
        return TOKEN_STRLIT;
    }
    if (token_str == "(") {
        return TOKEN_LBR;
    }
    if (token_str == ")") {
        return TOKEN_RBR;
    }
    if (token_str == ".") {
        return TOKEN_DOT;
    }
    return TOKEN_INVALID;
}

// Lexer using regex for tokenization
vector<Token> tokenize(const string& input) {
    vector<Token> result;
    regex token_regex(R"((\"[^\"]*\"|[A-Za-z_][A-Za-z0-9_]*|\(|\)|\.))");
    auto words_begin = sregex_iterator(input.begin(), input.end(), token_regex);
    auto words_end = sregex_iterator();

    for (auto it = words_begin; it != words_end; ++it) {
        string token_str = it->str();
        TokenType type = getTokenType(token_str);
        if (type == TOKEN_INVALID) {
            result.push_back({TOKEN_INVALID, token_str});
            break; // No need to continue if an invalid token is found
        }
        result.push_back({type, token_str});
    }
    return result;
}

// Recursive descent parsing functions

// program → stmts
void program() {
    stmts();
}

// stmts → stmt stmts | λ
void stmts() {
    if (tokens[current_token_index].type == TOKEN_ID || tokens[current_token_index].type == TOKEN_STRLIT) {
        stmt();
        stmts();
    }
}

// stmt → primary | STRLIT | λ
void stmt() {
    if (tokens[current_token_index].type == TOKEN_ID) {
        primary();
    } else if (tokens[current_token_index].type == TOKEN_STRLIT) {
        cout << "STRLIT " << tokens[current_token_index].value << endl;
        getNextToken();
    }
}

// primary → ID primary_tail
void primary() {
    if (tokens[current_token_index].type == TOKEN_ID) {
        cout << "ID " << tokens[current_token_index].value << endl;
        getNextToken();
        primary_tail();
    }
}

// primary_tail → DOT ID primary_tail | LBR stmt RBR primary_tail | λ
void primary_tail() {
    if (tokens[current_token_index].type == TOKEN_DOT) {
        cout << "DOT ." << endl;
        getNextToken();
        if (tokens[current_token_index].type == TOKEN_ID) {
            cout << "ID " << tokens[current_token_index].value << endl;
            getNextToken();
            primary_tail();
        } else {
            error("Expected ID after DOT");
        }
    } else if (tokens[current_token_index].type == TOKEN_LBR) {
        cout << "LBR (" << endl;
        getNextToken();
        stmt();
        if (tokens[current_token_index].type == TOKEN_RBR) {
            cout << "RBR )" << endl;
            getNextToken();
            primary_tail();
        } else {
            error("Expected RBR after stmt");
        }
    }
}

// Function to move to the next token
void getNextToken() {
    if (current_token_index < tokens.size() - 1) {
        current_token_index++;
    } else {
        tokens.push_back({TOKEN_END, ""});
    }
}

// Error handling function
void error(const string& message) {
    cout << "invalid input" << endl;
    exit(1);
}

// Main function
int main() {
    string line;

    // Process multiple lines of input
    while (getline(cin, line)) {
        tokens = tokenize(line);
        if (tokens.empty() || tokens[0].type == TOKEN_INVALID) {
            cout << "invalid input" << endl;
            continue;
        }

        // Initialize and start parsing
        current_token_index = 0;
        getNextToken();
        program();

        // Check if all tokens were consumed
        if (tokens[current_token_index].type != TOKEN_END) {
            error("Unexpected token after valid input");
        }
    }

    return 0;
}
