from selenium_tests.pop_tests.pages.base import *


class AddressPage(BasePage):
    selectors = {
        "proceed_to_checkout_button": (By.XPATH, "//*[@title='Proceed to checkout']")
    }

    def __init__(self, driver):
        super().__init__()
        self.driver = driver

    def proceed_to_ceckout(self):
        proceed = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.selectors["proceed_to_checkout_button"]))
        ActionChains(self.driver).move_to_element(proceed).perform()
        self.driver.find_element(*self.selectors["proceed_to_checkout_button"]).click()
