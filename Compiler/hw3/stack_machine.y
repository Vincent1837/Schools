%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex();
    int yyerror(const char *s);
    int stack[1000];
    int top = -1;

    void push();
    int pop();
%}

%token NUMBER
%token ADD SUB MUL MOD INC DEC LOAD

%%

program     :
            | program expr
            ;

expr: LOAD NUM { push($2); }
    | ADD { if(top < 1) { YYABORT; } else { push(pop() + pop()); } }
    | SUB { if(top < 1) { YYABORT; } else { push(pop() - pop()); } }
    | MUL { if(top < 1) { YYABORT; } else { push(pop() * pop()); } }
    | MOD { if(top < 1) { YYABORT; } else { push(pop() % pop()); } }
    | INC { if(top < 0) { YYABORT; } else {push(pop() + 1);} }
    | DEC { if(top < 0) { YYABORT; } else {push(pop() - 1);} }
    ;

%%

void push(int value) {
    if (top < 999) {
        stack[++top] = value;
    } else {
        yyerror("Invalid Format\n");
        exit(1);
    }
}

int pop() {
    if (top >= 0) {
        return stack[top--];
    } else {
        yyerror("Invalid Format\n");
        exit(1);
    }
}

int main() {
    yyparse();
    if (top == 0) {
        printf("%d\n", pop());
        return 0;
    } else {
        yyerror("Invalid Format\n");
        exit(1);
    }
}

int yyerror(const char *s) {
    fprintf(stderr, "%s\n", s);
    return 0;
}

