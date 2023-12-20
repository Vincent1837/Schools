%{
#include <stdio.h>
#include <stdlib.h>

int stack[1000]; // Stack to store operands
int top = -1;    // Top of the stack

void push(int value) {
    if (top < 999) {
        stack[++top] = value;
    } else {
        fprintf(stderr, "Error: Stack overflow\n");
        exit(EXIT_FAILURE);
    }
}

int pop() {
    if (top >= 0) {
        return stack[top--];
    } else {
        fprintf(stderr, "Error: Stack underflow\n");
        exit(EXIT_FAILURE);
    }
}

%}

%token NUMBER
%token ADD SUB MUL MOD INC DEC LOAD

%%

program: /* empty */
       | program statement '\n' { printf("Result: %d\n", $2); }

statement: expr { $$ = $1; }

expr: ADD expr expr { $$ = pop() + pop(); push($$); }
    | SUB expr expr { $$ = pop() - pop(); push($$); }
    | MUL expr expr { $$ = pop() * pop(); push($$); }
    | MOD expr expr { $$ = pop() % pop(); push($$); }
    | INC expr      { $$ = pop() + 1; push($$); }
    | DEC expr      { $$ = pop() - 1; push($$); }
    | LOAD NUMBER   { push($2); $$ = $2; }
    | NUMBER        { push($1); $$ = $1; }

%%

int main() {
    yyparse();
    return 0;
}

int yyerror(const char *s) {
    fprintf(stderr, "Error: %s\n", s);
    return 0;
}

int yylex() {
    int c = getchar();
    if (c == '\n' || c == EOF) {
        return 0;
    } else if (c >= '0' && c <= '9') {
        ungetc(c, stdin);
        scanf("%d", &yylval);
        return NUMBER;
    } else {
        return c;
    }
}
