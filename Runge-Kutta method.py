import numpy as np
import sympy as sp
from math import exp
from sympy import pprint, dsolve, diff
from scipy.integrate import odeint
import matplotlib.pyplot as plt
a = 1; b = 2; N = 7
h = 0.1
print("h =", h)
y0 = 1
print("xi", end=":")
x = np.linspace(a, b, N)
for i in range(0, N-1):
    xi = a + h*i
    print(round(xi,2), end= ", ")
print()
print("Exact solution: ", end="")
for i in range (0, N-1):
    xi = a+h*i
    yi = 1 + xi**2
    print(round(yi,3), end=", ")
print()
y0 = 1
x0 = 1
f = lambda y,x: (-y**2 + 0.35/(x**2))
u = odeint(f, y0, x)
print("Midpoint : ", end="")
for i in range(0, N - 1):
    x[i] = a + h * i
    u = u.flatten()
    midpoint = u[i] + h*0.5*f(u[i],x[i])
    print(np.round(midpoint,3), end=", ")
print()
print("Numerical solution : ",end="")
for i in range(0, N - 1):
    x[i] = a + h * i
    u[i + 1] = f(u[i]+h*0.5*f(u[i],x[i]), x[i]+h*0.5) * h + u[i]
    u = u.flatten()
    print(np.round(u[i],3), end=", ")
print()
print("△i : ", end = "")
for i in range(0, N-1):
    x[i] = a + h * i
    yi = 1 + (a + h * i) ** 2
    u[i + 1] = f(u[i]+h*0.5*f(u[i],x[i]), x[i]+h*0.5) * h + u[i]
    delta = abs(u[i] - yi)
    print(round(delta,3), end =", ")
print()
print("max delta = ", delta)
def graph():
    t = lambda n: n ** 2 + 1
    n = np.linspace(a, b, N)
    plt.plot(n, t(n), 'k')
    x = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6])
    y = np.array([1.0, 1.04, 1.158, 1.357, 1.634, 1.991, 2.427, 2.942, 3.536])
    plt.plot(x, y, 'r')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(["exact", "Range-Kutta"])
    plt.grid()
    plt.show()
graph()