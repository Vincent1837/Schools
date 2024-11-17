%{
    #include <bits/stdc++.h>
    using namespace std;

    int count = 0;

    void print_tabs() {
        for (int i = 0; i < count; i++) {
            cout << "\t";
        }
    }

    int count_tabs(const string &s) {
        int ret = 0;
        for (char i : s) {
            if (i != '\t') break;
            ret++;
        }
        return ret;
    }

    void print_brace(const string &s) {
        while (count_tabs(s) < count) {
            count--;
            print_tabs();
            cout << "}\n";
        }
    }

    extern "C" int yywrap() { return 1; }
%}

%x ONE_LINE
%x MORE_LINE
%x PS

%%

"\t"*"# " {
    string s = yytext;
    print_brace(s);
    print_tabs();
    cout << "// ";
    BEGIN ONE_LINE;
}

<ONE_LINE>\n {
    cout << "\n";
    BEGIN INITIAL;
}

<ONE_LINE>. {
    cout << yytext;
}

"\t"*"\"\"\"" {
    string s = yytext;
    print_brace(s);
    print_tabs();
    cout << "/*";
    BEGIN MORE_LINE;
}

<MORE_LINE>"\"\"\"\n" {
    cout << "*/\n";
    BEGIN INITIAL;
}

<MORE_LINE>.|\n {
    cout << yytext;
}

"\t"*"print(" {
    string s = yytext;
    print_brace(s);
    print_tabs();
    cout << "cout << ";
    BEGIN PS;
}

<PS>")"\n? {
    cout << " << endl;\n";
    BEGIN INITIAL;
}

<PS>. {
    cout << yytext;
}

"if "(True|False)":\n" {
    print_tabs();
    cout << "if(" << (yytext[3] == 'T' ? "true" : "false") << ") {\n";
    count++;
}

"\t"* {
    string s = yytext;
    print_brace(s);
}

\n|\r\n {
    string s = yytext;
    print_brace(s);
    cout << "\n";
}

. {}

%%

int main(int argc, char *argv[]) {
    yylex();
    print_brace("");
    return 0;
}
