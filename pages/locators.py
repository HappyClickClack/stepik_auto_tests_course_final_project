from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") #Link (or button) to show the login page
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini>.btn-group>a.btn-default")        # Link (or button) to show the basket page

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")       # Login form header
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # Register form header
    REGISTER_EMAIL_INPUT = (By.CSS_SELECTOR, r'#register_form [name="registration-email"]')
    REGISTER_PASSWORD_INPUT = (By.CSS_SELECTOR, r'#register_form [name="registration-password1"]')
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, r'#register_form [name="registration-password2"]')
    REGISTATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, r'#register_form [name="registration_submit"]')

class ProductPageLocators:
    ADD_PRODUCT_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")          #"Add to Basket" button
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main>.price_color")                 # Item price
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main>h1")                            # Item name
    NOTIFICATION_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alertinner>strong")   # Product name in Notification
    SUCCESS_MESSAGE = NOTIFICATION_PRODUCT_NAME                                     # Message about the successful completion of adding a product to the basket
    NOTIFICATION_PRODUCT_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")# Product price in Notification

class BasketPageLocators:
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, ".basket-items h3>a")           # 1st item name in basket
    BASKET_TOTAL = (By.CSS_SELECTOR, ".basket-items div:nth-child(5)>p")    # Total value of the basket
            