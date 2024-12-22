%option noyywrap

%{
    #include "stack_machine.tab.h"
    extern int yylval;
%}

%%

add     { return ADD; }
sub     { return SUB; }
mul     { return MUL; }
mod     { return MOD; }
inc     { return INC; }
dec     { return DEC; }
load[ \t]+[0-9]+    { 
    yylval = atoi(yytext + 5);
    return LOAD;
}
[ \t\n] { /* Ignore blank spaces */ }
.       { return yytext[0]; }

%%