/*
 * potega.cpp
 * a0 = 1
 * a1 = a
 * an = a*...*a (n-czynników) dla n zaw. N+ - {1}
 */

#include <iostream>

using namespace std;

float potega_it(float x, int n) {
    float wynik = 1;
    for(int i=0; i<n; i++) {
        // testuję ilość powtórzeń pętli
        cout << i << endl;
    }
    return wynik;
}

int main(int argc, char **argv)
{
    // zadeklaruj zmienne
    // i pobierz od użytkownika podstawę i wykładnik
    cout << "Potęga:" << potega_it() << endl;
	return 0;
}

