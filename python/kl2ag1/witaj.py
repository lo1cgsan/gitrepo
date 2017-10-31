#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# osoba = "Adam Słodowy"
# osoba = 'Adam Słodowy'
osoba = input('Jak się nazywasz? ')
wiek = input('Ile masz lat? ')
print('Witaj,', osoba, '!')
print('Urodziłeś się w ', 2017 - int(wiek))
rok_pythona = 1991
wiek_pythona = 2017 - rok_pythona

if wiek_pythona > int(wiek):
    print('Jestem starszy!')
elif wiek_pythona < int(wiek):
    print('Jestem młodszy!')
else:
    print('Mamy tyle samo lat!')
