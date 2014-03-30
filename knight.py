#!/usr/bin/python
# coding: utf-8

from __future__ import print_function
import sys
from collections import namedtuple

Coord = namedtuple('Coord', ['x', 'y'])

with open('output.txt', 'wt'):
    pass


def check_args(argv):
    if len(argv) != 3:
        print('usage: knight.py chessboardsize x y\ne.g. knight.py 3 1 2')
        return False
    elif all(map(lambda x: x.isdigit(), argv)):
        if argv[0] > max(argv[1], argv[2]):
            return True
        else:
            print("chessboardsize should be larger than x and y!")
            return False
    else:
        print('arguments must be positive integers!')
        return False


class ChessBoard():

    def __init__(self, n, x, y):
        self.size = n
        self.destination = Coord(n, n)
        self.coord = Coord(x, y)
        self.max_step = pow(n, 2)
        self.min_steps = [[None] * (n + 1) for _ in range(n + 1)]  # min steps from x,y to n,n
        self.min_steps[n][n] = 0
        self.min_steps[x][y] = self.max_step
        self.next_steps = [[None] * (n + 1) for _ in range(n + 1)]  # where to go next
        self.next_steps[n][n] = Coord(n, n)
        self.move = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))
        self.path = []  # record final path
        self.path_found = False

    def in_chessboard(self, x, y):
        if 1 <= x <= self.size and 1 <= y <= self.size:
            return True
        else:
            return False

    def get_next_coord(self, x, y):
        """return all possible coord of next step"""
        for move in self.move:
            next_x, next_y = x + move[0], y + move[1]
            if self.in_chessboard(next_x, next_y):
                yield next_x, next_y

    def find_path(self, x, y):
        candidates = []
        for next_x, next_y in self.get_next_coord(x, y):
            if self.path_found:
                break
            if next_x == next_y == self.size:
                self.path_found = 1  # found the path
                self.min_steps[x][y] = 1
                self.next_steps[x][y] = self.destination
                return
            if self.min_steps[next_x][next_y] is None:
                self.min_steps[next_x][next_y] = self.max_step  # prevent going back
                self.find_path(next_x, next_y)
            candidates.append((self.min_steps[next_x][next_y], Coord(next_x, next_y)))
        try:
            next_coord_min_step, self.next_steps[x][y] = min(candidates)
        except ValueError:
            next_coord_min_step = self.max_step  # no candidates, set unreachable
        self.min_steps[x][y] = min(next_coord_min_step + 1, self.max_step)

    def display_path(self):
        x, y = self.coord.x, self.coord.y
        print("from ({0},{1}) to ({2},{2})".format(x, y, self.size))
        if self.min_steps[x][y] == self.max_step:
            print("unreachable", end='')
            self.path = None
        else:
            print("%d steps: " % self.min_steps[x][y], end='')
            print("(%d,%d)" % (x, y), end='')
            self.path.append((x, y))
            while Coord(x, y) != self.destination:
                x, y = self.next_steps[x][y].x, self.next_steps[x][y].y
                self.path.append((x, y))
                print("->(%d,%d)" % (x, y), end='')
        print('\n')

    def main(self):
        self.find_path(self.coord.x, self.coord.y)
        self.display_path()

if __name__ == '__main__':
    if check_args(sys.argv[1:]):
        cb = ChessBoard(sys.argv[1:])
        cb.find_path(cb.coord.x, cb.coord.y)



