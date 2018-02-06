#ifndef LISTA_HPP
#define LISTA_HPP

struct ELEMENT{
    int wartosc;
    ELEMENT *nast;  // wskaźnik do następnego elementu listy
};

class Lista {
    private:  // hermetyzacja danych
        ELEMENT *head;
        ELEMENT *tail;
    public:  // interfejs publiczny (API klasy)
        Lista(); //konstruktor
        ~Lista(); //destruktor, posprzątanie po klasie
       void Dodaj(int);
       void Wyswietl();
       bool Usun();
       void Wstaw(int, int);
};

#endif
