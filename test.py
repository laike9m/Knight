import unittest
import knight


class TestArgsCheck(unittest.TestCase):
    def test_succeed(self):
        self.assertTrue(knight.check_args(['1', '2', '3']))

    def test_less_args(self):
        self.assertFalse(knight.check_args(['2', '3']))

    def test_more_args(self):
        self.assertFalse(knight.check_args(['1', '2', '3', '4']))

    def test_none_int(self):
        self.assertFalse(knight.check_args(['2.1', '3', '4']))

    def test_none_int2(self):
        self.assertFalse(knight.check_args(['2', '3kk', '4']))


if __name__ == '__main__':
    unittest.main()
