import numpy as np
A = np.array([[3, -2, 5], [7, 4, -8], [5, -3, -4]], float)
print("A : ")
print(A)
b = np.array([[7], [3], [-12]], float)
print("b : ")
print(b)
a = np.hstack([A, b.reshape(-1, 1)])
print("a : ")
print(a)
n = len(b)
x = np.zeros((n,1))
for i in range(0, n):
    for j in range(0, n + 1):
        print("a[", i, "][", j, "] = ", a[i][j])
for i in range(0,n):
    if abs(a[i][i]==0.0):
        max = abs(a[i][i]) + i
        r = i
        for k in range(i+1,n):
            if abs(a[k][i])>max:
                max = abs(a[k][i])
                r = k
        for k in range(i, n+1):
            m = a[r][k]
            a[r][k] = a[i][k]
            a[i][k] = m
        for j in range(i + 1, n):
            c = -a[j][i]/a[i][i]
            for l in range(i, n+1):
                a[j][l] += c*a[i][l]
    if abs(a[i][i]!=0.0):
        for j in range(i + 1, n):
            c = -a[j][i]/a[i][i]
            for k in range(i, n+1):
                a[j][k] += c*a[i][k]
x[n-1] = a[n-1][n]/a[n-1][n-1]
for i in range(n - 1, -1, -1):
    x[i] = a[i][n] / a[i][i]
    c = a[i]
    for j in range(i - 1, -1, -1):
        a[j][n]=a[j][n]-a[j][i]*x[i]
for i in range(n):
    print("x",i+1,"=" , *x[i])