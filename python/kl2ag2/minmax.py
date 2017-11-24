#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint


def minimum(lista):
    min = lista[0]
    for i in lista:
        if i < min:
            min = i
    return min


def maksimum(lista):
    max = lista[0]
    for i in lista:
        if i > max:
            max = i
    return max


def minmax(lista):
    lmin = []
    lmax = []
    i = 0
    for i in range(int(len(lista) / 2)):
        if lista[i] > lista[i + 1]:
            lmin.append(lista[i + 1])
            lmax.append(lista[i])
        else:
            lmin.append(lista[i])
            lmax.append(lista[i + 1])


def losuj(ile, zakres):
    lista = []
    for i in range(ile):
        lista.append(randint(0, zakres))
    return lista


def main(args):
    ile = 20
    zakres = 50
    lista = losuj(ile, zakres)
    assert minimum([7, 4, 9, 1, 3, 0]) == 0
    assert maksimum([7, 4, 9, 1, 3, 0]) == 9
    print(lista)
    print("Minimum: ", minimum(lista))
    print("Maksimum: ", maksimum(lista))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
