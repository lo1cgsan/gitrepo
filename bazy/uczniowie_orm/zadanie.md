# Baza danych "Uczniowie"

Dysponujesz bazą danych SQLite3 zapisaną w pliku *szkola.db*.
Bazę możesz otworzyć wydając w terminalu polecenie:

```
$~ sqlite3 szkola.db 
```

Polecenia użyteczne w interpreterze SQLite3:

* `.table` – lista tabel;
* `.schema nazwa_tabeli` – definicja SQL tabeli, pokauje nazwy i typy pól, klucze podstawowe i obce;
* `.quit` – wyjście z interpretera SQLite3.

Zadanie rozwiązuj w pliku *uczniowie_orm_kl3ag1_nazwisko.py*.

## Model danych

Na podstawie bazy *szkola.db* zdefiniuj przy użyciu ORM Peewee
model danych, tj. listę klas opisujących obiekty przechowywane
w bazie.

## Kwerendy

Używając systemu ORM Peewee przygotuj kwerendy uruchamiane w osobnych
funkcjach:

a. imiona i nazwiska uczniów klasy 1A;
b. maksymalny wynik z egzaminu humanistycznego;
c. średni wynik z egzaminu z matematyki uczniów z klasy 1A;
d. oceny Doroty Nowak;
e. średnią ocen z fizyki uzyskanych w październiku przez wszystkich uczniów.
