import pytest
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .helper.utility import HelperMethods
main_page_link = "http://selenium1py.pythonanywhere.com/"
product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """
    The test checks that the guest does not see a notification about a new item in the basket after adding an item to the basket
     1. Guest opens some product page
     2. Add the product to the cart, without checking of details
     3. We expect that there is no notification
    """
    page = ProductPage(browser, product_page_link, 0) # 0 - disable implicitly_wait
    page.open()
    page.add_product_to_basket(check_details = False)
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    """
    The test checks that a guest does not see notifications about some items in the cart
     1. User opens some product page
     2. We expect that there are no notifications
    """
    page = ProductPage(browser, product_page_link, 0) # 0 - disable implicitly_wait
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    """
    The test checks that a notification about a new item in the basket disappears after timeout
     1. Guest opens some product page
     2. Add the product to the cart, without checking of details
     3. We expect that notification should disappear
    """
    page = ProductPage(browser, product_page_link, 0) # 0 - disable implicitly_wait
    page.open()
    page.add_product_to_basket(check_details = False)
    page.should_disappear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    """
    The test checks that a guest can open a login page from a product page
     1. Guest opens some product page
     2. We expect that there is a link to the 'Login or register' page
    """
    page = ProductPage(browser, product_page_link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    """
    The test checks that a guest can open a login page from a product page
     1. Guest opens some product page
     2. Goes to the 'Login or register' page by the link in the site header
     3. We expect that opened page is a 'Login or register' page
    """
    main_page = ProductPage(browser, product_page_link)
    main_page.open()
    main_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    """
    The test checks if a guest does not see any items in the basket
    1. Guest opens some product page
    2. Go to the basket
    3. We expect that there are no products in the basket
    """
    page = ProductPage(browser, product_page_link, 0) # 0 - disable implicitly_wait
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()

@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    """
    The test checks if a guest can add an item to the basket
     1. User opens some product page
     2. Read attributes of the product
     3. Add the product to the cart, check the notification on the current product page, go to the Basket page
     4. We expect that there the product in the basket have the same attributes
    """
    page = ProductPage(browser, link)
    page.open()
    product_attributes = page.get_product_attributes()
    page.add_product_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.check_product_in_basket(product_attributes)

class TestUserAddToBasketFromProductPage():

    @pytest.fixture(autouse=True)
    def setup(self, browser):
        main_page = ProductPage(browser, main_page_link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(HelperMethods.get_fake_email(), r'12345_Qwerty')
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        """
        The test checks that the new user does not see notifications about some items in the cart
         1. User opens some product page
         2. We expect that there are no notifications
        """
        page = ProductPage(browser, product_page_link, 0) # 0 - disable implicitly_wait
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        """
        The test checks if a registered user can add an item to the basket
         1. User opens some product page
         2. Read attributes of the product
         3. Add the product to the cart, check the notification on the current product page, go to the Basket page
         4. We expect that there the product in the basket have the same attributes
        """
        page = ProductPage(browser, product_page_link)
        page.open()
        product_attributes = page.get_product_attributes()
        page.add_product_to_basket()
        basket_page = BasketPage(browser, browser.current_url)
        basket_page.check_product_in_basket(product_attributes)