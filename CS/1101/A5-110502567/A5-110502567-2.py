"""
Assignment 5
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""

def bin_to_dec(str):
    dec_num = 0
    str_lst = [x for x in str]
    str_lst.reverse()
    for i in range(len(str_lst)):
        if str_lst[i] == "1":
            dec_num += (2**i)
    return dec_num

def dec_to_bin(num):
    bin_str = ""
    while num != 0:
        if num % 2 == 0:
            bin_str = "0" + bin_str
        else:
            bin_str = "1" + bin_str
        num //= 2
    return bin_str

def main():
    while True:
        get = input()
        if get == "-1":
            break
        elif "+" in get:
            a = get.split("+")[0]
            b = get.split("+")[1]
            print(dec_to_bin(bin_to_dec(a) + bin_to_dec(b)))
        elif "-" in get:
            a = get.split("-")[0]
            b = get.split("-")[1]
            print(dec_to_bin(bin_to_dec(a) - bin_to_dec(b)))
        else :
            print("No operator found !")
            break
main()