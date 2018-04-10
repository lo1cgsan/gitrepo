#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pylab as plt


def fun(x):
    # return 2 * x ** 2 - 4 * x
    return 2 * x - 3


def wykres(a, b, d):
    lx = np.arange(a, b + d, d)
    ly = [fun(i) for i in lx]
    plt.plot(lx, ly, "o:", color="g")
    plt.grid()
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.axvline(x=a, color='y')
    plt.axvline(x=b, color='y')
    plt.show()


def m_zerowe(a, b, dokladnosc):
    c = (a + b) / 2
    while b - a > dokladnosc and fun(a) is not 0 and fun(b) is not 0:
        c = (a + b) / 2
        if fun(a) * fun(c) < 0:
            b = c
        else:
            a = c

    if fun(a) == 0:
        return a
    if fun(b) == 0:
        return b
    return c


def main(args):
    lewy = prawy = 1
    while fun(lewy) * fun(prawy) > 0 or prawy < lewy:
        lewy = float(input("Podaj lewy kraniec przedziału: "))
        prawy = float(input("Podaj prawy kraniec przedziału: "))
    d = float(input("Podaj dokładność: "))
    wynik = m_zerowe(lewy, prawy, d)
    print("Przybliżona wartość m. zerowego: {:.8f}".format(wynik))
    wykres(lewy, prawy, d)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
