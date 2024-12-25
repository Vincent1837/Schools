from lexer import lexer
from parser import parser

def main():
    for i in range(7, 9):
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

if __name__ == "__main__":
    main()
