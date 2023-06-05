import pytest, time
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage 
from .helper.utility import HelperMethods
from .pages.locators import LoginPageLocators


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                     # открываем страницу
    page.should_be_login_link()     # проверяем наличие ссылки на страницу логина
    
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    main_page = ProductPage(browser, link)   
    main_page.open()                      
    main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    1. Гость открывает страницу товара
    2. Переходит в корзину по кнопке в шапке 
    3. Ожидаем, что в корзине нет товаров
    4. Ожидаем, что есть текст о том что корзина пуста     
    """
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link, 0)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(autouse=True) 
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        main_page = ProductPage(browser, link)   
        main_page.open()                      
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.get_element(*LoginPageLocators.REGISTER_EMAIL_INPUT, r'Registration form does not contain an Email field!').send_keys(HelperMethods.get_fake_email())
        login_page.get_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT, r'Registration form does not contain an Password field!').send_keys('12345_Qwerty')
        login_page.get_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT, r'Registration form does not contain an Confirm Password field!').send_keys('12345_Qwerty')
        login_page.get_element(*LoginPageLocators.REGISTATION_SUBMIT_BUTTON, r'Registration form does not contain a Submit button!').click()
        login_page.should_be_authorized_user()
        
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link, 0)
        page.open()
        page.should_not_be_success_message()
        
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209"
        page = ProductPage(browser, link)
        page.open()
        product_attributes = page.get_product_attributes()
        page.add_product_to_basket()
        assert product_attributes == BasketPage(browser, browser.current_url).get_products_attributes(), '\nAttributes of product in basket does not match item added!'   