from selenium import webdriver


class BasePage:

    url = "http://automationpractice.com/index.php"

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url=self.url)

    def find_element(self):
        pass
