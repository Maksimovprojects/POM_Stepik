import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(10)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form [type = 'submit']")
    assert add_to_basket_button.is_displayed()








