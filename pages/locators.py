from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, "//a[@class='btn btn-default']")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.ID, "register_form")


class BasketPageLocators:
    BASKET_BUTTON = (By.XPATH, "//a[@class='btn btn-default']")
    EMPTY_BASKET_MSG = (By.XPATH, "//*[contains(text(), 'Your basket is empty')]")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button[value='Add to basket']")
    ITEM_PRICE = (By.CSS_SELECTOR, "h1+p.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1) > div[class = 'alertinner '] strong")
    BASKET_ITEM_PRICE = (By.CSS_SELECTOR, "div[class = 'alertinner '] p strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[text()[contains(.,'has been added to your basket')]]")
