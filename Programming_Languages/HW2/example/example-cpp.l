%{
#include <iostream>
using namespace std;

void printHello();
%}
%option noyywrap

%%

.   {}
\n  { printHello(); }
%%

void printHello() {
    cout << "hello" << endl;
}

int main() {
    yylex();
    return 0;
}