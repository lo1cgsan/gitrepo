/*
 * petle_cw7.cpp
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int m = 0; // numer miesiąca
    for (int i=0; i < 3; i++)
    {
        cout << "Podaj numer miesiąca: ";
        cin >> m;
        if (m > 0 && m < 13) break;
        else cout << "Błędne dane!" << endl;
    }
    
    switch (m)
    {
        // if (m == 1)
        case 1:
            cout << "styczeń";
        break;
        // if (m == 2)
        case 2:
            cout << "luty";
        break;
        // if (m == 3)
        case 3:
            cout << "marzec";
        break;
    }
    
    return 0;
}

