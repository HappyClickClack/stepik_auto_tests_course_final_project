import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By 

class ProductPage(BasePage):
    def add_product_to_basket(self, check_details = True):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        if check_details:
            self.check_notification()
            self.go_to_basket_page()

    def get_product_attributes(self):
        self.product_price = self.get_element(*ProductPageLocators.PRODUCT_PRICE, r'Product price is not presented!').text.strip()
        self.product_name = self.get_element(*ProductPageLocators.PRODUCT_NAME, r'Product name is not presented!').text.strip()
        return (self.product_name, self.product_price)

    def add_to_basket(self):
        self.get_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON, r'"Add to basket" button is not presented!').click()
        
    def check_notification(self):
        assert self.product_name == self.get_element(*ProductPageLocators.NOTIFICATION_PRODUCT_NAME, r'Notification with product name is not presented!').text.strip(),\
           r'Product name in Notification does not match item added!'
        assert self.product_price == self.get_element(*ProductPageLocators.NOTIFICATION_PRODUCT_PRICE, r'Notification with product price is not presented!').text.strip(),\
           r'Product price in Notification does not match item added!'

    def go_to_basket_page(self):
        self.get_element(*ProductPageLocators.BASKET_LINK, r'View basket" button is not presented!').click()
        
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           r'Success message is presented, but should not be!'
        
    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
           r'Success message is not disappeared, but should be!'