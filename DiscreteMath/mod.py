def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

def p(n:int, r:int):
    return factorial(n)//factorial(n-r)

def c(n:int, r:int):
    return factorial(n)//(factorial(r)*factorial(n-r))

print(c(12,5)-c(9,5)-c(7,5))