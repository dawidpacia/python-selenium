import unittest
from selenium_tests.pop_tests.pages.main import MainPage
from selenium_tests.pop_tests.pages.login import LoginPage
from selenium import webdriver
from selenium_tests.pop_tests.common.config import url, chrome_options


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        for argument in chrome_options:
            options.add_argument(argument)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(url=url)
        self.main_page, self.login_page, = MainPage(self.driver), LoginPage(self.driver)

    def test_positive_login(self):
        self.login_page.login("aaatest@gmail.com", "test1")
        self.login_page.check_if_logged_in()

    def test_wrong_email(self):
        self.login_page.login("aaatestgmail.com", "test1")
        self.login_page.check_error_alert()

    def test_wrong_password(self):
        self.login_page.login("aaatest@gmail.com", "test12")
        self.login_page.check_error_alert()

    def tearDown(self) -> None:
        self.driver.save_screenshot("test.png")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
