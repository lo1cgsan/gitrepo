#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  mlotek.py

import random

def main(args):
    
    liczba = random.randint(1, 10)
    print(liczba)
    
    for i in range(3):
        odp = int(input('Jaką liczbę mam na myśli? (1-10) '))
        
        if liczba == odp:
            print('Zgadłeś!')
        else:
            print('Błąd!')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
