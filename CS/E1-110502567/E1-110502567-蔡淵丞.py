"""
Exam 1
Name: 蔡淵丞
Student Number: 110502567
Course 2021-CE1003-B
"""
while True:
    N = input()
    if N == "stop" :
        break
    else:
        W = int(input())
        H = int(input())
        T = int(input())
        F = int(input())
        S = input()
        for j in range(F):
            for i in range(H):
                if i >= T and i <= H-T-1 :
                    print((S*T + " "*(W-T*2) + S*T) * int(N))
                else:
                    print(S*W*int(N))