#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  funkcje2.py

def sumuj(x, y):
    return x + y

def odejmij(x, y):
    return x - y

def main(args):
    a = int(input('Podaj liczbe: '))
    b = int(input('Podaj liczbe: '))
    print('Suma:', sumuj(a, b))
    print('Różnica:', odejmij(a, b))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
