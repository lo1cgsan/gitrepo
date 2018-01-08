#!/usr/bin/env python
# -*- coding: utf-8 -*-

from math import floor


def wyszukiwanie_liniowe(l, e):
    for i in range(0, len(l)):
        if l[i] == e:
            return i
    return -1


def wyszukiwanie_binarne(l, e):
    lewy, prawy = 0, len(l) - 1
    while lewy < prawy:
        srodek = floor((lewy + prawy) / 2)
        print(srodek)
        if e <= l[srodek]:
            prawy = srodek
        else:
            lewy = srodek + 1
    return -1


def main(args):
    lista = [4, 3, 7, 0, 2, 3, 1, 9, -4]
    pass

    el =
     13
    print(wyszukiwanie_liniowe(lista, el))
    print(wyszukiwanie_binarne(lista, el))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
