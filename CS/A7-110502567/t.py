def print_parentheses(n: int):
    if n == 1:
        return {"()"}
    return {"("+i+")" for i in print_parentheses(n-1)} | {"()"+i for i in print_parentheses(n-1)} | {i+"()" for i in print_parentheses(n-1)}
print(" \n".join(print_parentheses(int(input()))))