from .main_page import MainPage
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_quest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link) # initial Page Object, send to constructor instance of driver and url
    page.open()                    # open page by url
    page.go_to_login_page()        # execute method "go_to_login_page" go to login page


def test_quest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
