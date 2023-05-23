from sympy import *

init_printing()
var('x, y')
fn = x*(y**2)*log(x**2)
for i in range(3):
    ifn = Integral(fn,x,y)
    fn = ifn.doit()
    pprint(ifn)
    print("=")
    pprint(fn)
    print()
fn = x*(y**2)*log(x**2) 
for i in range(3):
    ifn = Integral(fn,y,x)
    fn = ifn.doit()
    pprint(ifn)
    print("=")
    pprint(fn)
    print()

