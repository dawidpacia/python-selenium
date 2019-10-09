import unittest
from selenium_tests.pop_tests.pages.main import MainPage
from selenium_tests.pop_tests.pages.search import SearchPage
from selenium_tests.pop_tests.pages.basket import BasketPage
from selenium_tests.pop_tests.pages.login import LoginPage
from selenium_tests.pop_tests.pages.address import AddressPage
from selenium import webdriver
from hamcrest import *
import HtmlTestRunner
import logging

class CartTests(unittest.TestCase):

    url = "http://automationpractice.com/index.php"

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        #options.add_argument("--headless")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url=self.url)

        self.main_page, self.search_page, self.basket_page, self.login_page, self.address_page  \
            = MainPage(self.driver), SearchPage(self.driver), BasketPage(self.driver), LoginPage(self.driver), AddressPage(self.driver)


    def test_adding_to_cart(self):
        self.login_page.login("aaatest@gmail.com", "test1")
        self.main_page.make_search("Printed Summer")
        self.search_page.add_all_elements_to_cart()
        self.basket_page.navigate_to_cart()
        total_price = self.basket_page.get_total_price()
        delivery_price = self.basket_page.get_delivery_price()

        assert_that(total_price, less_than_or_equal_to(100))
        assert_that(delivery_price, equal_to(2))

        self.basket_page.proceed_to_ceckout()
        self.address_page.proceed_to_ceckout()

    def tearDown(self) -> None:
        self.driver.save_screenshot("reports\\cart_screenshot.png")
        self.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(report_name="last_report.html"))
