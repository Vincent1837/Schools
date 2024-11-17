%{
#include <stdio.h>
%}

%%

[0-9]+                    { printf("%s INTEGER\n", yytext); }
[0-9]+\.[0-9]+            { printf("%s FLOAT\n", yytext); }
\"([^\"\n]|[^\n])*\"      { printf("%s STRING\n", yytext); }
\'([^\'\n]|[^\n])*\'      { printf("%s STRING\n", yytext); }
(true|false)              { printf("%s BOOLEAN\n", yytext); }
[0-9]+[+\-*/]+[0-9+\-*/]* { printf("%s OPERATION\n", yytext); }
/[+\-*/].*                { printf("%s INVALID\n", yytext); }
.*                        { printf("%s INVALID\n", yytext); }

%%

int main() {
    yylex();
    return 0;
}
