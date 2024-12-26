# NCU 1131 Compiler Final Project Documentation

## Mini-LISP interpreter implementation

### Basic Features

| Feature               | Description                                    | Points |
|-----------------------|------------------------------------------------|--------|
| **1. Syntax Validation**  | Print "syntax error" when parsing invalid syntax | 10     |
| **2. Print**              | Implement `print-num` statement                | 10     |
| **3. Numerical Operations** | Implement all numerical operations            | 25     |
| **4. Logical Operations** | Implement all logical operations               | 25     |
| **5. if Expression**      | Implement `if` expression                      | 8      |
| **6. Variable Definition** | Able to define a variable                     | 8      |
| **7. Function**           | Able to declare and call an anonymous function | 8      |
| **8. Named Function**     | Able to declare and call a named function      | 6      |

---

### Bonus Features

| Feature               | Description                                     | Points |
|-----------------------|-------------------------------------------------|--------|
| **1. Recursion**          | Support recursive function call                 | 5      |
| **2. Type Checking**      | Print error messages for type errors            | 5      |
| **3. Nested Function**    | Nested function (static scope)                  | 5      |
| **4. First-class Function** | Able to pass functions, support closure        | 5      |

### My Inplemented Features

I have implemented features **1. Syntext Validation ~ 6. Variable** Definition in python.

#### File Structure

```text
    ----lexer.py            (Lexical analizer)
    |
    |
    ----parser.py           (Parser)
----|
    |
    ----main.py             (Opens test files and parses them)
    |
    |
    ----public_test_data    (folder containing test files) 
```

# Usage

1. Install the `ply` library using `pip install ply`

2. Run **main.py** and it will interpret the test files

```python
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
            print('---------------------------------------------')

if __name__ == "__main__":
    main()
```