/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    // char imie; // deklaracja zmiennej znakowej
    char imie[10]; // deklaracja zmiennej tablicowej
    
	cout << "Witaj w C++!" << endl;
	cout << "Podaj imię: ";
    cin >> imie;
    cout << "Cześć, " << imie << "!" << endl;
	return 0;
}

