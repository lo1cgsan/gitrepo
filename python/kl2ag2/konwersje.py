#!/usr/bin/env python
# -*- coding: utf-8 -*-


def dec2other(liczba10, podstawa):
    """Konwersja liczby dziesiętnej na system o podanej podstawie"""
    liczba = []  # pusta lista do zapamiętywania reszt
    while liczba10 != 0:
        reszta = liczba10 % podstawa  # obliczanie reszt z dzielenia
        if reszta > 9:  # wykorzystanie kodu ASCII
            reszta = chr(reszta + 55)
        liczba.append(str(reszta))
        liczba10 = int(liczba10 / podstawa)  # uwaga
    liczba.reverse()  # odwrócenie kolejności elementów
    return "".join(liczba)


def zamiana1():
    """Pobranie danych wejściowych"""
    liczba = int(input("Podaj liczbę: "))
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    print("Wynik konwersji: {}(10) = {}({})".format(
        liczba, dec2other(liczba, podstawa), podstawa))


def other2dec(liczba, podstawa):
    """Zamiana podanej liczby na system dziesiętny"""
    #  123(7) = 1 * 7^2 + 2 * 7^1 + 3
    liczba10 = 0
    potega = len(liczba) - 1
    for cyfra in liczba:
        # pass
        liczba10 += int(cyfra) * (podstawa ** potega)  # 1 * 7 ** 2
        potega -= 1

    return liczba10


def zamiana2():
    """Pobranie danych wejściowych"""
    liczba = input("Podaj liczbę: ")  # ABC
    podstawa = 0
    while podstawa < 2 or podstawa > 16:
        podstawa = int(input("Podaj podstawę: "))
    # pass

    print("Wynik konwersji: {}({}) = {}(10)".format(
        liczba, podstawa, other2dec(liczba, podstawa)))



def main(args):
    print("Zamiana liczby dziesiętnej na liczbę o podanej podstawie "
          "<2;16> lub odwrotnie.")
    zamiana1()
    zamiana2()
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
