/*
 * ulamek.cpp
 * 
 * Copyright 2018  <>
 */


#include <iostream>

using namespace std;

class Ulamek {
private:
    int licznik;
    int mianownik;
public:
    Ulamek (int, int);  // deklaracja konstruktora obiektu
    void zapisz(int, int);  // tylko deklaracja!!!
    void wypisz() {
        cout << licznik << "/" << mianownik;
    }
    int get_l() {
        return licznik;
    }
    int get_m() {
        return mianownik;
    }
    void skracaj() {
        // użyj algorytmu euklidesa w wersji optymalnej
        ;
    }
};  // koniec definicji klasy!!!

void Ulamek::zapisz(int l, int m) {  // definicja metody
    licznik = l;
    if (m != 0) mianownik = m;
    else {
        cout << "Mianownik nie może być zerem!" << endl;
        exit(1);
    }
}

Ulamek::Ulamek(int l, int m) {  // definicja konstruktora
    licznik = l;
    if (m != 0) mianownik = m;
    else {
        cout << "Mianownik nie może być zerem!" << endl;
        exit(1);
    }
}

int main(int argc, char **argv)
{
	Ulamek ul1(4, 5);
    Ulamek ul2(1, 7);
    //ul1.zapisz(4, 5);
    //ul2.zapisz(1, 7);
    cout << "1 ułamek: ";
    ul1.wypisz();
    cout << endl << "2 ułamek: ";
    ul2.wypisz();
    cout << endl;
    cout << ul1.get_l() << endl;
    cout << ul1.get_m() << endl;
    
	return 0;
}

