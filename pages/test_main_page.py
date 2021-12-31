import time

from .main_page import MainPage
from .login_page import LoginPage
from .basket_page import BasketPage


def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)  # initial Page Object, send to constructor instance of driver and url
    # page is instance of MainPage class with two arguments
    main_page.open()  # open page by url
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_quest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    page.open()
    page.should_go_to_the_basket()
    page.should_be_empty_basket()