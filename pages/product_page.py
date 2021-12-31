from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_product_page(self):
        self.should_be_product_url()
        self.should_be_item_price()
        self.should_be_add_to_basket_button()
        self.should_be_name_of_item()
        self.should_not_be_success_message()

    def should_be_product_url(self):
        assert self.browser.current_url, "Product page url is not presented"

    def should_be_item_price(self):
        assert self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text, "Price is not presented"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), "'Add to basket' button is not " \
                                                                                "presented "

    def should_be_name_of_item(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), "Name of item is not presented"

    def should_be_available_click_add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        basket.click()

    def should_be_name_of_item_added_to_basket_the_same(self):
        name_of_item_in_basket = self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        assert name_of_item_in_basket == item_name, "The name of item on the product page and in basket isn't same"

    def basket_price_equals_product_page_price(self):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_PRICE).text
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        assert item_price == basket_price, "Price on product page and basket page isn't equal"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared"
