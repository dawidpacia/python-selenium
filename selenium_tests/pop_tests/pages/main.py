from selenium_tests.pop_tests.pages.base import *
from selenium_tests.pop_tests.selectors.main_page import main_page_selectors as selectors


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.selectors = selectors

    def make_search(self, search_text):
        self.driver.find_element(*self.selectors["search_field"]).send_keys(search_text)
        self.driver.find_element(*self.selectors["submit_button"]).click()
