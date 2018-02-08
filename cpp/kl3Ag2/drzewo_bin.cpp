/*
 * drzewo_bin.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>

using namespace std;

struct WEZEL{
    int wartosc;
    WEZEL *lewy;  // wskaźnik do lewego potomka
    WEZEL *prawy;  // wskaźnik do prawy potomka
} *korzen = NULL;  // definicja struktury i utworzenie wskaźnika korzenia


// funkcja tworzy nowy węzeł i zwraca wskaźnik do niego
WEZEL* stworzWezel(int wartosc) {
    WEZEL *nowyWezel = new WEZEL;
    nowyWezel->wartosc = wartosc;
    nowyWezel->lewy = NULL;
    nowyWezel->prawy = NULL;
    
    return nowyWezel;
}

// funkcja dodaje nowy węzeł do drzewa
void dodajWezel(WEZEL *wezel, int wartosc) {
    if (korzen == NULL) { // drzewo jest puste
        korzen = stworzWezel(wartosc);
    } else { // drzewo nie jest puste!
        if (wartosc < wezel->wartosc) { // wstawiamy do lewego poddrzewa
            if (wezel->lewy != NULL) {
                dodajWezel(wezel->lewy, wartosc); // wywołanie rekurencyjne
            } else { // lewy potomek nie istnieje
                wezel->lewy = stworzWezel(wartosc); // tworzymy nowy wezel
            }
        } else { // wstawiamy do prawego poddrzewa
            if (wezel->prawy != NULL) {
                dodajWezel(wezel->prawy, wartosc); // wywołanie rekurencyjne
            } else { // prawy potomek nie istnieje
                wezel->prawy = stworzWezel(wartosc); // tworzymy nowy wezel
            }
        }
    }
}

int main(int argc, char **argv)
{
	
	return 0;
}

