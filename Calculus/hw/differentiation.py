from pylab import *
from sympy import *
x = symbols("t")
result = limit(sin(x)/x, x, 0)
print(result)