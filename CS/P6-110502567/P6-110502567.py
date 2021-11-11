"""
Practice 6
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
def function(number):
    if number <= 0:
        return 0

    elif number % 2 == 0:
        return 2 + function(number//2)

    else:
        return 3 + function(function2(number)-5)

def function2(number):
    num_str = str(number)
    sum = 0
    for i in num_str:
        sum += int(i)
    return sum

with open ("test.txt", "r") as data:
        for i in data.readlines():
            print(function(int(i)))
