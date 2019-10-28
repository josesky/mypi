f = abs

def add(x, y, f):
    return f(x) + f(y)

print(add(5, -11, f))

L = []
for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
    L.append(f(n))
print(L)

print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(r))

print(sorted([33, 11, 33, 88, -10]))


def lazy_sum(*args):
    def sum():

        ax = 0
        for i in args:
            ax = ax + i
        return ax
    return sum


f = lazy_sum(1, 3, 5, 7, 9)
print(f())

print(lazy_sum.__name__)

def int2(x, base=2):
    return int(x, base)
print(int2('10'))


import functools
int2 = functools.partial(int, base=10)
print(int2('1000'))