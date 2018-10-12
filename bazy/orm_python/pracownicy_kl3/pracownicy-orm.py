#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pracownicy-orm.py

from peewee import *
from dane import *  # import funkcji z pliku dane.py

baza_plik = 'pracownicy.sqlite3'
baza = SqliteDatabase(baza_plik)

class BazaModel(Model):
    class Meta:
        database = baza
        

class Premia(BazaModel):
    id = CharField(primary_key = True)
    premia = DecimalField()


class Dzial(BazaModel):
    id = IntegerField(primary_key = True)
    nazwa = CharField()
    siedziba = CharField()


class Pracownik(BazaModel):
    id = CharField(primary_key = True)
    nazwisko = CharField()
    imie = CharField()
    stanowisko = ForeignKeyField(Premia, related_name='pracownicy')
    data_zatr = CharField()
    placa = DecimalField(decimal_places=2)
    id_dzial = ForeignKeyField(Dzial, related_name='pracownicy')
    premia = DecimalField(decimal_places=2, default=0)

baza.connect()
baza.create_tables([Premia, Dzial, Pracownik], True)

premia = dane_z_pliku('premia.txt')
premia = wyczysc_dane(premia, 1)

dzial = dane_z_pliku('dział.txt')

pracownicy = dane_z_pliku('pracownicy.txt')
pracownicy = wyczysc_dane(pracownicy, 5)
pracownicy = wstaw_premie(pracownicy, dict(premia))

premia = [dict(zip(Premia._meta.sorted_field_names, row)) for row in premia]

dzial = [dict(zip(Dzial._meta.sorted_field_names, row)) for row in dzial]

pracownicy = [dict(zip(Pracownik._meta.sorted_field_names, row)) for row in pracownicy]


#~dane = [
    #~{'id': 'Kierowca', 'premia': '0.2'},
    #~{'id': 'Dyrektor', 'premia': '0.7'},
    #~{'id': 'Inżynier', 'premia': '0.4'}
#~]
#~for rekord in dane:
#~Premia.create(id=rekord['id'], premia=rekord['premia'])

# tworzenie instancji klasy
#~obiekt = Premia(id = "Sprzątaczka", premia = 0.2)
#~print(obiekt.id, obiekt.premia)
#~obiekt.save()

#~obiekt = Premia(id = "Sekretarka", premia = 0.35)
#~print(obiekt.id, obiekt.premia)
#~obiekt.save()




