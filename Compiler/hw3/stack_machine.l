%option noyywrap

%%
[0-9]+    { yylval = atoi(yytext); return NUMBER; }
.        { return yytext[0]; }
%%

int yywrap() {
    return 1;
}
