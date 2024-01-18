import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.click_add_to_basket_button()
    page.solve_quiz_and_get_code()
    page.should_be_item_has_been_added_alert()
    page.should_be_basket_total_alert()
    page.should_be_header_basket_total_info()