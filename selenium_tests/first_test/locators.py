from selenium import webdriver
from selenium.common.exceptions import *

driver = webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')

try:
    logo_locator = driver.find_element_by_id('header_logo')
    cart_locator = driver.find_element_by_class_name('shopping_cart')
    email_newsletter_locator = driver.find_element_by_link_text('support@seleniumframework.com')
    twitter_locator = driver.find_element_by_class_name('twitter')
    popular_locator = driver.find_element_by_class_name('homefeatured')
    contact_us_locator = driver.find_element_by_link_text('Contact us')

    logo_locator_css = driver.find_element_by_css_selector('[src$="logo.jpg"]')
    cart_locator_css = driver.find_element_by_css_selector('[href$="controller=order"]')
    email_newsletter_locator_css = driver.find_element_by_css_selector('#newsletter-input')
    twitter_locator_css = driver.find_element_by_css_selector('.twitter')
    popular_locator_css = driver.find_element_by_css_selector('.homefeatured')
    contact_us_locator_css = driver.find_element_by_css_selector('#contact-link')

    logo_locator_xpath = driver.find_element_by_xpath('//*[@class="logo img-responsive"]')
    cart_locator_xpath = driver.find_element_by_xpath('//b[contains(text(), "Cart")]')
    email_newsletter_locator_xpath = driver.find_element_by_xpath('//*[@id="newsletter-input"]')
    twitter_locator_xpath = driver.find_element_by_xpath('//*[@class="twitter"]')
    popular_locator_xpath = driver.find_element_by_xpath('//*[@class="homefeatured"]')
    contact_us_locator_xpath = driver.find_element_by_xpath('//*[@id="contact-link"]')

except NoSuchElementException as err:
    print(err)

driver.close()

