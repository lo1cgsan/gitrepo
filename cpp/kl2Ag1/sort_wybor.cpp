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
    int tmp = a;
    a = b;
    b = tmp;
}


void sort_wyb(int t[], int n) {
    // selection sort
    cout << "-------------- Sortowanie przez wybieranie ------------" << endl;
    int i, j, k;
    for (i = 0; i < n; i++) {
        k = i;
        for (j = i + 1; j < n; j++) {
            if (t[j] < t[k])
                k = j;
        }
        zamien(t[i], t[k]);
    }
}


int main(int argc, char **argv)
{
    //int t[] = {3, 4, 1, 8, 0}
    //t = [3, 4, 1, 8, 0]
    
	const int ile = 10;
    int tab[ile];
    wypelnij(tab, ile, 20);
    drukuj(tab, ile);
    sort_wyb(tab, ile);
    drukuj(tab, ile);
	return 0;
}

