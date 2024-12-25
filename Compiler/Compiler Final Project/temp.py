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
        print("#t" if p[3] == "#t" else "#f")

def p_exp(p):
    '''exp : BOOL_VAL
           | number
           | variable
           | num_op
           | logical_op
           | fun_exp
           | fun_call
           | if_exp'''
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
        p[0] = '#t' if all(x == '#t' for x in p[3]) else '#f'
    elif p[2] == 'or':
        p[0] = '#t' if any(x == '#t' for x in p[3]) else '#f'

    elif p[2] == 'not':
        p[0] = '#t' if p[3] != "#t" else '#f'

def p_exp_list(p):
    '''exp_list : exp
                | exp_list exp'''
    p[0] = [p[1]] if len(p) == 2 else p[1] + [p[2]]

def p_def_stmt(p):
    '''def_stmt : LPAREN DEFINE ID exp RPAREN'''
    symbol_table[p[3]] = p[4]
    p[0] = f"Defined {p[3]} = {p[4]}"

def p_variable(p):
    '''variable : ID'''
    p[0] = p[1]  # Pass the variable name for evaluation later

def p_fun_call(p):
    '''fun_call : LPAREN fun_exp param_list RPAREN
                | LPAREN ID param_list RPAREN'''
    if isinstance(p[2], dict):  # Inline function
        params = p[2]['params']
        body = p[2]['body']
        if len(params) != len(p[3]):
            raise ValueError(f"Expected {len(params)} arguments, got {len(p[3])}")
        bindings = dict(zip(params, p[3]))
        p[0] = evaluate_function(body, bindings)
    else:  # Named function
        func = symbol_table.get(p[2])
        if func is None:
            raise ValueError(f"Undefined function '{p[2]}'")
        params = func['params']
        body = func['body']
        if len(params) != len(p[3]):
            raise ValueError(f"Expected {len(params)} arguments, got {len(p[3])}")
        bindings = dict(zip(params, p[3]))
        p[0] = evaluate_function(body, bindings)

        
def p_fun_exp(p):
    '''fun_exp : LPAREN FUN LPAREN fun_ids RPAREN fun_body RPAREN'''
    p[0] = {'params': p[4], 'body': p[6]}

def p_fun_ids(p):
    '''fun_ids : ID
               | fun_ids ID
               | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]] 

def p_fun_body(p):
    '''fun_body : exp'''
    p[0] = p[1] 


def p_param_list(p):
    '''param_list : exp
                  | param_list exp
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]]

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

def evaluate_function(body, bindings):
    return evaluate_expression(body, bindings)

def evaluate_expression(exp, bindings=None):
    if isinstance(exp, dict):  # Compound expressions (e.g., operations)
        operator = exp.get('operator')
        args = [evaluate_expression(arg, bindings) for arg in exp.get('args', [])]
        # Handle arithmetic operations
        if operator == '+':
            return sum(args)
        elif operator == '*':
            result = 1
            for arg in args:
                result *= arg
            return result
        elif operator == '-':
            return args[0] - args[1]
        elif operator == '/':
            return args[0] // args[1]
    elif isinstance(exp, str):  # Variable lookup
        if bindings and exp in bindings:  # Check local scope first
            return bindings[exp]
        elif exp in symbol_table:  # Check global scope
            return symbol_table[exp]
        else:
            raise ValueError(f"Undefined variable '{exp}'")
    else:
        return exp  # Literal values (numbers, booleans, etc.)

# Build the parser
parser = yacc.yacc(debug=True)

# unit test for parser
if __name__ == '__main__':
    for i in range(1, 9):
        for j in range(1, 3):
            test_file = f'public_test_data/0{i}_{j}.lsp'
            with open(test_file) as f:
                code = f.read()
            print(f'Test 0{i}_{j}:')
            print(code)
            try:
                result = parser.parse(code, lexer=lexer)
                print(f'Result: {result}')
            except Exception as e:
                print(f'syntax error: {e}')
            print('----------------------------------------------------------------')
