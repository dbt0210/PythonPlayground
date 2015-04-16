import matlib


def memoize(f):
    cache = {}

    def wrapper(arg):
        if arg not in cache:
            cache[arg] = f(arg)
        return cache[arg]

    return wrapper

# first benchmark
matlib.bench(24)
# memoize fib()
matlib.fib = memoize(matlib.fib)
# second benchmark
matlib.bench(*range(100))