#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj(tekst, klucz):
    reszta = len(tekst) % klucz
    if reszta:
        tekst += (klucz - reszta) * "."

    szyfrogram = ""
    for i in range(klucz):
        for j in range(int(len(tekst) / klucz)):
            # i = 0, j = 0
            # 0, 5, 10 itd.
            szyfrogram += tekst[i]

    return szyfrogram


def main(args):
    tekst = input("Podaj tekst: ")

    klucz = int(input("Klucz: "))
    while 2 * klucz > len(tekst):
        klucz = int(input("Klucz: "))

    szyfrogram = szyfruj(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
