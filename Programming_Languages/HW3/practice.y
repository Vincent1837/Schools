%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define YYSTYPE union YYSTYPE

#include "lex.yy.h"

void yyerror(const char *s);

int a, b;

%}

%union {
    int num;
    char *id;
    char *str;
}

%token <num> NUM
%token <id> ID
%token LESS_THAN
%token ASSIGN
%token IF
%token LBRACE
%token RBRACE
%token LPAREN
%token RPAREN
%token PRINTF
%token <str> STRING

%left '+' '-'
%left '*' '/'

%%

stmt_list:
    stmt
    | stmt_list stmt
    ;

stmt:
    expr_stmt
    | selection_stmt
    ;

expr_stmt:
    ID ASSIGN NUM ';'    { a = $3; }
    | PRINTF '(' STRING ')' ';' { printf("%s\n", $3); }
    ;

selection_stmt:
    IF '(' ID LESS_THAN ID ')' LBRACE PRINTF '(' STRING ')' ';' RBRACE
        { if (a < b) printf("a is win\n"); }
    ;

%%

void yyerror(const char *s) {
    printf("%s\n", s);
}

int main() {
    yyparse();
    return 0;
}
