from lexer import lexer
from parser import parser

def main():
    for i in range(1, 7):
        for j in range(1, 3):
            test_file = f'public_test_data/0{i}_{j}_hidden.lsp'
            with open(test_file) as f:
                code = f.read()
            print(f'Test 0{i}_{j}:')
            print(code)
            try:
                result = parser.parse(code, lexer=lexer)
            except Exception as e:
                print(f'syntax error')
            print('----------------------------------------------------------------')

if __name__ == "__main__":
    main()
