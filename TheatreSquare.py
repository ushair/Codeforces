from math import ceil
n , m , a = map(int, input().split())
X = ceil(n / a)
Y = ceil(m / a)
print(int(X * Y))
