#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib_iter(n):
    """Wylicza n-ty wyraz ciągu Fionacciego
       F(0) = 0
       F(1) = 1
       F(n) = F(n-2) + F(n-1) dla n > 1
    """
    a, b = (0, 1)
    for i in range(1, n - 1):
        a = b
        b = a + b
    if n > 0:
        return b
    else:
        return a


def main(args):
    n = int(input('Podaj wyraz ciągu: '))
    assert fib_iter(0) == 0
    assert fib_iter(1) == 1
    assert fib_iter(2) == 1
    assert fib_iter(3) == 2
    assert fib_iter(4) == 3
    assert fib_iter(5) == 5
    print("Wyraz {:d} = {:d}".format(n, fib_iter(n)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
