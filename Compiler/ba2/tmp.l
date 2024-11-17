%{
#include <stdio.h>
%}

%%

[0-9]*\.[0-9]+                  {printf("%s FLOAT", yytext); }
[0-9]+                          {printf("%s INTEGER", yytext);}
"true"                          {printf("%s BOOLEAN", yytext);}
"false"                         {printf("%s BOOLEAN", yytext); }
\"[^\n"]*\"                     {printf("%s STRING", yytext); }
\'[^\n']*\'                     {printf("%s STRING", yytext); }
[0-9]+([+|*|/|"\-"]+[0-9]*)+    {printf("%s OPERATION", yytext); }
\n                              {printf("\n");}
.*                              {printf("%s INVALID", yytext); }

%%
int main(){
    yylex();
    return(0);
}

int yywrap() {
    return 1;
}