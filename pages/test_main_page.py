from .main_page import MainPage
from .login_page import LoginPage


def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # initial Page Object, send to constructor instance of driver and url
    # page is instance of MainPage class with two arguments
    page.open()                    # open page by url
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_quest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()