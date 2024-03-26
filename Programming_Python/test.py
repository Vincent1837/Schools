
import numpy as np
import matplotlib.pyplot as plt

def factorial(n) :
  f=1
  for i in range(2,n+1) : f *= i
  return f

def taylor_poly(n, xs) :
  s = 0
  for k in range(n) :
    s = s + ( (-1) ** (k) * xs ** (2 * k + 2)) / factorial(2 * k + 1)
  return s 

a, b, m = -2 * np.pi , 2 * np.pi, 100
xs = np.linspace(a, b, m)
n = 10
for i in range(1, n) :
  ys = taylor_poly(i, xs)
  plt.plot(xs, ys, label = "p" + str(2 * (i)))

plt.plot(xs, xs * (np.sin(xs)), label="x sin(x)")
plt.title("Taylor polynomials with different orders for x sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.ylim(-6, 2)
plt.show()



'''
# Function definition
def f(xs):
    return xs * np.sin(xs)

# Taylor polynomial function
def taylor_polynomial(xs, degree):
    result = 0
    for n in range(1, degree + 1):
        term = ((-1) ** (n - 1)) * (xs ** (2*n)) / factorial(2*n-1)
        result += term
    return result

# Values
xs_values = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(xs_values, f(xs_values), label="f(xs) = xs * sin(xs)", color='black')

for degree in range(1, 11):
    plt.plot(xs_values, taylor_polynomial(xs_values, degree), label=f"P{2*degree}")

plt.title("Taylor polynomials with different orders for xs sin(xs)")
plt.xslabel("Xs")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
'''

"""
import pylab , numpy
def factorial(n) :
  f=1
  for i in range(2,n+1) : f *= i
  return f
def taylor_poly(n,xs) :
  s = 0
  for k in range(n) :
    s = s + ( (-1)**(k)* xs**(2*k+2) ) / factorial(2*k+1)
  return s 
a , b , m = -2*numpy.pi , 2*numpy.pi , 100
xss = numpy.linspace(a,b,m)
n = 10
for i in range(1,n) :
  ys = taylor_poly(i,xss)
  pylab.plot( xss, ys, label="p"+str(2*(i)))
pylab.plot( xss, xss*(numpy.sin(xss)), label="xs sin(xs)")
pylab.title("Taylor polynomials with different orders for xs sin(xs)")
pylab.legend()
pylab.grid()
pylab.xslabel("Xs")
pylab.ylabel("Y")
pylab.ylim(-6,2)
pylab.show()"""