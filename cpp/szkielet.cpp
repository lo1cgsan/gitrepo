/*
 * szkielet.cpp
 */

#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int liczba;  // deklaracja zmiennej liczba typu całkowitego
    liczba = 12.78;
    // std::cout << liczba;
    cout << liczba;
    
    int a, b, c, d;  // deklaracja zmiennych
    a = b = c = d = 0; // inicjalizacja zmiennych
    a = 10; // przypisanie
    b = 2 * a; // mnożenie
    c = b + a; // dodawanie
    d = a / b; // dzielenie
    
    cout << "\n" << a << " " << b << " " << (b - a);
    cout << " " << d;
    
    return 0;
}

