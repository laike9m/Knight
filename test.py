#!/usr/bin/python
# coding: utf-8

import unittest
import knight


class TestArgsCheck(unittest.TestCase):
    def test_succeed(self):
        self.assertTrue(knight.check_args(['4', '2', '3']))

    def test_less_args(self):
        self.assertFalse(knight.check_args(['2', '3']))

    def test_more_args(self):
        self.assertFalse(knight.check_args(['1', '2', '3', '4']))

    def test_none_int(self):
        self.assertFalse(knight.check_args(['2.1', '3', '4']))

    def test_none_int2(self):
        self.assertFalse(knight.check_args(['2', '3kk', '4']))

    def test_invalid_size(self):
        self.assertFalse(knight.check_args(['3', '3', '3']))


class TestFindPath(unittest.TestCase):
    def validate_path(self, n, x, y, path):
        if not path:
            return True  # unreachable
        if path[0] != (x, y) or path[-1] != (n, n):
            return False
        valid_range = range(1, n + 1)
        for c, next_c in zip(path[:-1], path[1:]):
            if c[0] not in valid_range or c[1] not in valid_range:
                return False
            dx, dy = abs(next_c[0] - c[0]), abs(next_c[1] - c[1])
            if not {dx, dy} == {1, 2}:
                return False
        return True

    def test_unreachable1(self):
        n, x, y = 2, 1, 2
        cb = knight.ChessBoard(n, x, y)
        cb.main()
        self.assertEqual(cb.path, None, '212 should be unreachable, path %s' % str(cb.path))

    def test_unreachable2(self):
        n, x, y = 2, 1, 1
        cb = knight.ChessBoard(n, x, y)
        cb.main()
        self.assertEqual(cb.path, None, '212 should be unreachable, path %s' % str(cb.path))

    def test_unreachable3(self):
        n, x, y = 3, 2, 2
        cb = knight.ChessBoard(n, x, y)
        cb.main()
        self.assertEqual(cb.path, None, '322 should be unreachable, path %s' % str(cb.path))

    def test_random(self):
        import random
        for i in range(10):
            n = random.randint(1, 300)
            x = random.randint(1, n)
            y = random.randint(1, n)
            print("run test: n=%d, x=%d, y=%d" % (n, x, y))
            cb = knight.ChessBoard(n, x, y)
            cb.main()
            self.assertTrue(self.validate_path(n, x, y, cb.path))

if __name__ == '__main__':
    unittest.main()