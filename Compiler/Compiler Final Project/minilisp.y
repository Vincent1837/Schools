%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Symbol table for variable definitions
typedef struct {
    char *name;
    int value;
} Symbol;

#define MAX_SYMBOLS 100
Symbol symbol_table[MAX_SYMBOLS];
int symbol_count = 0;

int lookup_symbol(char *name);
void define_symbol(char *name, int value);

%}

// Tokens
%token LPAREN RPAREN PRINT_NUM PRINT_BOOL DEFINE FUN IF AND OR NOT MOD
%token GREATER SMALLER EQUAL PLUS MINUS MULTIPLY DIVIDE TRUE FALSE NUMBER ID

// Precedence
%right IF
%left OR AND
%left EQUAL GREATER SMALLER
%left PLUS MINUS
%left MULTIPLY DIVIDE MOD

// Data Types for yacc
%union {
    int num;        // For numbers
    char *id;       // For identifiers
}

// Grammar Rules and Actions
%%
program:
    stmt_list
    ;

stmt_list:
    stmt
    | stmt_list stmt
    ;

stmt:
    exp
    | def_stmt
    | print_stmt
    ;

print_stmt:
    LPAREN PRINT_NUM exp RPAREN { printf("%d\n", $3); }
    | LPAREN PRINT_BOOL exp RPAREN { printf("%s\n", $3 ? "#t" : "#f"); }
    ;

exp:
    NUMBER                { $$ = $1; }
    | TRUE                { $$ = 1; }
    | FALSE               { $$ = 0; }
    | ID                  { $$ = lookup_symbol($1); }
    | num_op
    | logical_op
    | if_exp
    ;

num_op:
    LPAREN PLUS exp_list RPAREN {
        $$ = 0;
        for (int i = 0; i < $3.count; ++i) $$ += $3.values[i];
    }
    | LPAREN MINUS exp exp RPAREN { $$ = $3 - $4; }
    | LPAREN MULTIPLY exp_list RPAREN {
        $$ = 1;
        for (int i = 0; i < $3.count; ++i) $$ *= $3.values[i];
    }
    | LPAREN DIVIDE exp exp RPAREN { $$ = $3 / $4; }
    ;

logical_op:
    LPAREN AND exp_list RPAREN { $$ = 1; for (int i = 0; i < $3.count; ++i) $$ = $$ && $3.values[i]; }
    | LPAREN OR exp_list RPAREN { $$ = 0; for (int i = 0; i < $3.count; ++i) $$ = $$ || $3.values[i]; }
    | LPAREN NOT exp RPAREN { $$ = !$3; }
    ;

if_exp:
    LPAREN IF exp exp exp RPAREN { $$ = $3 ? $4 : $5; }
    ;

def_stmt:
    LPAREN DEFINE ID exp RPAREN { define_symbol($3, $4); }
    ;
%%
int lookup_symbol(char *name) {
    for (int i = 0; i < symbol_count; ++i) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            return symbol_table[i].value;
        }
    }
    printf("Error: Undefined variable '%s'\n", name);
    exit(1);
}

void define_symbol(char *name, int value) {
    for (int i = 0; i < symbol_count; ++i) {
        if (strcmp(symbol_table[i].name, name) == 0) {
            symbol_table[i].value = value;
            return;
        }
    }
    symbol_table[symbol_count].name = strdup(name);
    symbol_table[symbol_count].value = value;
    ++symbol_count;
}
