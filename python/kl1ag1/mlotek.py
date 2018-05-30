#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random


def main(args):
    liczba = random.randint(1, 10)  # losowanie liczby <1;10>
    print("Wylosowano:", liczba)
    # pobranie typu użytkownika
    odp = input("Podaj liczbę od 1 do 10: ")
    print("Podałeś:", odp)

    if liczba == int(odp):  # porównanie odpowiedzi z wylosowaną liczbą
        print("Zgadłeś!")
    else:
        print("Spróbuj jeszcze raz!")

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
