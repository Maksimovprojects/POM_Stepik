from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_go_to_the_basket(self):
        basket = self.browser.find_element(*BasketPageLocators.BASKET_BUTTON)
        basket.click()

    def should_be_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MSG), "'Your basket is now empty' message " \
                                                                              "isn't presented "



