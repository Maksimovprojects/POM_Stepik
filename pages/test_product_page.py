import time
from selenium.common.exceptions import NoAlertPresentException  # в начале файла
from selenium.webdriver.common.by import By
from selenium import webdriver
from .locators import ProductPageLocators
from .product_page import ProductPage


def test_quest_can_go_to_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)  # initial Page Object, send to constructor instance of driver and url
    # page is instance of ProductPage class with two arguments
    page.open()  # open page by url
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_product_page()

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_page = ProductPage(browser, browser.current_url)
    product_page.should_be_available_click_add_to_basket()
    product_page.test_solve_quiz_and_get_code()
    product_page.should_be_message_added_to_basket()
    product_page.basket_price_equals_product_page_price()




