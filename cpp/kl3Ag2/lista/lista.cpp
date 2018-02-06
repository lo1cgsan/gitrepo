/*
 * lista.cpp
 * 
 * Copyright 2018  <>
 */

#include <iostream>
#include "lista.hpp"

Lista::Lista(){
    head = NULL; // lista jest pusta
    tail = NULL;
}

Lista::~Lista(){
    while(Usun()) {;};  // usunięcie wszystkich elementów listy
}

void Lista::Dodaj(int wartosc){
    ELEMENT *el = new ELEMENT;
    el->wartosc = wartosc;
    el->nastepny = NULL;
    if (head == NULL) { // lista była pusta
        head = el;
        tail = el;
    } else {
        tail->nastepny = el; // ustawienie wskaźnika nastepny dotychczasowego
        // ostatniego elementu na adres nowego elementu
        tail = el;  // aktualizacja wskaźnika do ostatniego elementu
    }
}

void Lista::Wyswietl(){
    ELEMENT *el = head;
    while (el != NULL) {
        std::cout << el->wartosc << " ";
        el = el->nastepny;
    }
}

bool Lista::Usun(){
    if (head != NULL) { // lista zawiera elementy!
        if (head == tail) { // usuwamy ostatni element
            delete head; // usuwamy zmienną wskazywaną przez head
            head = NULL;
            tail = NULL;
        } else { // usuwamy ostatni element z listy
            ELEMENT *el = head;
            while (el->nastepny != tail){ // szukam przedostatniego elementu
                el = el->nastepny;
            }
            delete el->nastepny; // usuwamy ostatni element
            el->nastepny = NULL;
            tail = el;  // aktualizacja wskaźnka ostatniego elementu
        }
        return true;
    }
    return false;
}

void Lista::Wstaw(int pozycja, int wartosc) {
    ;
}
