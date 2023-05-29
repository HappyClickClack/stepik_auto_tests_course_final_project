from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
    
#def test_guest_should_see_login_link(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    page = MainPage(browser, link)
#    page.open()
#    page.should_be_login_link()
#    
#def test_guest_can_go_to_login_page(browser):
#    link = "http://selenium1py.pythonanywhere.com/"
#    main_page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
#    main_page.open()                      # открываем страницу
#    main_page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина
#    login_page = LoginPage(browser, browser.current_url)
#    login_page.should_be_login_page()
    
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    product_attributes = page.get_product_attributes()
    page.add_product_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_product_attributes = basket_page.get_products_attributes()
    assert product_attributes == basket_product_attributes, '\nAttributes of product in basket does not match item added!'