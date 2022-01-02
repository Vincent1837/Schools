"""
Exam 3
Name: 蔡淵丞
Student Number: 110502567
Course 2021-CE1003-B
"""
def convert62(c):
    if ord(c) in range(47, 58):
        return int(c)
    elif ord(c) in range(65, 91):
        return ord(c)-55
    else:
        return ord(c)-61 

def func(str, idx):
    decnum = 0
    for i in range(len(str)):
        decnum += (idx**i)*convert62(string[i])

    return decnum

while True:
    string = input()
    if string == "-1":
        break
    flg = True
    for i in range(convert62(max(string))+1,63 ):
        if func(string, i) % (i-1) == 0:
            print(i)
            flg = False
            break
    if flg:
        print("such number is impossible!")