/*
 * hello.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int bok = 0;
    
    cout << "Podaj bok: " << endl;
    cin >> bok;
    cout << "Obwód: " << 4 * bok << endl;
    cout << "Pole: " << bok * bok << endl;
    
    return 0;
}

