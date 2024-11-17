%{
#include <stdio.h>
%}

%%

\"([^\"\n]|\'[^\']*\'|[^\"])*\"$ { 
    printf("Valid: %s\n", yytext); 
}  // Valid double-quoted string with properly nested single quotes

\'([^\'\n]|\"[^\"]*\"|[^\'])*\'$ { 
    printf("Valid: %s\n", yytext); 
}  // Valid single-quoted string with properly nested double quotes

\"([^\"\n]*\'[^\']*)[^\"]*       { 
    printf("Invalid: %s (unclosed single quote inside double-quoted string)\n", yytext); 
}  // Double-quoted string with unclosed single quote

\'([^\'\n]*\"[^\"]*)[^\']*       { 
    printf("Invalid: %s (unclosed double quote inside single-quoted string)\n", yytext); 
}  // Single-quoted string with unclosed double quote

\"([^\"\n]*)                    { 
    printf("Invalid: %s (unclosed double quotes)\n", yytext); 
}  // Unclosed double-quoted string

\'([^\'\n]*)                    { 
    printf("Invalid: %s (unclosed single quotes)\n", yytext); 
}  // Unclosed single-quoted string

.*                              { 
    printf("Invalid: %s\n", yytext); 
}  // Catch-all invalid rule

%%

int main() {
    yylex();
    return 0;
}

int yywrap(){
    return 1;
}
