import sys


input = sys.stdin.readline
n, k = map(int, input().split())
p = 1000000007


def get_factorial(n):
    if n == 0:
        return 1
    else:
        for i in range(1, n):
            n = n * i % p
        return n


def multi(a, n):
    if n == 1:
        return a % p
    else:
        if n % 2 == 0:
            return ((multi(a, n//2)) ** 2) % p
        else:
            return (((multi(a, n//2)) ** 2) * a) % p


a = get_factorial(n) % p
b = multi(get_factorial(k), p-2) % p
c = multi(get_factorial(n-k), p-2) % p


print(a * b * c % p)
