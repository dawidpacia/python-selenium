import unittest
from hamcrest import *

class BasicTests(unittest.TestCase):

    def test_add(self):
        assert_that(1, equal_to(2))


if __name__ == "__main__":
    unittest.main()
