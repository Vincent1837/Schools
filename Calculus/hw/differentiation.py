from pylab import *

def h(t):
    return 1.2732 * sin(2 * t) + 0.4244 * sin(6 * t) + 0.25465 * sin(10 * t) + 0.18189 * sin(14 * t) + 0.14147 * sin(18 * t)

title("sawtooth function approximation and derivatives")
xlabel("t")
ylabel("s")

t = arange(-pi, pi, 0.00001)
z = 0.000000001
y1 = h(t)
y2 = (h(t + z) - h(t)) / z
p1, = plot(t, y1, color = 'b')
p2, = plot(t, y2, color = '#8fbc8f')

legend(handles=[p1, p2], labels=['h(t)', "h'(t)"], loc='lower right')
grid()
show()