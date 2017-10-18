/*
 * funkcje.cpp
 */


#include <iostream>

using namespace std;

int sumuj(int a, int b)
{
    return a + b;
}

int odejmij(int a, int b)
{
    return a - b;
}

int iloczyn(int a, int b)
{
    return a * b;
}

int iloraz(int a, int b)
{
    // sprawdź b!
    return a/b;
}

int main(int argc, char **argv)
{
    int a, b;
    cout << "Podaj liczby: ";
    cin >> a >> b;
    
    int suma = sumuj(a, b);
    int roznica = odejmij(a, b);
    
    cout << "Suma: " << suma << endl;
    cout << "Różnica: " << roznica << endl;

    return 0;
}

