import unittest
from selenium_tests.pop_tests.pages.main import MainPage
from selenium_tests.pop_tests.pages.search import SearchPage
from selenium_tests.pop_tests.pages.basket import BasketPage
from selenium import webdriver
from hamcrest import *


class CartTests(unittest.TestCase):

    url = "http://automationpractice.com/index.php"

    def setUp(self) -> None:
        driver = webdriver.Chrome()
        driver.get(url=self.url)

        self.main_page = MainPage(driver)
        self.search_page = SearchPage(driver)
        self.basket_page = BasketPage(driver)

    def test_adding_to_cart(self):
        self.main_page.make_search("Printed Summer")
        self.search_page.add_all_elements_to_cart()
        self.basket_page.navigate_to_cart()
        total_price = self.basket_page.get_total_price()
        delivery_price = self.basket_page.get_total_price()
        assert_that(total_price, less_than_or_equal_to(100))
        assert_that(delivery_price, equal_to(2))

    def tearDown(self) -> None:
        self.main_page.driver.quit()


if __name__ == '__main__':
    unittest.main()
