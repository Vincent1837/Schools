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
        s += ((-1)**(k) * m**(k + 1)) / factorial(k)
    return s

x = numpy.linspace(0, 10.5, 100)
n = 20

for i in range(1, n+1):
    y = taylorPloy(i, x)
    pylab.plot(x, y, label='p'+str(i))
pylab.plot(x, x*pylab.exp(-x), label="xexp(-x)")

pylab.title("Taylor ploynomials with different orders for x exp(-x)")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.grid()
pylab.legend()
pylab.ylim(-2, 3)
pylab.show()