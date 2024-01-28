from math import log
def f(x):
    return x**4+8*x**3-6*x**2-72*x+90
def half(f, a, b, e):
    k = 0
    while (b - a)/2 > e:
        x1 = (a + b)/2 - 0.01
        x2 = (a + b)/2 + 0.01
        if f(x1)>f(x2):
            a = x1
        else:
            b = x2
        print(k, " iteration")
        print("x1:", x1,"x2:", x2)
        print("f(x1):", f(x1),"f(x2):", f(x2))
        k += 1
    x = (a+b)/2
    return(x, k)
a = 1.5
b = 2
e = 0.05
x, k = half(f, a, b, e)
print("Answer:", x,"f(x):", f(x), "\nfound in", k, "iterations")