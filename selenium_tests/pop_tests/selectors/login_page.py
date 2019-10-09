from selenium.webdriver.common.by import By

login_page_selectors = {
    "signin_button": (By.CLASS_NAME, "login"),
    "email_field": (By.ID, "email"),
    "password_field": (By.ID, "passwd"),
    "submit_signin_button": (By.ID, "SubmitLogin"),
    "error_alert": (By.ID, "create_account_error")
}
