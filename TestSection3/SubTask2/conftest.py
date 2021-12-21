import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def chrome_browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def gecko_browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()

# comment