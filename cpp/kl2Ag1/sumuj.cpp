/*
 * sumuj.cpp
 * Program pobiera i sumuje 10 liczb, wynik drukuje na ekranie.
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i;
    int suma = 0;
    int liczba = 0;

    for (i = 0; i < 10; i++)
    {
        cout << "Podaj liczbę: ";
        cin >> liczba;
        suma += liczba;
    }
    cout << "Suma liczb: " << suma << endl;

    return 0;
}

