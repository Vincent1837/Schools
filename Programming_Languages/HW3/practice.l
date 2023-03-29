%{
#include "y.tab.h"
%}

%%
[a-zA-Z]+   { yylval.id = strdup(yytext); return ID; }
[0-9]+      { yylval.num = atoi(yytext); return NUM; }
"<"         { return LESS_THAN; }
"="         { return ASSIGN; }
"if"        { return IF; }
"{"         { return LBRACE; }
"}"         { return RBRACE; }
"("         { return LPAREN; }
")"         { return RPAREN; }
"printf"    { return PRINTF; }
\".*\"      { yylval.str = strdup(yytext); return STRING; }
[ \t\n]     { /* ignore whitespace */ }
.           { printf("Invalid character: %c\n", *yytext); }
%%

int yywrap() {
    return 1;
}
