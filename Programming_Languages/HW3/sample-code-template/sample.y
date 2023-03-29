%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void yyerror(const char *message);

/** If you need global variable, declare them here **/

%}

%union{
	char sval[64];
	int ival;
}

%token IF INT PRINT
%token<ival> NUMBER
%token<sval> ID STRING
%type<ival> id_val

%%

program		: def_stmt def_stmt cond_exp
			;
def_stmt	: /**def_stmt grammar**/ ';' { /** 當語法 match 時會執行這裡的 code **/ }
			;
cond_exp	: IF /**cond_exp grammar**/ { }
			;
id_val		: ID { }
			;
stdout		: /**stdout grammar**/ ';' { }
			;

%%

void yyerror (const char *message)
{
	/** This function is called when there is a syntax error **/
	/** 輸入的文法錯誤時會 call 這個 function **/
}

int main()
{
	/** You can write any code in main function **/
	yyparse();

	return 0;
}