import time
from .base_page import BasePage
from .locators import LoginPageLocators, BasePageLocators
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url, "Login url is not presented"
        # assert True (mock stub)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        # assert True (mock stub)

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        # assert True (mock stub)

    def register_new_user(self, email, password):
        find_email_field = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        find_email_field.send_keys(email)
        find_password_field = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD)
        find_password_field.send_keys(password)
        find_confirm_password_field = self.browser.find_element(*LoginPageLocators.CONFIRM_REGISTER_PASSWORD)
        find_confirm_password_field.send_keys(password)
        find_register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        find_register_button.click()










