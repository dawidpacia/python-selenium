from hamcrest import *
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("http://automationpractice.com")

    def test_something(self):
        self.driver.find_element_by_id("search_query_top").send_keys("Printed Summer")
        self.driver.find_element_by_name("submit_search").click()
        add_to_cart_elements = self.driver.find_elements_by_xpath("// a[ @ title = 'Add to cart']")
        items = self.driver.find_elements_by_class_name("product-container")
        for i in range(len(add_to_cart_elements)):
            ActionChains(self.driver).move_to_element(items[i]).perform()
            add_to_cart_elements[i].click()
            continue_button = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@title='Continue shopping']")))
            continue_button.click()
            continue_button = WebDriverWait(self.driver, 10).until_not(
                EC.element_to_be_clickable((By.XPATH, "//*[@title='Continue shopping']")))
        self.driver.find_element_by_class_name("ajax_cart_quantity").click()
        price_element = self.driver.find_element_by_id("total_product").text
        delivery_price_element = self.driver.find_element_by_id("total_shipping").text
        total_price = float(price_element[1:])
        delivery_price = float(delivery_price_element[1:])
        assert_that(total_price, less_than_or_equal_to(100))
        assert_that(delivery_price, equal_to(2))



    def tearDown(self) -> None:
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
