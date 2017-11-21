#!/usr/bin/env python
# -*- coding: utf-8 -*-


def nwd_v1(a, b):
    """Wersja klasyczna"""
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def nwd_v2(a, b):
    """Wersja optymalna"""
    while a > 0:
        a = a % b
        b = b - a
    return b


def main(args):
    a = int(input('Podaj liczbę naturalną: '))
    b = int(input('Podaj liczbę naturalną: '))
    assert nwd_v2(5, 10) == 5
    assert nwd_v2(3, 9) == 3
    assert nwd_v2(33, 11) == 11
    print("NWW({:d}, {:d}) = {:d}".format(a, b, nwd_v2(a, b)))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
