import ply.lex as lex

# Reserved words
reserved = {
    'define': 'DEFINE',
    'fun': 'FUN',
    'if': 'IF',
    'and': 'AND',
    'or': 'OR',
    'not': 'NOT',
    'mod': 'MOD',
    'print-num': 'PRINT_NUM',
    'print-bool': 'PRINT_BOOL'
}

# Token definitions
tokens = [
    'NUMBER', 'ID', 'PLUS', 'MINUS', 'MULTIPLY', 'DIVIDE', 'GREATER',
    'SMALLER', 'EQUAL', 'LPAREN', 'RPAREN', 'TRUE', 'FALSE', 'BOOL_VAL', "ILLEGAL"
] + list(reserved.values())

# Regular expressions for tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_GREATER = r'>'
t_SMALLER = r'<'
t_EQUAL = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_BOOL_VAL = r'\#t|\#f'


# Reserved words and identifiers
def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9\-]*'
    t.type = reserved.get(t.value, 'ID')  # Check for reserved words
    return t

# Numbers
def t_NUMBER(t):
    r'-?\d+'
    t.value = int(t.value)
    return t

# Ignored characters
t_ignore = ' \t'

# Newline tracking
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    #print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)
    return '@@'

# Build the lexer
lexer = lex.lex()

# unit test for lexer
if __name__ == '__main__':
    test_file = 'public_test_data/b1_1.lsp'
    with open(test_file):
        code = ''.join(line.rstrip() for line in open(test_file))
    # code = '156 define ()))(or@) if bool-val #t #f'
    lexer.input(code)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)
