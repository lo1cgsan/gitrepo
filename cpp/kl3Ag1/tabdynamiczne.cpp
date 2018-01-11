/*
 * tabdynamiczne.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>

using namespace std;

void wprowadzDane(int *t, int ile) {
    for(int i=0; i < ile; i++) {
        cout << "Podaj liczbę: ";
        //cin >> t[i];
        cout << "Adres komórki: " << (t + i) << endl;
        cin >> *(t + i);
    }
}

int tab1W() {
    // tworzenie 1-wymiarowej tablicy dynamicznej
    int ile = 0;
    cout << "Ile liczb podasz? " << endl;
    cin >> ile;
    
    try {
        int *tab;
        tab = new int[ile];
        wprowadzDane(tab, ile);
    } catch(bad_alloc) {
        cout << "Za mało pamięci!";
        return 1;
    }
    
    return 0;
}

int main(int argc, char **argv)
{
	tab1W();
	return 0;
}

