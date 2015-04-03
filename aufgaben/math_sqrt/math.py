from math import sqrt
from math import factorial


def guess_sqrt(number, iterations=5):
    x = number
    for i in range(0,iterations):
        x = (x + number / x) / 2
    return x, sqrt(number), x-sqrt(number)


def fac_rec(number):
    if number == 1:
        return number
    return fac_rec(number - 1) * number


def fac_iter(number):
    res = 1
    for i in range(2, number+1):
        res = res * i
    return res


# Test
print("sqrt(10) = " + guess_sqrt(10))
# this is quite fast
print("42000! = " + factorial(42000))
# this isn't
print("42000! = " + fac_iter(42000))
# Python's default maximum recursion depth is 1000.
# print("42000! = " + fac_rec(42000))