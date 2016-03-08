# -*- encoding: utf-8 -*-

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

def triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]

if __name__ == '__main__':
    g = (x * x for x in range(1, 11, 3))
    L = []
    while True:
        try:
            L.append(next(g))
        except StopIteration as e:
            print('encountered StopIteration exception.')
            break
    print(L)

    f = fib(4)
    print(next(f), next(f), next(f), next(f))

    g = triangles()
    for i in range(10):
        print(next(g))

    print(next(zip([0] + [1], [1] + [0])))
