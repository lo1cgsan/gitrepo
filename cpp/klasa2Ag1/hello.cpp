/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    // char imie; // deklaracja zmiennej znakowej
    char imie[10]; // deklaracja zmiennej tablicowej
    int wiek;
    wiek = 0; //inicjacja zmiennej
    
    cout << "Witaj w C++!" << endl;
    cout << "Podaj imię: ";
    // cin >> imie;
    cin.getline(imie, 10);
    cout << "Cześć, " << imie << "!" << endl;
    cin.ignore(100, '\n');
    cout << "Ile masz lat? ";
    cin >> wiek;
    cout << "Urodziłeś się w roku " << 2017 - wiek << endl;
    
    return 0;
}

