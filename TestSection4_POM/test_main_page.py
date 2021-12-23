# No need import "time" module, I need only method sleep.
from time import sleep
# In selenium 4.1.0 methods browser.find_element_by_css_selector outdated
from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    sleep(6)
    login_link.click()

def test_quest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)