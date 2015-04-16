from time import time


def fib(n):
    return 0 if n == 0 else 1 if n == 1 else fib(n-1)+fib(n-2)


def bench(*args):
    t = time()
    result = [fib(i) for i in args]
    td = time() - t
    print("Result ({0} seconds): {1}".format(td, result))