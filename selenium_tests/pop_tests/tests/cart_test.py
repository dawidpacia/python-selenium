import unittest
from selenium_tests.pop_tests.pages.main import MainPage


class CartTests(unittest.TestCase):

    def setUp(self) -> None:
        self.main_page = MainPage()

    def test_adding_to_cart(self):
        self.main_page.make_search("Printed Summer")

    def tearDown(self) -> None:
        self.main_page.driver.quit()

if __name__ == '__main__':
    unittest.main()
