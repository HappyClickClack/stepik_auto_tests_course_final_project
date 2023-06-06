import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
main_page_link = "http://selenium1py.pythonanywhere.com/"

class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        """
        The test checks that a guest can see link to a login page
         1. Guest opens the main page
         2. We expect that there is a link to the 'Login or register' page
        """
        page = MainPage(browser, main_page_link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        """
        The test checks that a guest can open a login page
         1. Guest opens the main page
         2. Goes to the 'Login or register' page by the link in the site header
         3. We expect that opened page is a 'Login or register' page
        """
        main_page = MainPage(browser, main_page_link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    """
    The test checks that the basket is empty for a new guest
     1. Guest opens the main page
     2. Goes to the basket by the button in the site header
     3. We expect that there are no products in the basket
     4. We expect that there is a text that the basket is empty
    """
    page = MainPage(browser, main_page_link, 0) # 0 - disable implicitly_wait
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    