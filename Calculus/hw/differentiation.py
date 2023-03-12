import numpy
import pylab

def factorial(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def taylorPloy(n, m):
    s = 0
    for k in range(n):
        s += (-1)**pylab.floor(k/2) * (m**k / factorial(k))
    return s

x = numpy.linspace(0, 10.5, 100)
n = 20

for i in range(1, n, 2):
    y = taylorPloy(i, x)
    pylab.plot(x, y, label='p'+str(i))
pylab.plot(x, pylab.sin(x)+pylab.cos(x), label="sin(x)+cos(x)")

pylab.title("Taylor ploynomials with different orders for sin(x)+cos(x)")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.grid()
pylab.legend()
pylab.ylim(-2, 2)
pylab.show()