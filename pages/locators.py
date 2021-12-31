from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    # LOGIN_EMAIL = (By.NAME, 'login-username')
    # LOGIN_PASSWORD = (By.NAME, "login-password")
    # LOGIN_BUTTON = (By.NAME, "login_submit")
    #
    REGISTER_FORM = (By.ID, "register_form")
    # REGISTER_EMAIL = (By.NAME, 'registration-email')
    # REGISTER_PASSWORD = (By.NAME, "registration-password1")
    # CONFIRM_REGISTER_PASSWORD = (By.NAME, "registration-password2")
    # REGISTER_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, "button[value='Add to basket']")
    ITEM_PRICE = (By.CSS_SELECTOR, "h1+p.price_color")
    ITEM_NAME = (By.CSS_SELECTOR, "h1")
    BASKET_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1) > div[class = 'alertinner '] strong")
    BASKET_ITEM_PRICE = (By.CSS_SELECTOR, "div[class = 'alertinner '] p strong")
    SUCCESS_MESSAGE = (By.XPATH, "//*[text()[contains(.,'has been added to your basket')]]")
