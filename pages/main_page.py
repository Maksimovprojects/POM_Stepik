from .base_page import BasePage
from selenium.webdriver.common.by import By # In selenium 4.1.0 methods browser.find_element_by_css_selector outdated

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.browser.find_element(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"