/*
 * sumuj.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int i; // zmienna iteracyjna
    int suma = 0; // suma kolejnych liczb
    int liczba = 0;  // liczba wprowadzana
    int ile_razy = 0;
    
    cout << "Ile liczb podasz? ";
    cin >> ile_razy;
    
    for (i = 0; i < ile_razy; i++)
    {
        cout << "Podaj liczbę: " << endl;
        cin >> liczba;
        // suma = suma + liczba;
        suma += liczba;
    }
    
    cout << "Suma: " << suma << endl;
    
    return 0;
}

