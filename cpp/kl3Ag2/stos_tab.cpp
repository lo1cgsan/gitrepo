/*
 * stos_tab.cpp
 * 
 * Copyright 2018  <>
 * 
 */


#include <iostream>

using namespace std;

bool czy_pusty(int sp, int sr) {
    if (sp < sr) return true;
    return false;
}

void push(int stos[], int &sp, int sr, int dane) {
    cout << dane << " ";  // informacyjny wydruk wstawianej wartości
    if (czy_pusty(sp, sr)) {
        stos[sp] = dane;
        sp++;
    } else {
        cout << "Błąd przepełnienia stosu!";
    }
}

int pop(int stos[], int &sp) {
    sp--;
    return stos[sp];
}

int main(int argc, char **argv)
{
	int *stack; //wskaźnik
    int sr; //rozmiar stosu
    int sp = 0; //wskaźnik stosu (ang. stack pointer)
    
    cout << "Podaj rozmiar: "; cin >> sr;
    stack = new int[sr];
    
    srand(time(NULL));
    for (int i=0; i < sr+3; i++) {
        push(stack, sp, sr, rand()%100 + 1);
    }
    
    for (int i=0; i < sr; i++) {
        cout << pop(stack, sp) << " ";
    }
    
    5 + 7 => 57+
    5 - 6 + 7 => 56-7+
    6 / 9 + 8 * 4 => 69/84*+
    
	return 0;
}

