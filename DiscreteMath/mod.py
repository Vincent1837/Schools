x = 1
m = 101
power = (123**2) % m
bin_str = bin(1001)[:1:-1]
print(bin_str)
for i in bin_str:
    print("char : ", i)
    if i == "1":
        x = (x * power) % m
        
    else:
        power = (power*power) % m
    print("x, power : ", x, power)
        

print(x)