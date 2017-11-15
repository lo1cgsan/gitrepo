#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  silnia.py
#  n! = 1 dla n={0, 1}
#  n! = 1 * ... * n dla N+ - {1}


def silnia_it(n):
    wynik = 1
    for i in range(2, n + 1):
        wynik = wynik * i
    return wynik


def main(args):
    """Funkcja główna"""
    n = int(input('Podaj liczbę naturalną: '))
    assert type(n) == int
    assert silnia_it(0) == 1
    assert silnia_it(1) == 1
    assert silnia_it(2) == 2
    assert silnia_it(3) == 6
    print('Silnia dla {:d}: {:d}'.format(n, silnia_it(n)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
