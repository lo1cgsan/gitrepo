#!/usr/bin/env python
# -*- coding: utf-8 -*-
# znaleźć największy wspólny dzielnik dwóch liczb naturalnych

def euklides_rek(a, b):
    if b == 0:
        return a
    return euklides_rek(b, a % b)


def main(args):
    assert euklides_rek(3, 9) == 3
    print(euklides_rek(20, 5))
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
