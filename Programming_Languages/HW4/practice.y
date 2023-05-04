%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct{
    int type;
    union {
        int int_num;
        float float_num;
    };
} Number;

Number table[26];

char badchar;

void yyerror(const char *message);

int yylex();
extern int yylineno;
%}

%union{
	char sval[64];
	int ival;
    float fval;
    struct{
        int type;
        union {
            int int_num;
            float float_num;
        };
    }number;
}

%token INT FLOAT PRINT
%token<ival> INT_NUMBER
%token<fval> FLOAT_NUMBER
%token<sval> ID
%type<number> expr
%type<number> factor
%%
program		    : def ';' | assign ';' | print ';'
                | def ';' program
                | assign ';' program
                | print ';' program;

def             : float_def | int_def 
                ;
int_def         : INT ID            {
                                        if(table[$2[0]-'A'].type!=0){
                                            badchar=$2[0];
                                            yyerror("Variable %2$c redeclaration. Error in line %1$d.");
                                        }
                                        table[$2[0]-'A'].type=1;
                                    }
                ;
float_def       : FLOAT ID          {   if(table[$2[0]-'A'].type!=0){
                                            badchar=$2[0];
                                            yyerror("Variable %2$c redeclaration. Error in line %1$d.");
                                        }
                                        table[$2[0]-'A'].type=2;
                                    }
                ;

assign          : ID '=' expr       {
                                        if(table[$1[0]-'A'].type==0){
                                            badchar=$1[0];
                                            yyerror("Variable %2$c undefined. Error in line %1$d.");
                                        }
                                        if(table[$1[0]-'A'].type!=$3.type){
                                            yyerror("Type error. Error in line %1$d.");
                                        }
                                        if(table[$1[0]-'A'].type==1) table[$1[0]-'A'].int_num=$3.int_num;
                                        if(table[$1[0]-'A'].type==2) table[$1[0]-'A'].float_num=$3.float_num;
                                    }
                ;

expr            : factor '+' factor {
                                        if($1.type!=$3.type){
                                            yyerror("Type error. Error in line %1$d.");
                                        }
                                        if($1.type==1){
                                            $$.type=1;
                                            $$.int_num=$1.int_num+$3.int_num;
                                        }
                                        if($3.type==2){
                                            $$.type=2;
                                            $$.int_num=$1.float_num+$3.float_num;
                                        }
                                    }
                | factor '-' factor {
                                        if($1.type!=$3.type){
                                            yyerror("Type error. Error in line %1$d.");
                                        }
                                        if($1.type==1){
                                            $$.type=1;
                                            $$.int_num=$1.int_num-$3.int_num;
                                        }
                                        if($3.type==2){
                                            $$.type=2;
                                            $$.int_num=$1.float_num-$3.float_num;
                                        }
                                    }
                | factor            {
                                        $$=$1;
                                    }
                ;
factor          : INT_NUMBER        {   
                                        $$.type=1;
                                        $$.int_num=$1; 
                                    }
                | FLOAT_NUMBER      {   
                                        $$.type=2;
                                        $$.float_num=$1;
                                    }
                | ID                {
                                        if(table[$1[0]-'A'].type==0){
                                            badchar=$1[0];
                                            yyerror("Variable %2$c undefined. Error in line %1$d.");
                                        }
                                        $$.type=table[$1[0]-'A'].type;
                                        if(table[$1[0]-'A'].type==1) $$.int_num=table[$1[0]-'A'].int_num;
                                        if(table[$1[0]-'A'].type==2) $$.float_num=table[$1[0]-'A'].float_num;
                                    }
                ;
print           : PRINT ID          {
                                        if(table[$2[0]-'A'].type==0){
                                            badchar=$2[0];
                                            yyerror("Variable %2$c undefined. Error in line %1$d.");
                                        }
                                        //if(table[$2[0]-'A'].type==1) printf("%d",table[$2[0]-'A'].int_num);
                                        //if(table[$2[0]-'A'].type==2) printf("%f",table[$2[0]-'A'].float_num);
                                    }
                ; 
%%


void yyerror (const char *message) {
	printf(message,yylineno,badchar);
	exit(1);
}

int main(){
    yyparse();
	return 0;
}
