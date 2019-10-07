import unittest
from hamcrest import *
from python_tests.src.fibonacci import fibonacci

class MyTestCase(unittest.TestCase):

    def test_positive(self):
        assert_that(fibonacci(10), equal_to(34))

    def test_negative(self):
        assert_that(fibonacci(-1), equal_to(False))

    def test_large_value(self):
        assert_that(fibonacci(100), equal_to(218922995834555169026))

    def test_first_value(self):
        assert_that(fibonacci(1), equal_to(0))

    def test_zero(self):
        assert_that(fibonacci(0), equal_to(False))

    def test_string(self):
        assert_that(fibonacci("1"), equal_to(False))

    def test_float(self):
        assert_that(fibonacci(1.1), equal_to(False))


if __name__ == '__main__':
    unittest.main()
