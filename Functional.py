import math
from functools import reduce

def add(a, b, f):
    return f(a) + f(b)

def same(x, *fs):
    return [f(x) for f in fs]

def str2num(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        nums = { k:v for k, v in zip([str(x) for x in range(10)], range(10)) }
        return nums[s]
    return reduce(fn, map(char2num, s))

if __name__ == '__main__':
    print(add(-10, 20, abs))
    print(same(2, abs, math.sqrt))
    r = map(lambda x: x * x, range(10))
    print(list(r))

    print(reduce(lambda x,y: x * 10 + y, range(10)))

    print(str2num('123435'))

    languages = ['swIfT', 'jAva', 'pYthON', 'c++']
    print(list(map(lambda x: x[:1].upper() + x[1:].lower(), languages)))

    print(reduce(lambda x, y: x * y, range(1,10)))

    L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
    print(sorted(L, key=lambda x: x[1], reverse=True))
    print(sorted(L, key=lambda x: x[0].lower()))
