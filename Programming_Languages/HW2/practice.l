%{
#include <stdio.h>
%}

%option noyywrap
%%
[A-Z]+,\s[A-Z][a-z]+-[A-Z][a-z]+ {printf("\n%s\n", yytext);}
[A-Z][0-9]{9} {printf("identity number: %s\n", yytext);}
[0-9]+@[a-z]+(.[a-z]+)+ {printf("email: %s\n", yytext);}
[0-9]{4}\/[0-9]{2}\/[0-9]{2} {printf("birthday: %s\n", yytext);}
\+886[0-9]{9} {printf("phone: %s\n", yytext);}
%%

int main() {
    yylex();
    return 0;
}