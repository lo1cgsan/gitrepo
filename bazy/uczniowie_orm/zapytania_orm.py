# -*- coding: utf-8 -*-

from peewee import *

baza_plik = "szkola.db"
baza = SqliteDatabase(baza_plik)  # ':memory:'


class BazaModel(Model):  # klasa bazowa
    class Meta:
        database = baza


class Klasa(BazaModel):
    klasa = CharField(null=False)
    rok_naboru = IntegerField(null=False)
    rok_matury = IntegerField(null=False)


class Przedmiot(BazaModel):
    przedmiot = CharField(null=False)
    imien = CharField(null=False)
    nazwiskon = CharField(null=False)
    plecn = IntegerField()

class Uczen(BazaModel):
    id = IntegerField(primary_key=True)
    imie = CharField(null=False)
    nazwisko = CharField(null=False)
    plec = IntegerField()
    klasaid = ForeignKeyField(Klasa, related_name='uczniowie')
    egzhum = IntegerField()
    egzmat = IntegerField()
    egzjez = IntegerField()

class Ocena(BazaModel):
    id = IntegerField(primary_key=True)
    datad = DateField()
    uczen_id = ForeignKeyField(Uczen, related_name='oceny')
    przedmiot_id = ForeignKeyField(Przedmiot, related_name='oceny')
    ocena = DecimalField(decimal_places=2)

baza.connect()  # nawiązujemy połączenie z bazą

def kwerenda_a():
    query = (Uczen
             .select(Uczen.imie, Uczen.nazwisko)
             .join(Klasa)
             .where(Klasa.klasa == "1A")
            )

    for obj in query:
        print(obj.imie, obj.nazwisko, obj.klasaid.klasa)

kwerenda_a()
