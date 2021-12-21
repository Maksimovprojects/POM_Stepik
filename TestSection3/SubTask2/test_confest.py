from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link_1(chrome_browser):
    chrome_browser.get(link)
    chrome_browser.find_element(By.CSS_SELECTOR, "#login_link")

def test_guest_should_see_login_link_2(gecko_browser):
    gecko_browser.get(link)
    gecko_browser.find_element(By.CSS_SELECTOR, "#login_link")





