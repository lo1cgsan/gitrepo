#ifndef DRZEWO_HPP
#define DRZEWO_HPP

struct Wezel {
    int wartosc;
    Wezel *lewy;
    Wezel *prawy;
} *korzen = NULL; // definicja struktury i utworzenie wskaźnika korzen

class Drzewo {
    private:  // hermetyzacja danych
        Wezel *korzen;
    public:  // interfejs publiczny - API klasy
        Drzewo(); //konstruktor
        Wezel* stworzWezel(int wartosc);
        void dodajWezel(Wezel *wezel, int wartosc);
        void wyswietlRosnoco(Wezel *wezel);
};

#endif
