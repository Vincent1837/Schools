from lexer import lexer
from parser import parser

def main():
    # Load test data
    test_file = "public_test_data/01_1.lsp"  # Replace with your actual file path
    try:
        with open(test_file, "r") as f:
            code = f.read()

        print("Processing Mini-LISP code...")
        # Parse the code
        result = parser.parse(code, lexer=lexer)
        print("Parsing completed!")
        print("Result:")
        print(result)

    except FileNotFoundError:
        print(f"File '{test_file}' not found!")

if __name__ == "__main__":
    main()
