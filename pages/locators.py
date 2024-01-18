from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")



class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_HAS_BEEN_ADDED_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    BASKET_TOTAL_ALERT = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) .alertinner p")
    HEADER_BASKET_TOTAL_INFO = (By.CSS_SELECTOR, ".basket-mini")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main p.price_color")