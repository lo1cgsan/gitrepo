/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std;

void sumuj(int a, int b)
{
    cout << "Suma: " << a + b << endl;
}

void odejmij(int a, int b)
{
    cout << "Różnica: " << a - b << endl;
}

void iloczyn(int a, int b)
{
    cout << "Iloczyn: " << a * b << endl;
}

void iloraz(int a, int b)
{
    // sprawdź b!
    cout << "Iloraz: " << a/b << endl;
}

int main(int argc, char **argv)
{
    int a, b;
    cout << "Podaj liczby: ";
    cin >> a >> b;
    
    sumuj(a, b);

    return 0;
}

