import time
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By 

class BasketPage(BasePage):
    def is_basket_empty(self):
        return self.is_not_element_present(*BasketPageLocators.BASKET_TOTAL, timeout = 1)
        
    def should_be_empty_basket(self):
        assert self.is_basket_empty(), r'The basket should be empty, but it is not!'
    
    def get_products_attributes(self):
        result = (None, None)
        if not self.is_basket_empty():
            total = self.get_element(*BasketPageLocators.BASKET_TOTAL, r'Total in basket is not presented!').text
            product_name = self.get_element(*BasketPageLocators.BASKET_PRODUCT_NAME, r'Product name in basket is not presented!').text
            result = (product_name, total)
        return result