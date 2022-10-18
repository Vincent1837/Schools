"""
Practice 4
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
def read_file(fileName, mode = "r"):
    with open(fileName, mode) as f:
        lines = f.readlines()
        list_of_formulas = []
        for i in lines:
            list_of_formulas.append(i.split())
    return list_of_formulas

def judge_the_formula(formula):
    if formula[1] == "+":
        T_F = "T" if int(formula[0]) + int(formula[2]) == int(formula[4]) else "F"
    elif formula[1] == "-":
        T_F = "T" if int(formula[0]) - int(formula[2]) == int(formula[4]) else "F"
    else:
        T_F = "T" if int(formula[0]) * int(formula[2]) == int(formula[4]) else "F"
    return T_F

def main():
    with open("ans-110502567.txt", "w") as answer:
        for i in read_file("test.txt"):
            answer.write("{}\n".format(judge_the_formula(i)))


if __name__ == "__main__":
    main()