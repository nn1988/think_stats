def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

if __name__ == '__main__':
    print('factory of 10 is: %s' % (fact(3)))
