from selenium_tests.pop_tests.pages.base import *


class SearchPage(BasePage):
    selectors = {
        "add_to_cart_button": (By.XPATH, "// a[ @ title = 'Add to cart']"),
        "product_container": (By.CLASS_NAME, "product-container"),
        "continue_shopping_button": (By.XPATH, "//*[@title='Continue shopping']")
    }

    def __init__(self, driver):
        super().__init__()  # access to BasePage + init
        self.driver = driver

    def add_to_cart(self, product_object, add_to_cart_button):
        ActionChains(self.driver).move_to_element(product_object).perform()
        add_to_cart_button.click()
        continue_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.selectors["continue_shopping_button"]))
        continue_button.click()
        WebDriverWait(self.driver, 10).until_not(
            EC.element_to_be_clickable(self.selectors["continue_shopping_button"]))

    def add_all_elements_to_cart(self):
        add_to_cart_elements = self.driver.find_elements(*self.selectors["add_to_cart_button"])
        items = self.driver.find_elements(*self.selectors["product_container"])
        for i in range(len(add_to_cart_elements)):
            self.add_to_cart(items[i], add_to_cart_elements[i])
