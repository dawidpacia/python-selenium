from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium_tests.pop_tests.common.config import element_waiting_timeout


class BasePage:


    def __init__(self):
        pass

    def wait_to_appear(self, driver, selector):
        continue_button = WebDriverWait(driver, element_waiting_timeout).until(EC.presence_of_element_located(selector))
        return continue_button

    def wait_to_dissappear(self, driver, selector):
        continue_button = WebDriverWait(driver, element_waiting_timeout).until(EC.invisibility_of_element_located(selector))
        return continue_button

    def hover(self, driver, element):
        ActionChains(driver).move_to_element(element).perform()
