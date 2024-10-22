#include <iostream>
#include <string>

using namespace std;
bool program();
bool stmts();
bool stmt();
bool primary();
bool primary_tail();

bool program() {
    return stmts();
}

bool stmts() {
    return 
}

int main () {
    string input;
    while (getline(cin, input)) {
        cout << "hello, " << input << endl;
    }
    return 0;
}