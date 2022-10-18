"""
Assignment 3
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
import math
def main():
    with open("test.txt", "r") as data_be_read:
        nums = []
        for i in data_be_read.readline().split():
            nums.append(int(i)) # int nums = [num1, num2, ..., numN]
    with open("answer.txt", "w") as data_be_writed:
        for i in range(len(nums)):
            data_be_writed.write("Number_{}: {}\n".format(i+1,nums[i]))    
            for j in find_factor(nums[i]):
                data_be_writed.write("{} {}\n".format(j, find_prime(j)))
    return

def find_factor(num):
    facts = []
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            facts.append(i)
            facts.append(num//i)
    facts.sort()
    facts = list(dict.fromkeys(facts)) # remove duplicates
    
    return facts

def find_prime(num):
    is_prime = True
    if num == 1:
        is_prime = False
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
    Y_N = "Y" if is_prime else "N"
    return Y_N

main()