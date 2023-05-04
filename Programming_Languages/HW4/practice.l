%{
#include "y.tab.h"
%}

%option yylineno

int_number	[0-9]+
float_number  [0-9]+\.[0-9]+   
id		[A-Z]

%%

int		                { return INT; }
float                   { return FLOAT;}
print    	            { return PRINT; }
(=|\+|-|;)              { return yytext[0]; }
{float_number}	        { yylval.fval=atof(yytext); return FLOAT_NUMBER; }
{int_number}	        { yylval.ival=atoi(yytext); return INT_NUMBER; }
{id}		            { strncpy(yylval.sval,yytext,strlen(yytext));yylval.sval[strlen(yytext)]='\0'; return ID; }
[\n\t\r]	            {}
.			            {}

%%

int yywrap() {
    return 1;
}