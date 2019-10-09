from selenium.webdriver.common.by import By

main_page_selectors = {
    "search_field": (By.ID, "search_query_top"),
    "submit_button": (By.NAME, "submit_search")
}
