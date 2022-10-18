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
    get_set = set(get)
    
    if get == "0":
        break

    elif "." in get or "-" in get:
        print("Error: Input should be a positive integer!\n")

    elif " " in get:
        print("Error: Blank space found in the input!\n")
    
    elif get_set.issubset({str(num) for num in range(10)}):
        if int(get) > 500:
            print("Error: Input should be less than  or equal to 500!\n")
            continue
        print(function(int(get)))

    else :
        print("Error: Input should be a positive integer!\n")