%{
#include "sample.tab.h"
#include "string.h"

/** RE 請換成 regular expression **/
%}
%option noyywrap

number	RE
id		RE
string	RE

%%

RE		{ return INT; }
RE		{ return IF; }
RE    	{ return PRINT; }
RE      { return yytext[0]; }
{number}	{ /** assign NUMBER token's value **/ return NUMBER; }
{id}		{ /** assign ID token's value **/ return ID; }
{string}	{ /** assign STRING token's value **/ return STRING; }

[\n\t\r ]	{}
.			{}

%%