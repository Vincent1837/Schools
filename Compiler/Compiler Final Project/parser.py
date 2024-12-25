import ply.yacc as yacc
from lexer import *

# Symbol table for variable and function definitions
symbol_table = {}

# Grammar rules
def p_program(p):
    '''program : stmt_list'''
    p[0] = p[1]

def p_stmt_list(p):
    '''stmt_list : stmt
                 | stmt_list stmt'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_stmt(p):
    '''stmt : exp
            | def_stmt
            | print_stmt'''
    p[0] = p[1]

def p_print_stmt(p):
    '''print_stmt : LPAREN PRINT_NUM exp RPAREN
                  | LPAREN PRINT_BOOL exp RPAREN'''
    if p[2] == 'print-num':
        print(p[3])
    elif p[2] == 'print-bool':
        print('#t' if p[3] else '#f')

def p_exp(p):
    '''exp : bool_val
           | number
           | VARIABLE
           | num_op
           | logical_op
           | fun_exp
           | fun_call
           | if_exp'''
    p[0] = p[1]

def p_bool_val(p):
    '''bool_val : TRUE
                | FALSE'''
    p[0] = p[1]

def p_number(p):
    '''number : NUMBER'''
    p[0] = p[1]
    
def p_num_op(p):
    '''num_op : LPAREN PLUS exp_list RPAREN
              | LPAREN MINUS exp exp RPAREN
              | LPAREN MULTIPLY exp_list RPAREN
              | LPAREN DIVIDE exp exp RPAREN
              | LPAREN MOD exp exp RPAREN
              | LPAREN GREATER exp exp RPAREN
              | LPAREN SMALLER exp exp RPAREN
              | LPAREN EQUAL exp_list RPAREN'''
    if p[2] == '+':
        p[0] = sum(p[3])
    elif p[2] == '-':
        p[0] = p[3] - p[4]
    elif p[2] == '*':
        p[0] = 1
        for num in p[3]:
            p[0] *= num
    elif p[2] == '/':
        p[0] = p[3] // p[4]
    elif p[2] == 'mod':
        p[0] = p[3] % p[4]
    elif p[2] == '>':
        p[0] = '#t' if p[3] > p[4] else '#f'
    elif p[2] == '<':
        p[0] = '#t' if p[3] < p[4] else '#f'
    elif p[2] == '=':
        p[0] = '#t' if all(x == p[3][0] for x in p[3]) else '#f'

def p_logical_op(p):
    '''logical_op : LPAREN AND exp_list RPAREN
                  | LPAREN OR exp_list RPAREN
                  | LPAREN NOT exp RPAREN'''
    if p[2] == 'and':
        p[0] = '#t' if all(p[3]) else '#f'
    elif p[2] == 'or':
        p[0] = '#t' if any(p[3]) else '#f'
    elif p[2] == 'not':
        p[0] = '#t' if not p[3] else '#f'

def p_exp_list(p):
    '''exp_list : exp
                | exp_list exp'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_def_stmt(p):
    '''def_stmt : LPAREN DEFINE VARIABLE exp RPAREN'''
    symbol_table[p[3]] = p[4]
    p[0] = f"Defined {p[3]} = {p[4]}"

def p_variable(p):
    '''VARIABLE : ID'''
    if p[1] in symbol_table:
        p[0] = symbol_table[p[1]]
    else:
        raise ValueError(f"Undefined variable '{p[1]}'")

def p_fun_exp(p):
    '''fun_exp : LPAREN FUN fun_ids fun_body RPAREN'''
    p[0] = {'params': p[4], 'body': p[6]}

def p_fun_ids(p):
    '''fun_ids : VARIABLE
               | fun_ids VARIABLE
               | empty'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_fun_body(p):
    '''fun_body : exp'''
    p[0] = p[1]

def p_fun_call(p):
    '''fun_call : LPAREN fun_exp param_list RPAREN
                | LPAREN fun_name param_list RPAREN'''
    if isinstance(p[2], dict):  # Anonymous function
        params = p[2]['params']
        body = p[2]['body']
        bindings = dict(zip(params, p[3]))
        p[0] = evaluate_function(body, bindings)
    elif p[2] in symbol_table:  # Named function
        func = symbol_table[p[2]]
        params = func['params']
        body = func['body']
        bindings = dict(zip(params, p[3]))
        p[0] = evaluate_function(body, bindings)
    else:
        raise ValueError(f"Undefined function '{p[2]}'")
    
def p_fun_name(p):
    '''fun_name : ID'''
    p[0] = p[1]

def p_param_list(p):
    '''param_list : exp
                  | param_list exp'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_if_exp(p):
    '''if_exp : LPAREN IF test_exp then_exp else_exp RPAREN'''
    p[0] = p[4] if p[3] == '#t' else p[5]

def p_test_exp(p):
    '''test_exp : exp'''
    p[0] = p[1]

def p_then_exp(p):
    '''then_exp : exp'''
    p[0] = p[1]

def p_else_exp(p):
    '''else_exp : exp'''
    p[0] = p[1]

def p_empty(p):
    '''empty :'''
    p[0] = None

def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Helper function to evaluate function calls
def evaluate_function(body, bindings):
    global symbol_table
    original_symbols = symbol_table.copy()
    symbol_table.update(bindings)
    result = parser.parse(body)
    symbol_table = original_symbols
    return result

# Build the parser
parser = yacc.yacc()

# unit test for parser
if __name__ == '__main__':

    test_file = 'public_test_data/01_1.lsp'
    with open(test_file):
        code = ''.join(line.rstrip() for line in open(test_file))
    result = parser.parse(code, lexer=lexer)
    print(result)