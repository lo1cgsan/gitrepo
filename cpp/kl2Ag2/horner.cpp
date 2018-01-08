/*
 * horner.cpp
 * 
 */

#include <iostream>

using namespace std;

// W(x) = 2*x*x*x + 3*x*x + 5*x + 4 (8)
// W(x) = x (2x^2 + 3x + 5) + 4
// W(x) = x ( x (2x +3) +5) + 4 (3)

float horner_rek(int k, float tbwsp[], float x) {
    if (k == 0)
        return tbwsp[0] * x;
    return horner_rek(k-1, tbwsp, x) * x + tbwsp[k];
}


float horner_it(int k, float tbwsp[], float x){
    float wynik = tbwsp[0];
    for (int i = 1; i < k + 1; i++){
        wynik = wynik * x + tbwsp[i];
    }
    return wynik;
}


int main(int argc, char **argv)
{
    float x;
    float tbwsp[4];
    int stopien = 3;
    
    cout << "Podaj argument: "; cin >> x;
    for (int i = 0; i < 4; i++) {
        cout << "Podaj współczynnik: ";
        cin >> tbwsp[i];
    }
    
    cout << "Wartość wielomianu: " << horner_it(stopien, tbwsp, x) << endl;
	return 0;
}

