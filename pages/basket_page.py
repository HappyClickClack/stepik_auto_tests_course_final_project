import time
from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.webdriver.common.by import By 

class BasketPage(BasePage):
    def get_products_attributes(self):
        total = self.get_element(*BasketPageLocators.BASKET_TOTAL, r'Total in basket is not presented!').text
        product_name = self.get_element(*BasketPageLocators.BASKET_PRODUCT_NAME, r'Product name in basket is not presented!').text
        return (product_name, total)