/*
 * najwieksza.cpp
 * Pobierz trzy liczby całkowite od użytkownika i wydrukuj największą
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int a, b, c;
    a = b = c = 0;
    cout << "Podaj 3 liczby: ";
    cin >> a >> b >> c;

    if (a > b)
    {
        if (a > c)
            cout << "Największe a=" << a;
        else
            cout << "Największe c=" << c;
    }
    else if (b > a)
    {
        if (b > c)
            cout << "Największe b=" << b;
        else
            cout << "Największe c=" << c;
    }

    return 0;
}

