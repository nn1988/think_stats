# -*- coding: utf-8 -*-

import os

def maskMobileNo(mobileNo):
    return mobileNo[:3] + ''.join(['*' for x in range(4)]) + mobileNo[-4:]

if __name__ == '__main__':
    L = list(range(1, 100, 2))
    print(L)

    print(maskMobileNo('123545'))

    for i, value in enumerate(['a','b','c','d']):
        print(i, value)

    print([x * x for x in range(1, 11, 2)])
    print([m + n for m in 'ABC' for n in 'XYZ'])
    print([d for d in os.listdir('.')])

    L1 = ['Hello', 'World', 18, 'Apple', None]
    print([x.upper() for x in L1 if isinstance(x, str)])
