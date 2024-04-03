%{
#include <stdio.h>
#include <stdlib.h>

int yylex();
void yyerror(const char *s);

int stack[1000];
int top = -1;

void push(int value) {
    if (top < 999) {
        stack[++top] = value;
    } else {
        printf("invalid Format\n");
        exit(EXIT_FAILURE);
    }
}

int pop() {
    if (top >= 0) {
        return stack[top--];
    } else {
        printf("invalid Format\n");
        exit(EXIT_FAILURE);
    }
}
%}

%token NUMBER
%token ADD SUB MUL MOD INC DEC LOAD

%%

program: /* empty */
       | program statement '\n' { /* Do something with the result */ }

statement: expr { /* Do something with the result */ }

expr: ADD expr expr { push(pop() + pop()); }
    | SUB expr expr { push(-pop() + pop()); }
    | MUL expr expr { push(pop() * pop()); }
    | MOD expr expr { int b = pop(); int a = pop(); push(a % b); }
    | INC expr      { push(pop() + 1); }
    | DEC expr      { push(pop() - 1); }
    | LOAD NUMBER   { push($2); }
    ;

%%

int main() {
    yyparse();
    if (top == 0) {
        printf("Result: %d\n", pop());
        return 0;
    } else {
        printf("invalid Format\n");
        exit(EXIT_FAILURE);
    }
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

int yylex() {
    int c = getchar();
    if (c == '\n' || c == EOF) {
        return 0;
    } else if (c == '+') {
        return ADD;
    } else if (c == '-') {
        return SUB;
    } else if (c == '*') {
        return MUL;
    } else if (c == '%') {
        return MOD;
    } else if (c == 'i') {
        return INC;
    } else if (c == 'd') {
        return DEC;
    } else if (c == 'l') {
        // Handle "load" instruction
        int value;
        scanf("%d", &value);
        yylval = value;
        return LOAD;
    } else if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    } else {
        return c;
    }
}
