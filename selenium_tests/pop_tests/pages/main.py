from selenium_tests.pop_tests.pages.base import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    selectors = {
        "search_field": (By.ID, "search_query_top"),
        "submit_button": (By.NAME, "submit_search")
    }

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def make_search(self, search_text):
        self.driver.find_element(*self.selectors["search_field"]).send_keys(search_text)
        self.driver.find_element(*self.selectors["submit_button"]).click()
