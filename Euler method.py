import numpy as np
import sympy as sp
from math import exp
from sympy import pprint, dsolve, diff
from scipy.integrate import odeint
import matplotlib.pyplot as plt
a = 0; b = 2; N = 10
h = (b-a)/N
print("△x = ", h)
x = sp.Symbol('x')
y = sp.Function('y')
y(x)
dydx=sp.Eq(y(x).diff(x),(2*x*y(x))/(x**2+1))
print("Equation")
pprint(dydx)
print("Symbolic solution")
pprint(dsolve(dydx))
print("Initial value problem")
y = dsolve(dydx, ics={y(0):1})
pprint(y)
x = np.linspace(a, b, N)
print("xi : ",end="")
for i in range(0, N-1):
    xi = a + h*i
    print(round(xi,2), end= ", ")
print()
print("Exact solution: ", end="")
for i in range (0, N-1):
    xi = a+h*i
    yi = 1 + xi**2
    print(round(yi,2), end=", ")
print()
print("Numerical solution", end=": ")
f = lambda y,x: ((2*x*y)/(x**2+1))
y0 = 1
u = odeint(f, y0, x)
for i in range(0, N - 1):
    x[i] = a + h * i
    u[i + 1] = f(u[i], x[i]) * h + u[i]
    u = u.flatten()
    print(np.round(u[i],3), end=", ")
print()
print("yi+1 : ", end = "")
for i in range(0, N - 1):
    x[i] = a + h * i
    u[i + 1] = f(u[i], x[i]) * h + u[i]
    u = u.flatten()
    print(np.round(u[i+1],3), end=", ")
print()
print("△i : ", end = "")
for i in range(0, N-1):
    x[i] = a + h * i
    yi = 1 + (a + h * i) ** 2
    u[i + 1] = f(u[i], x[i]) * h + u[i]
    delta = abs(u[i] - yi)
    print(round(delta,3), end =", ")
print()
print("max delta = ", delta)
def main():
    f = lambda x: x**2+1
    x = np.linspace(a, b, N)
    plt.plot(x, f(x),'-k')
    x = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6])
    y = np.array([ 1.0, 1.0, 1.077, 1.225, 1.442, 1.723, 2.068, 2.474, 2.943])
    plt.plot(x, y, '-r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(["exact", "Euler"])
    plt.grid()
    plt.show()
main()