"""
Practice 5
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
while True:
    get = input("NUM(BIN) : ")
    if get == "-1":
        print("\n")
        break
    
    elif set(get) == {"0", "1"} or set(get) == {"0"} or set(get) == {"1"}:
        print("NUM(DEC) after X16 : {}".format(int(get, 2)*16))
        print("NUM(OCT) : {}\n".format(oct(int(get, 2)*16)[2:]))
    
    else:
        print("Not Binary Number !\n")