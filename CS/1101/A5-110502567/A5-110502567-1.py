"""
Assignment 5
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""

def bin_to_hex(bin_str):
    bin_hex_dict = {
        "0000" : "0",
        "0001" : "1",
        "0010" : "2", 
        "0011" : "3",
        "0100" : "4",
        "0101" : "5", 
        "0110" : "6",
        "0111" : "7",
        "1000" : "8",
        "1001" : "9",
        "1010" : "A",
        "1011" : "B",
        "1100" : "C",
        "1101" : "D",
        "1110" : "E",
        "1111" : "F"
    }
    # Add 0s to the front
    if len(bin_str) % 4 != 0:
        bin_str = "0"*(4-(len(bin_str) % 4)) + bin_str
    
    # Group by 4
    splt_lst = []
    for idx in range(0, len(bin_str), 4):
        splt_lst.append(bin_str[idx:idx+4])

    # Convert binary to hexadecimal
    hex_lst=[bin_hex_dict[i] for i in splt_lst]
    hex_str = ""
    for i in hex_lst:
        hex_str += i

    return hex_str


while True:
    get = input("Binary: ")
    if get == "-1":
        print("\n")
        break
    elif set(get) == {"0", "1"} or set(get) == {"0"} or set(get) == {"1"}:
        print("Hexadecimal: {}".format(bin_to_hex(get).lstrip("0")))
    else:
        print("Not Binary Number!")