import numpy as np
f1 = lambda x1, x2, x3: (2*x2-5*x3+7)/3
f2 = lambda x1, x2, x3: (8*x3-4*x2+3)/7
f3 = lambda x1, x2, x3: (3*x2+4*x3-12)/5
x1_0 = 0
x2_0 = 0
x3_0 = 0
k = 0
N = 4
e = 1*10**(-12)
print('\nk\t  x1\t  x2\t  x3\n')
while (k<N):
    new_x1 = f1(x1_0,x2_0,x3_0)
    new_x2 = f2(x1_0,x2_0,x3_0)
    new_x3 = f3(x1_0,x2_0,x3_0)
    print('%d\t%0.4f\t%0.4f\t%0.4f\n' % (k+1, new_x1, new_x2, new_x3))
    e1 = abs(x1_0 - new_x1);
    e2 = abs(x2_0 - new_x2);
    e3 = abs(x3_0 - new_x3);
    error = np.array([e1,e2,e3])
    k += 1
    x1_0 = new_x1
    x2_0 = new_x2
    x3_0 = new_x3
    if (max(error) < e):
        break
print('\nSolution: x1=%0.3f, x2=%0.3f and x3 = %0.3f\n' % (new_x1, new_x2, new_x3))