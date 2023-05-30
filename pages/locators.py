from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #Link (or button) to show the login page

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # Login form header
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Register form header

class ProductPageLocators():
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket") #"Add to Basket" button
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color") # Item price
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1") # Item name
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>.btn-group>a.btn-default") # Link (or button) to show the basket page
    NOTIFICATION_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner>strong") # Product name in Notification
    SUCCESS_MESSAGE = NOTIFICATION_PRODUCT_NAME # Message about the successful completion of adding a product to the basket
    NOTIFICATION_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong") # Product price in Notification

class BasketPageLocators():
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3>a") # Item name in basket
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-items div:nth-child(5)>p") # Total value of the basket