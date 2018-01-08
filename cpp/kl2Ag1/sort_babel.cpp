/*
 * sort_wybor.cpp
 *
 * Copyright 2017  <>
 */

#include <iostream>

using namespace std;

void wypelnij(int t[], int n, int maks) {
    srand(time(NULL)); // inicjacja generatora liczb pseudolosowych
    for (int i = 0; i < n; i++) {
        t[i] = 1 + rand() % maks; // losowanie liczb całkowitych <0; maks>
    }
}

void drukuj(int t[], int n) {
    for (int i = 0; i < n; i++) {
        cout << t[i] << " ";
    }
    cout << endl;
}


void zamien(int &a, int &b) {
}


void sort_wyb(int t[], int n) {
    // bubble sort
    cout << "-------------- Sortowanie przez bąbelkowe ------------" << endl;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n - 1sudo mc
        ; j++) {
            if (tab[j] > tab[j+1])
                zamien(tab[j], tab[j+1]);
        }
    }
}


int main(int argc, char **argv)
{
	const int ile = 10;
    int tab[ile];
    wypelnij(tab, ile, 20);
    drukuj(tab, ile);
    sort_babel(tab, ile);
    drukuj(tab, ile);
	return 0;
}

