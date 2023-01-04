import unittest


def factorize(x):
    """
    Factorize positive integer and return its factors.
    :type x: int,>=0
    :rtype: tuple[N],N>0
    """
    if x == 0 or x == 1:
        return x,


class TestFactorize(unittest.TestCase):

    def test_wrong_types_raise_exception(self):
        self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        self.assertRaises(ValueError, factorize, -1)

    def test_zero_and_one_cases(self):
        x1 = 0
        x2 = 1
        result1 = factorize(x1)
        result2 = factorize(x2)

        print(result1)

        for result, x in zip([result1, result2], [x1, x2]):
            self.assertCountEqual(result, x)

    def test_simple_numbers(self):
        result1 = factorize(3)
        result2 = factorize(13)

        for result in result1, result2:
            self.assertEqual(re)
