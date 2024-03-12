
import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.log(x)

x = np.linspace(0, 10, 100)
plt.plot(x, f(x))
plt.plot(x, x)
plt.plot(x, x**2.71828)
plt.grid(True)
plt.show()



'''
# Function definition
def f(x):
    return x * np.sin(x)

# Taylor polynomial function
def taylor_polynomial(x, degree):
    result = 0
    for n in range(1, degree + 1):
        term = ((-1) ** (n - 1)) * (x ** (2*n)) / factorial(2*n-1)
        result += term
    return result

# Values
x_values = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Plotting
plt.figure(figsize=(12, 8))
plt.plot(x_values, f(x_values), label="f(x) = x * sin(x)", color='black')

for degree in range(1, 11):
    plt.plot(x_values, taylor_polynomial(x_values, degree), label=f"P{2*degree}")

plt.title("Taylor polynomials with different orders for x sin(x)")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()
'''

