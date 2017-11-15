#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  potega.py
#  a0 = 1
#  a1 = a dla a w N+
#  an = a * ... * a (n czynników) dla a w N+ - {0, 1}


def potega_it(podst, wykladnik):
    wynik = 1
    for i in range(0, wykladnik):
        wynik = wynik * podst
    return wynik


def main(args):
    """Funkcja główna"""
    a = int(input('Podaj liczbę naturalną: '))
    n = int(input('Podaj wykładnik: '))
    assert type(a) == int
    assert type(n) == int
    assert potega_it(a, 0) == 1
    assert potega_it(a, 1) == a
    assert potega_it(2, 2) == 4
    assert potega_it(3, 2) == 9
    print('Potega dla {:d} do {:d}: {:d}'.format(a, n, potega_it(a, n)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
