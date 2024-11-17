%{
#include <stdio.h>
#include <string.h>
%}

%%
"#".*                         { printf("//%s\n", yytext+1); }
"\"\"\"(.*|\n)*\"\"\"" { printf("/*%s*/\n", yytext+3); }
"print"\\(\"([^\"]|[^\"])*\"\\) { 
                                    printf("cout << %s << endl;\n", yytext+6); 
                                }
"if"\\s(True|False):          { printf("if(%s) {\n", strcmp(yytext+3,"True")==0 ? "true" : "false"); }
\n                             { printf("\n"); }
.                              { ECHO; }
%%
int main() {
    yylex();
    return 0;
}

int yywrap() { return 1;}
