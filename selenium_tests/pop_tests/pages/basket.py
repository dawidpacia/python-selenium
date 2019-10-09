from selenium_tests.pop_tests.pages.base import BasePage
from selenium.webdriver.common.by import By


class BasketPage(BasePage):
    selectors = {
        "cart_button": (By.CLASS_NAME, "ajax_cart_quantity"),
        "total_price": (By.ID, "total_price"),
        "total_shipping": (By.ID, "total_shipping")
    }

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def navigate_to_cart(self):
        self.driver.find_element(*self.selectors["cart_button"]).click()

    def get_total_price(self):
        price_element = self.driver.find_element(*self.selectors["total_price"]).text
        return float(price_element[1:])

    def get_delivery_price(self):
        delivery_price_element = self.driver.find_element(*self.selectors["total_shipping"]).text
        return float(delivery_price_element[1:])


