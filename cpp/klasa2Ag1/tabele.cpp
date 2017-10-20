/*
 * tabele.cpp
 */


#include <iostream>

using namespace std;


int main(int argc, char **argv)
{
    int liczby[10];
    int i = 0;
    int suma = 0;
    int licznik = 0;
    
    for (i = 0; i < 10; i++) {
        cout << "Podaj liczbę: ";
        cin >> liczby[i];
    }

    for (i = 0; i < 10; i++) {
        //cout << liczby[i] << " ";
        suma += liczby[i];
        if (liczby[i] % 2 == 0)
            licznik++;
    }
    
    cout << "Suma liczb: " << suma << endl;

    return 0;
}

