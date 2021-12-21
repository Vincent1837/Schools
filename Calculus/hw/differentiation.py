from math import e , log
from numpy import cos, pi, sin
from numpy.core.function_base import linspace

def f(x):
    return 7**cos(x)*sin(x)

isum = 7/log(7, e) - 1/log(7, e)

x , dx= linspace(0,pi/2,101,retstep=True)

y = [f(i) for i in x]

rsum, lsum, usum, tsum = 0, 0, 0, 0

for i in range(0, len(y)-1):
    rsum += y[i]
    lsum += min(y[i],y[i+1])
    usum += max(y[i],y[i+1])
    tsum += y[i]+y[i+1]
rsum -= y[0]

rsum *= dx
lsum *= dx
usum *= dx
tsum *= dx/2

print(f"{'數學積分':8s} : {isum:.9f}\n\n")
print("迴圈求積:")
print(f"{'矩陣積分':8s}  : {rsum:.9f} 誤差: {abs(isum-rsum):<.10f}")
print(f"{'上矩形積分':8s} : {usum:.9f} 誤差: {abs(isum-usum):<.10f}")
print(f"{'下矩形積分':8s} : {lsum:.9f} 誤差: {abs(isum-lsum):<.10f}")
print(f"{'梯形積分法':8s} : {tsum:.9f} 誤差: {abs(isum-tsum):<.10f}\n\n")
isum1 = dx * sum(y[:-1])
isum2 = dx * sum([y[0], 2*sum(y[1:-1]), y[-1]])/2
isum3 = dx * sum([y[0],8*sum(y[1:-1:2]), 2*sum(y[2:-1:2]), y[-1]])/3
print("公式求積:")
print(f"{'矩形積分法':8s} : {isum1:<.9f} 誤差: {abs(isum-isum1):<.10f}")
print(f"{'梯形積分法':8s} : {isum2:<.9f} 誤差: {abs(isum-isum2):<.10f}")
print(f"{'Simpson積分':8s} : {isum3:<.9f} 誤差: {abs(isum-isum3):<.10f}")
