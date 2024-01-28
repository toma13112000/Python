import numpy as np
def f(x,y):
    return x**2 - 5*y - 3
def fx(x,y):
    return 2*x
def fy(x,y):
    return -5
def G(x,y):
    2*x-4*y+5
def Gx(x,y):
    return 2
def Gy(x,y):
    return -4
def delt(x, y):
    return fx(x,y)*Gy(x,y)-fy(x,y)*Gx(x,y)
def deltx(x, y):
    return f(x,y)*Gy(x,y)-fy(x,y)*G(x,y)
def delty(x, y):
    return fx(x,y)*G(x,y)-f(x,y)*Gx(x,y)
def Jac(x, y):
    return fx(x,y)*Gy(x,y)-fy(x,y)*Gx(x,y)
def Newton2D(x,y,k):
    while abs(x[1]-x[0]) or abs(y[1]-y[0]) < e:
        if(k!=0):
            x[0]=x[1]
            y[0]=y[1]
        x[1]=x[0]-1/Jac(x[0],y[0])*deltx(x[0],y[0])
        y[1]=y[0]-1/Jac(x[0],y[0])*delty(x[0],y[0])
        k = k+1
    print('Iteration-%d, x1 = %0.6f and y1 = %0.6f' % (k, x[1], y[1]))
x = np.zeros(2)
y = np.zeros(2)
e = 0.000001
x[0] = 1
y[0] = 2
print(Newton2D(x,y,0))