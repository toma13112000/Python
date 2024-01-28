import numpy as np
from math import fabs
n = int(input("Enter matrix length: "))
A = np.zeros((n,n), float)
b = np.zeros(n, float)
N = int(input("Enter number of iterations: "))
e = float(input("Enter accuracy of calculations: "))
print("Enter coefficients of an equation: ")
for i in range(n):
    for j in range(n):
        A[i][j] = float(input( 'A['+str(i+1)+']['+ str(j+1)+']='))
print("A:")
print(A)
print("Enter column vector's values: ")
for i in range(n):
    b[i] = float(input( 'b['+str(i+1)+']='))
print("b:")
print(b)
x0 = np.zeros(n)
k = 0
while (k<N):
    x = np.copy(x0)
    for i in range(n):
        for i in range(n):
            sum = 0
            if (A[i][i] == 0.0):
                for k in range(n):
                    D = A[i][i]
                    A[i][i] = A[i][k]
                    A[i][k] = D
                    print(A)
        s1 = sum(A[i][j]*x[j] for j in range (i))
        s2 = sum(A[i][j]*x0[j] for j in range (i+1,n))
        x[i] = 1/A[i][i]*(b[i]-s1 - s2)
        error = np.sqrt(sum((x[i]-x0[i])**2))
        if (error < e):
            break
    k = k+1
    print("k=", k)
    for i in range(n):
        x0 = x.copy()
    for i in range(n):
        print("x",i+1,"=",np.round(x[i],3))
print(error)