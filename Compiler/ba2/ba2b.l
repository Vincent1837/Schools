%{
#include <iostream>
#include <string>

using namespace std;

int indentation_level = 0;

void output_indentation() {
    for (int i = 0; i < indentation_level; ++i) {
        cout << "\t";
    }
}

int get_leading_tabs(const string &line) {
    int tab_count = 0;
    for (char ch : line) {
        if (ch != '\t') break;
        ++tab_count;
    }
    return tab_count;
}

void close_braces(const string &line) {
    while (get_leading_tabs(line) < indentation_level) {
        --indentation_level;
        output_indentation();
        cout << "}\n";
    }
}

extern "C" int yywrap() {
    return 1; 
}
%}

%x SINGLE_COMMENT
%x MULTI_COMMENT
%x PRINT_STATE

%%

"\t"*"# " {
    string current_line = yytext;
    close_braces(current_line);
    output_indentation();
    cout << "// ";
    BEGIN SINGLE_COMMENT;
}

<SINGLE_COMMENT>\n {
    cout << "\n";
    BEGIN INITIAL;
}

<SINGLE_COMMENT>. {
    cout << yytext;
}

"\t"*"\"\"\"" {
    string current_line = yytext;
    close_braces(current_line);
    output_indentation();
    cout << "/*";
    BEGIN MULTI_COMMENT;
}

<MULTI_COMMENT>"\"\"\"\n" {
    cout << "*/\n";
    BEGIN INITIAL;
}

<MULTI_COMMENT>.|\n {
    cout << yytext;
}

"\t"*"print(" {
    string current_line = yytext;
    close_braces(current_line);
    output_indentation();
    cout << "cout << ";
    BEGIN PRINT_STATE;
}

<PRINT_STATE>")"\n? {
    cout << " << endl;\n";
    BEGIN INITIAL;
}

<PRINT_STATE>. {
    cout << yytext;
}

"if "(True|False)":\n" {
    output_indentation();
    cout << "if(" << (yytext[3] == 'T' ? "true" : "false") << ") {\n";
    ++indentation_level;
}

"\t"* {
    string current_line = yytext;
    close_braces(current_line);
}

\n|\r\n {
    string current_line = yytext;
    close_braces(current_line);
    cout << "\n";
}
. {}

%%

int main() {
    yylex();
    close_braces("");
    return 0;
}
