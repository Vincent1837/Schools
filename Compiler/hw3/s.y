%{
    #include <stdio.h>
    #include <stdlib.h>

    int yylex();

    int stack[1000];
    int sp = -1;

    void push(int value) {
        if (sp < 999) {
            stack[++sp] = value;
        } else {
            printf("Invalid format\n")
            exit(EXIT_FAILURE);
        }
    }

    int pop() {
        if (sp >= 0) {
            return stack[sp--];
        } else {
            printf("Invalid format\n");
        }
    }
%}

%token NUMBER
%token ADD SUB MUL MOD INC DEC LOAD

%%

program: 
        | program statement '\n' {}

statement: expr {}

expr: ADD           { push(pop() + pop()); }
    | SUB           { push(-pop() + pop()); }
    | MUL           { push(pop() * pop()); }
    | MOD           { int b = pop(); int a = pop(); push(a % b); }
    | INC           { push(pop() + 1); }
    | DEC           { push(pop() - 1); }
    | LOAD NUMBER   { push(%2); }
    ;

%%

int main() {
    yyparse();
    if (sp == 0) {
        printf("%d", pop());
        return 0;
    } else {
        printf("Invalide format\n");
        exit(EXIT_FAILURE);
    }
}

int yylex() {
    char string[1000];
    scanf("%s", string);
    char c = string [0];
    if (c == '\n' || c == EOF) {
        return 0;
    } else if (c == 'a') {
        return ADD;
    } else if (c == 's') {
        return SUB;
    } else if (c == 'm' && string[1] == 'u') {
        return MUL;
    } else if (c == 'm' && string[1] == 'o') {
        return MOD;
    } else if (c == 'i') {
        return INC;
    } else if (c == 'd') {
        return DEC;
    } else if (c == 'l') {
        int val;
        scanf("%d", &val);
        yylval = val;
        return LOAD;
    } else if (c >= '0' && c <= '9') {
        yylval = atoi(string);
    } else {
        printf("Invalid format\n");
    }
}
