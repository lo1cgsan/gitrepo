/*
 * tabele.cpp
 */


#include <iostream>

using namespace std;

void ile5(int tab[], int ile) {
    int i;
    int licznik = 0;
    int parzyste = 0;
    for (i = 0; i < ile; i++) {
        if (tab[i] % 5 == 0)
            licznik5++;
        if (tab[i] % 2 == 0)
            parzyste++;
    }
    cout << "Podzielnych przez 5: " << licznik5 << endl;
     cout << "Parzystych: " << parzyste << endl;
}

void pobierzLiczby(int tab[], int ile) {
    int i = 0;
    for (i = 0; i < ile; i++) {
        cout << "Podaj liczbę: ";
        cin >> tab[i];
    }
}

void najmniejsza(int tab[], int ile) {
// funkcja znajduje i drukuje najmniejszą
// liczbę z tabeli
    int min = tab[0];
    int i = 0;
    for (i = 1; i < ile; i++) {
        if (min > tab[i])
            min = tab[i];
    }
    cout << "Najmniejsza: " << min << endl;
}

int main(int argc, char **argv)
{
    int rozmiar = 0;
    cout << "Ile liczb podasz: ";
    cin >> rozmiar;
    
    int liczby[rozmiar];
    
    pobierzLiczby(liczby, rozmiar);
    najmniejsza(liczby, rozmiar);

    return 0;
}

