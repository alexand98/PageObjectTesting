from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_add_to_basket_button(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        button.click()


    def should_be_item_has_been_added_alert(self):
        alert = self.browser.find_element(*ProductPageLocators.ITEM_HAS_BEEN_ADDED_ALERT)
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        assert alert.text == product_title.text


    def should_be_header_basket_total_info(self):
        alert = self.browser.find_element(*ProductPageLocators.HEADER_BASKET_TOTAL_INFO)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert alert.text.split()[2] == product_price.text


    def should_be_basket_total_alert(self):
        alert = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert alert.text == product_price.text
