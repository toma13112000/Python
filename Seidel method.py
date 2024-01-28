import numpy as np
from numpy.linalg import norm
from numpy.linalg import norm
A = np.array([[0.0, 1.2, 2.1, 0.9], [1.2, 21.2, 1.5, 2.5], [2.1, 1.5, 19.8, 1.3], [0.9, 2.5, 1.3, 32.1]], float)
print("A : ")
print(A)
b = np.array([21.70, 27.46, 28.76, 49.72], float)
print("b: ")
print(b)
n = len(b)
x0 = np.zeros(n)
e = 0.001
k = 0

while True:
    x = np.zeros_like(b)
    for i in range(n):
        sum1 = 0
        sum2 = 0
        if (A[i][i] == 0.0):
            for l in range(n):
                D = A[i][i]
                A[i][i] = A[i][l]
                A[i][l] = D
        for j in range(i):
            sum1 += A[i][j] * x[j]
        for j in range(i+1,n):
            sum2 += A[i][j] * x0[j]
        x[i] = 1/A[i][i]*(b[i]-sum1-sum2)
        if x[i] == x[i-1]:
            break
        error = abs(norm(x)-norm(x0))
        if (error < e):
            break
    if np.allclose(x0, x, e, 10**(-12)):
        break
    k = k+1
    print("k=", k)
    for i in range(n):
        x0[i] = x[i]
    for i in range(n):
        print("x",i+1,"=",x[i])
j = np.linalg.solve(A,b)
print("Exact solution: ")
for i in range(n):
    print("x",i+1,"=",j[i])
print("error = ",error)