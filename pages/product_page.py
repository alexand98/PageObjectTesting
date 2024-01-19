from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()


    def get_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        return product_name.text


    def get_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_price.text


    def should_be_item_has_been_added_alert(self):
        alert = self.browser.find_element(*ProductPageLocators.ITEM_HAS_BEEN_ADDED_ALERT)
        assert alert.text == self.get_product_name()


    def should_be_header_basket_total_info(self):
        alert = self.browser.find_element(*ProductPageLocators.HEADER_BASKET_TOTAL_INFO)
        assert alert.text.split()[2] == self.get_product_price()


    def should_be_basket_total_alert(self):
        alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert alert.text == self.get_product_price()

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ITEM_HAS_BEEN_ADDED_ALERT), \
            "Success message is presented, but should not be"


    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.ITEM_HAS_BEEN_ADDED_ALERT), \
            "Success message is not dissappeared, but should not be"