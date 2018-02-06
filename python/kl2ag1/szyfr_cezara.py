#!/usr/bin/env python
# -*- coding: utf-8 -*-


def szyfruj_cezar(tekst, klucz):
    klucz = klucz % 26
    szyfrogram = ""
    for znak in tekst:
        # znak = znak.upper()
        ascii = ord(znak) + klucz  # kod ascii litery zastępującej
        if ascii > 90:
            ascii -= 26
        szyfrogram += chr(ascii)
    return szyfrogram


def deszyfruj(szyfrogram, klucz):
    tekst = ""
    pass
    return tekst


# obsłużyć spacje
# obsłużyć małe i duże litery

def main(args):
    tekst = input("Podaj tekst: ")
    klucz = int(input("Klucz: "))

    szyfrogram = szyfruj_cezar(tekst, klucz)
    print(szyfrogram)
    print(deszyfruj(szyfrogram, klucz))

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
