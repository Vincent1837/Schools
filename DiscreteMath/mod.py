import random
a = random.randrange(1, 100)
b = random.randrange(1, 100)
ans = a - b

while 1:
    print(a, '-', b)
    get = int(input("答案是..."))
    if get == ans:
        print("答對了，好棒！")
        break
    else:
        get = int(input("答錯了，請重算一次，答案是..."))
        if get == ans:
            print("答對了！")
            break
        else:
            print("答錯了！正確答案是", ans)
            break