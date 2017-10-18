/*
 * petle_switch.cpp
 * Program pobiera numer miesiąca i wyświetla jego nazwę
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    char zn=' '; // deklaracja
    cout << "Podaj znak: ";
    cin >> zn;
    
    while (zn == 't' || zn == 'T' || zn == 'n' || zn == 'N') {
        cout << "Podaj znak: ";
        cin >> zn;
        //~if (zn == 't' || zn == 'T' || zn == 'n' || zn == 'N')
            //~cout << zn << endl;
        //~else
            //~break;
        //~switch (zn) {
            //~case 't':
            //~case 'T':
            //~case 'n':
            //~case 'N':
                //~cout << "Poprawny ";
            //~break;
            //~default:
                //~cout << "Inny znak ";
                //~break;
        //~}
    };
    
    return 0;
}

