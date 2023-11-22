%{  
    int indentation = 0;
%}

leftbrace [^\n\{]*\{[^\n]*\n 
rightbrace [^\n\}]*\}[^\n]*\n
line [^\n\{\}]*\n 

%%
{leftbrace} {
    for(int i=0 ; i<indentation ; i++)
        printf("\t"); 
    ECHO;
    indentation++;
} 

{rightbrace} { 
    indentation--;
    for(int i=0 ; i<indentation ; i++)
        printf("\t"); 
    ECHO;
}

{line} {
    for(int i=0 ; i<indentation ; i++)
        printf("\t");
    ECHO;     
}

%%
int main(int argc, char* argv[]){
    yylex();
    return 0;
}