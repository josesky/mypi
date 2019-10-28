def test(a, b=-99):
    if a > b:
        return True
    else:
        return False
print(test(11))

def f(a, data=[]):
    data.append(a)
    return data

print(f(3))
print(f(5))



def func(a, b=5, c=10):
    print('a is', a, 'and b is ', b, 'and c is', c)
print(func(11))


def hello(*, name='User'):
    print("Hello", name)
print(hello(name='tianxia'))


import math


def longest_side(a, b):
    return math.sqrt(a*a + b*b)

if __name__=='__main__':
    print(longest_side.__doc__)
    print(longest_side(4, 5))


def high(l):
    return [i.upper() for i in l]

def test(h, l):
    return h(l)

l = ['Python', 'Linux', 'Git']

print(test(high, l))
