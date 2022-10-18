import itertools
lst = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
digits = input()
if digits == "0":
    print("none")
else :
    for i in list(itertools.product(*[lst[int(x)-2] for x in digits])):
        str = ""
        for j in i:
            str += j
        print(str + " ", end="")