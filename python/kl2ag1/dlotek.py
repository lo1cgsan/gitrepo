#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def losuj(ileliczb, maksliczb):
    liczby = []  # pusta lista

    ile = 0  # ilość unikalnych liczb
    # for i in range(ileliczb):
    while ile < ileliczb:
        liczba = random.randint(0, maksliczb)
        if liczby.count(liczba) == 0:
            liczby.append(liczba)
            ile += 1

    print(liczby)
    return liczby


def main(args):
    ileliczb = int(input('Ile liczb chcesz zgadywać?'))
    maksliczb = int(input('Maksymalna losowana liczba: '))

    liczby = losuj(ileliczb, maksliczb)

    # pobieranie typów użytkownika
    typy = set()  # pusty zbiór
    for i in random(ileliczb):
        typ = input('Podaj typ: ')
        typy.add(typ)

    print(typy)


    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
