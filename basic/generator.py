# -*- coding: utf-8 -*-
gen = (x * x for x in range(10))
print(gen)

for num in gen :
    print(num)

def fibon(n):
    a = b = 1
    for i in range(n) :
        yield a
        a,b = b,a+b

# for x in fibon(10000) :
#     print(x, end = ' ')

def triangles(n):
    L = [1]
    while True :
        yield L
        L.append(1)
        L = [L[i - 1] + L[i] for i in range(len(L))]

n = 0
for t in triangles(10) :
    print(t)
    n = n + 1
    if n == 10 :
        break