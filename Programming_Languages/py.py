from matplotlib import pylab
from numpy import *
a,b,n = 0,10*pi,1000
angs = linspace(a,b,n)
rs = sin(2.3*angs)**2 + cos(2.3*angs)**4
pylab.polar(angs,rs,lw=2,color='g')
pylab.fill(angs,rs,color='w')
pylab.title('graph of sin(2.3x)^2 + cos(2.3x)^4 for x in [0,10pi]',color='r')
