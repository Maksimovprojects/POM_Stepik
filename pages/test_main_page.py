import pytest
from .main_page import MainPage
from .login_page import LoginPage
from .basket_page import BasketPage


@pytest.mark.login_quest
class TestLoginFromMainPage:

    def test_quest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)  # initial Page Object, send to constructor instance of driver and url
        # page is instance of MainPage class with two arguments
        main_page.open()  # open page by url
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)  # initialization as instance of class LoginPage
        login_page.should_be_login_page()

    def test_quest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page_basket = BasketPage(browser, link)
    page_basket.should_go_to_the_basket()
    page_basket.should_be_empty_basket()