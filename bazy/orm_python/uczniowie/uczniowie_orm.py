#!/usr/bin/env python
# -*- coding: utf-8 -*-

from peewee import *
from dane import *

baza_plik = "szkola.db"
baza = SqliteDatabase(baza_plik)  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza


class Klasa(BazaModel):
    nazwa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)

    def __str__(self):
        return self.nazwa


class Przedmiot(BazaModel):
    nazwa = CharField(null=False)
    imien = CharField(null=False)
    nazwiskon = CharField(null=False)
    plecn = IntegerField()


class Uczen(BazaModel):
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField()
    klasa = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = IntegerField()
    egzmat = IntegerField()
    egzjez = IntegerField()


class Ocena(BazaModel):
    datad = DateField()
    uczen = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = DecimalField(decimal_places=2)


def dodaj_dane():
    baza.create_tables([Klasa, Przedmiot, Uczen, Ocena], True)

    klasa = dane_z_pliku('tbKlasy.csv', ',')
    klasa = [dict(zip(['nazwa', 'rok_naboru', 'rok_matury'], rekord)) for rekord in klasa]

    przedmiot = dane_z_pliku('tbPrzedmioty.csv', ',')
    przedmiot = [dict(zip(['nazwa', 'imien', 'nazwiskon', 'plecn'], rekord)) for rekord in przedmiot]

    uczen = dane_z_pliku('tbUczniowie.csv', ',')
    uczen = [dict(zip(['imie', 'nazwisko', 'plec', 'klasa', 'egzhum', 'egzmat', 'egzjez'], rekord)) for rekord in uczen]

    ocena = dane_z_pliku('tbOceny.csv', ',')
    ocena = [dict(zip(['datad', 'uczen', 'przedmiot', 'ocena'], rekord)) for rekord in ocena]

    with baza.atomic():
        Klasa.insert_many(klasa).execute()
        Przedmiot.insert_many(przedmiot).execute()
        Uczen.insert_many(uczen).execute()
        Ocena.insert_many(ocena).execute()

    baza.commit()  # zatwierdzenie operacji


def kwerenda_a():
    query = (Uczen
             .select(Uczen.imie, Uczen.nazwisko, Uczen.klasa)
             .join(Klasa)
             .where(Klasa.nazwa == "1A")
            )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.klasa)


def main(args):
    baza.connect()  # nawiązujemy połączenie z bazą
    # dodaj_dane()
    kwerenda_a()
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
