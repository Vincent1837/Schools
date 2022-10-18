"""
Assignment 7
Name: 蔡淵丞
Student Number: 110502567
Course: 2021-CE1003-B
"""
with open("seat.txt", "r") as data:
    seat = [int(x) for x in data.read()]

seat_taken = [x for x in range(len(seat)) if seat[x] == 1]

count = 1
while {0}.issubset(set(seat)):
    for i in seat_taken:
        if i-count >= 0:
            if seat[i-count] == 0:
                seat[i-count] = count+1
        if i+count < len(seat):
            if seat[i+count] == 0:
                seat[i+count] = count+1
    count += 1

furthest_seats = [x for x in range(len(seat)) if seat[x] == count]
L = count-1
print("L = {}".format(L))
print("i = {}".format(furthest_seats))