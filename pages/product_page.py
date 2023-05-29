import time
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By 

class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.add_to_basket()
        self.solve_quiz_and_get_code()
        self.go_to_basket_page()

    def get_product_attributes(self):
        self.product_price = self.get_element(*ProductPageLocators.PRODUCT_PRICE, r'Product price is not presented!').text
        self.product_name = self.get_element(*ProductPageLocators.PRODUCT_NAME, r'Product name is not presented!').text
        return (self.product_name, self.product_price)

    def add_to_basket(self):
        self.get_element(*ProductPageLocators.ADD_PRODUCT_TO_BASKET_BUTTON, r'"Add to basket" button is not presented!').click()

    def go_to_basket_page(self):
        self.get_element(*ProductPageLocators.BASKET_LINK, r'View basket" button is not presented!').click()