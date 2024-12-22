%{
#include <stdio.h>
#include <stdlib.h>

#define MAX_STACK 100

void yyerror(const char *s);
int yylex();

int stack[MAX_STACK];
int sp = 0;

void push(int value);
int pop();
%}

%token LOAD ADD SUB MUL MOD INC DEC

%%

program:
    /* 空程序 */
    | program instruction
;

instruction:
    LOAD { push($1); }
    | ADD  { 
        if (sp < 2) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() + pop()); 
    }
    | SUB  { 
        if (sp < 2) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() - pop());
    }
    | MUL  { 
        if (sp < 2) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() * pop()); 
    }
    | MOD  { 
        if (sp < 2) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() % pop());
    }
    | INC  { 
        if (sp < 1) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() + 1); 
    }
    | DEC  { 
        if (sp < 1) {
            printf("Invalid format\n"); 
            exit(1);
        }
        push(pop() - 1); 
    }
;

%%

void yyerror(const char *s) {
    printf("Invalid format\n");
    exit(1);
}

int main() {
    if (yyparse() == 0) {
        if (sp == 1) {
            printf("%d\n", stack[0]);
        } else {
            printf("Invalid format\n");
        }
    }
    return 0;
}

void push(int value) {
    if (sp >= MAX_STACK) {
        printf("Invalid format\n");
        exit(1);
    }
    stack[sp++] = value;
}

int pop() {
    if (sp <= 0) {
        printf("Invalid format\n");
        exit(1);
    }
    return stack[--sp];
}
