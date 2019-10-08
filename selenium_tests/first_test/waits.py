from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome()
driver.get("https://brainly.com/")
# driver.implicitly_wait(30)


try:
    driver.find_element_by_link_text("LOG IN").click()
    driver.find_element_by_name("username").send_keys("dawidpacia123")
    driver.find_element_by_name("password").send_keys("test123" + Keys.ENTER)
    #driver.find_element_by_xpath("//button[@data-test='form-login-submit']").send_keys()
except NoSuchElementException as err:
    print(err)

element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(., 'new')]")))

element.click()

WebDriverWait(driver, 60).until(
            EC.invisibility_of_element_located((By.XPATH, "//button[contains(., 'new')]")))

driver.quit()
