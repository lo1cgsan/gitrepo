/*
 * dec2bin.cpp
 * 
 * Copyright 2018  <>
 * 
 * 
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    char znakA='A';
    char znakB='B';
    int l14 = 65;
    int l15 = 66;
    cout << (int)znakA << (int)znakB << endl;
    cout << (char)l14 << (char)l15 << endl;
    
    // dane wejściowe
    int reszty[16];
	int liczba = 0;
    int podstawa = 0;
    // 120 - 64 = 56
    // 56 - 32 = 24
    // 24 - 16 = 8
    // 8 - 8 = 0
    // 1111000
    cout << "Podaj liczbę i podstawę: ";
    cin >> liczba >> podstawa;
    
    // algorytm
    int i = 0; // indeks tabeli
    do {  // pętla wykona się przynajmniej raz
        reszty[i] = liczba % podstawa;
        liczba = liczba / podstawa;
        i++;
    } while(liczba > 0);
    
    //~for (int j = i - 1; j >=0; j--){
        //~cout << reszty[j];
    //~}
    
    while (i-1 >= 0) {
        i--;
        if (podstawa > 10)
            cout << (char)(reszty[i]+55);
        else
            cout << reszty[i];
    }
	return 0;
}

