"""
Assignment 4
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
with open("score_110502567.txt", "r") as f:
    data = list(map(lambda x : x.split() , f.readlines()))
names = [data[i][0].lower() for i in range(1,6)]
items = [data[0][i].lower() for i in range(6)]
item = input("查詢項目: ").lower()
name = input("姓名: ").lower()
if item in items and name in names:
    print("{} {} {}".format(data[names.index(name)+1][0],
    data[0][items.index(item)], data[names.index(name)+1][items.index(item)]))