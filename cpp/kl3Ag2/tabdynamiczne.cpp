/*
 * wskazniki.cpp
 * 
 */


#include <iostream>
#include <iomanip>
#include <cstdlib>


using namespace std;

void wprowadz(float *t, int ile) {
    for(int i = 0; i < ile; i++) {
        cout << "Podaj liczbę: ";
        // cin >> t[i];
        cout << "Adres elementu: " << (t + i) << endl;
        cin >> *(t+i);
    }
}

void drukuj(float *t, int ile) {
    for(int i = 0; i < ile; i++) {
        cout << *(t + i) << endl;
    }
}


int tab1W() {
    cout << "Ile podasz liczb?";
    int ile;
    cin >> ile;

    cout << sizeof(ile) << endl;

    try {
        float *ptab = NULL;
        ptab = new float[ile];  // utworzenie tablicy dynamicznej
        wprowadz(ptab, ile);
        drukuj(ptab, ile);
    } catch(bad_alloc) {
        cout << "Za mało pamięci!";
        return 1;
    }

    return 0;
}

void wypelnij2W(int **tab, int w, int k) {
    srand(time(NULL));
    for(int i = 0; i < w; i++) {
        for(int j = 0; j < k; j++) {
            // tab[0][0]
            tab[i][j] = rand() % 101;
            cout << setw(4) << tab[i][j];
        }
        cout << endl;
    }
}

int tab2W() {
    int w, k, i;
    cout << "Podaj liczbę wierszy i kolumn: ";
    cin >> w >> k;
    int **tab; // deklaracja wskaźnika do wskaźnika
    
    try {
        tab = new int *[w];  // utworzenie tablicy dynamicznej
    } catch(bad_alloc) {
        cout << "Za mało pamięci!";
        return 1;
    }

    for(i = 0; i < w; i++) {
        try {
            tab[i] = new int[k];
        } catch(bad_alloc) {
            cout << "Za mało pamięci!";
            return 1;
        }
    }
    
    // wypełnianie tablicy danymi
    wypelnij2W(tab, w, k);

    return 0;
}


int main(int argc, char **argv)
{
    tab2W();
	return 0;
}

