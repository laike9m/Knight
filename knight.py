#!/usr/bin/python
# coding: utf-8

import sys
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])


def check_args(argv):
    if len(argv) != 3:
        print('usage: knight.py chessboardsize x y\ne.g. knight.py 3 1 2')
        return False
    elif all(map(lambda x: x.isdigit(), argv)):
        return True
    else:
        print('arguments must be positive integers!')
        return False


class ChessBoard():

    def __init__(self, n, x, y):
        self.size = n
        self.coord = Coord(x, y)


if __name__ == '__main__':
    pass



