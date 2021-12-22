import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

# ------------THE FIRST VARIANT ITERATING BROWSERS (NO NEED 'conftest.py' file) ---------------------
@pytest.mark.parametrize('browser', ['webdriver.Chrome()', 'webdriver.Firefox()'])
def test_guest_should_see_login_link(browser):
    with eval(browser) as br:
        br.get(link)
        br.find_element(By.CSS_SELECTOR, "#login_link")
