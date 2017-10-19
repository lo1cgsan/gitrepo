/*
 * funkcje.cpp
 */

#include <iostream>

using namespace std;

void dodaj(int a, int b)
{
    cout << "Suma: " << a +b << endl;
}

int odejmij(int l1, int l2)
{
    return l1 - l2;
}

int dziel(int l1, int l2)
{
    if (l2 == 0) {
        cout << "Nie dziel przez 0!" << endl;
        return 0;
    }
    return l1/l2;
}

int main(int argc, char **argv)
{
    int a, b;
    a = b = 0;
    
    cout << "Podaj 2 liczby: " << endl;
    cin >> a >> b;
    
    dodaj(a, b); //wywołanie funkcji
    cout << "Różnica: " << odejmij(a, b) << endl;
    
    cout << "Iloraz: " << dziel(a, b) << endl;
    
    return 0;
}

