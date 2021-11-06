"""
Assignment 6
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
def function(number):
    if number >= 10:
        return 1+function(number-22)+function(function(number-30)-30)

    elif number >= 5 and number <= 9:
        return 2+function(number-2)
    
    else:
        return 3

while True:
    get = input("Please input the variable for F(N) :")
    if "." in get or "-" in get:
        print("Error: Input should be A positive integer!\n")

    elif " " in get:
        print("Error: Blank space found in the input!\n")

    elif get > 500:
        print("Error: Input should be less than  or equal to 500!\n")
    
    elif set(x for x in get) in {str(num) for num in range(10)}:
        print(function(int(get)))

    else :
        print("Error: Input should be A positive integer!\n")