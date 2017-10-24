#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  zapytania.py
import sqlite3


def wyniki(cur):
    wyniki = cur.fetchall()  # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))


def kw_c(cur):
    cur.execute("""
        SELECT siedziba, SUM(placa) AS pensje
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial=dzial.id
        GROUP BY siedziba
        ORDER BY pensje ASC
    """)

    wyniki(cur)


def kw_d(cur):
    nazwa = input("Podaj nazwę działu: ")
    siedziba = input("Podaj siedzibę działu: ")
    print(nazwa)
    
    cur.execute("""
        SELECT nazwisko, imie, dzial.id, dzial.nazwa, dzial.siedziba
        FROM pracownicy, dzial
        WHERE pracownicy.id_dzial = dzial.id
        AND dzial.nazwa = ?
        AND siedziba = ?
    """, (nazwa, siedziba))
    
    wyniki = cur.fetchall()  # pobierz wszystkie wiersze od razu
    for row in wyniki:
        print(tuple(row))

def kw_e(cur):
    cur.execute("""
        SELECT datad
        FROM tbOceny
        WHERE strftime('%m', datad) LIKE '10'
    """)
## https://sqlite.org/lang_datefunc.html

def dodaj(cur):
    cur.execute("""
        INSERT INTO tbKlasy
        VALUES (?, ?, ?, ?)
    """, [None, '3C', 2015, 2017])


def aktualizuj(cur):
    cur.execute("""
        UPDATE tbKlasy
        SET klasa = ?
        WHERE idklasy = ?
    """, ['3D', 13])


def usun(cur):
    cur.execute('DELETE FROM tbKlasy WHERE klasa = ? AND roknaboru = ?', ['3B', 2015])

def main(args):
    con = sqlite3.connect('szkola.db')
    cur = con.cursor()  # utworzenie kursora
    con.row_factory = sqlite3.Row

    # dodaj(cur)
    # aktualizuj(cur)
    usun(cur)
    con.commit()
    wyniki(cur.execute('SELECT * FROM tbKlasy'))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
