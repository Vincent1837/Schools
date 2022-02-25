"""
Exam 2
Name: 蔡淵丞
Student Number: 110502567
Course 2021-CE1003-B
"""
with open("invoice.txt", "r") as data:
    invoice = data.readlines()
    invoice[-1] += "\n"
    
with open("num.txt", "r") as data:
    num = data.readlines()
    num[-1] += "\n"

lst = [0 for i in range(10)]

print(invoice)
for i in invoice:
    if i == num[0]:
        lst[0] += 1
        lst[9] += 10000000
    elif i == num[1]:
        lst[1] += 1
        lst[9] += 2000000
    elif i == num[2] or i == num[3] or i == num[4]:
        lst[2] += 1
        lst[9] += 200000
    elif i[1:] == num[2][1:] or i[1:] == num[3][1:] or i[1:] == num[4][1:]:
        lst[3] += 1
        lst[9] += 40000
    elif i[2:] == num[2][2:] or i[2:] == num[3][2:] or i[2:] == num[4][2:]:
        lst[4] += 1
        lst[9] += 10000
    elif i[3:] == num[2][3:] or i[3:] == num[3][3:] or i[3:] == num[4][3:]:
        lst[5] += 1
        lst[9] += 4000
    elif i[4:] == num[2][4:] or i[4:] == num[3][4:] or i[4:] == num[4][4:]:
        lst[6] += 1
        lst[9] += 1000
    elif i[5:] == num[2][5:] or i[5:] == num[3][5:] or i[5:] == num[4][5:] or i[5:] == num[5] or i[5:] == num[6] or i[5:] == num[7]:
        lst[7] += 1
        lst[9] += 200
    else:
        lst[8] += 1
    
print("特別獎 :", lst[0])
print("特獎 :", lst[1])
print("頭獎 :", lst[2])
print("二獎 :", lst[3])
print("三獎 :", lst[4])
print("四獎 :", lst[5])
print("五獎 :", lst[6])
print("六獎 :", lst[7])
print("沒中獎 :", lst[8])
print(lst[9])