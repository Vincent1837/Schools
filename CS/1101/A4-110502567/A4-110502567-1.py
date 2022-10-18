"""
Assignment 4
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
with open("score.txt", "r") as f:
    data = list(map(lambda x : x.split() , f.readlines()))

with open("score_110502567.txt", "w") as f:
    for i in data:
        sum = 0
        if i == data[0]:
            continue
        for j in range(1,5):
            sum += int(i[j])
        i.append(sum/4)
    for lines in data:
        for items in lines:
            f.write(str(items)+" ")
            if items == lines[5]:
                f.write("\n")