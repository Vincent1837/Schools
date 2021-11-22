"""
Assignment 7
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
def print_parentheses(n: int):
    if n == 1:
        return {"()"}
    return {"("+i+")" for i in print_parentheses(n-1)} | {"()"+i for i in print_parentheses(n-1)} | {i+"()" for i in print_parentheses(n-1)}

with open("num.txt", "r") as data:
    number = int(data.read())

with open("110502567.txt", "w", encoding="utf-8") as data:
    if number == 0:
        data.write("none")
        data.write("\n110502567蔡淵丞")
        print("none")
    else:
        data.write(" ".join(print_parentheses(number)))
        data.write("\n110502567蔡淵丞")
        print(" ".join(print_parentheses(number)))