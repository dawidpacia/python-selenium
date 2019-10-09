from selenium_tests.pop_tests.pages.base import *
from selenium_tests.pop_tests.selectors.login_page import login_page_selectors as selectors


class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.selectors = selectors

    def login(self, email, password):
        self.driver.find_element(*self.selectors["signin_button"]).click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selectors["email_field"]))
        self.driver.find_element(*self.selectors["email_field"]).send_keys(email)
        self.driver.find_element(*self.selectors["password_field"]).send_keys(password)
        self.driver.find_element(*self.selectors["submit_signin_button"]).click()
