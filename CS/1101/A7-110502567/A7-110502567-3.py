"""
Assignment 7
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
import itertools
with open("digit.txt", 'r') as data:
    digits = data.read()
    
lst = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

with open("110502567.txt","w", encoding="utf-8") as data:
    if digits == "1":
        data.write("none")
        data.write("\n110502567蔡淵丞")
    else :
        for i in list(itertools.product(*[lst[int(x)-2] for x in digits])):
            str = ""
            for j in i:
                str += j
            data.write(str + " ")
        data.write("\n110502567蔡淵丞")