from selenium import webdriver

options = webdriver.ChromeOptions()
#options.add_argument('--headless')
#options.add_argument('--accept_untrusted_certs')
#driver2 = webdriver.Firefox()
#driver2.close()

driver = webdriver.Chrome(options=options)
driver.get("http://automationpractice.com/index.php")
driver.find_element_by_id("header_logo").click()
driver.close()
