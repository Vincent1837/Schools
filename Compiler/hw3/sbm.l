%{
    #include "sbm.tab.h"
%}

%%

load[ \t]+[0-9]+ { 
    yylval = atoi(yytext + 5);
    return LOAD;
}
add       { return ADD; }
sub       { return SUB; }
mul       { return MUL; }
mod       { return MOD; }
inc       { return INC; }
dec       { return DEC; }
[ \t\n]+  { /* 忽略空白字符 */ }
.         { return yytext[0]; }

%%
