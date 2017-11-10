#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  dane.py
import csv


def dane_z_pliku(plik, delimiter):
    dane = []  # pusta lista
    with open(plik, newline='', encoding='utf-8') as plikcsv:
        tresc = csv.reader(plikcsv, delimiter=delimiter)
        for rekord in tresc:
            dane.append(rekord)
    return dane


def wyczysc_dane(dane, pole):
    for i, rekord in enumerate(dane):
        element = rekord[pole]
        element = element.replace(" ", "")
        element = element.replace(",", ".")
        element = element.replace("zł", "")
        rekord[pole] = element
        dane[i] = rekord
    return dane


def main(args):
    klasa = dane_z_pliku('tbKlasy.csv', ',')
    # print(klasa)

    przedmiot = dane_z_pliku('tbPrzedmioty.csv', ',')
    # print(przedmiot)

    uczen = dane_z_pliku('tbUczniowie.csv', ',')
    # print(uczen)
    ocena = dane_z_pliku('tbOceny.csv', ',')
    print(ocena)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
