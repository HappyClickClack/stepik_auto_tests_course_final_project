import math
from ..helper.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        if timeout > 0:
            self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def go_to_login_page(self):
        login_link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, method, css_selector):
        try:
            self.browser.find_element(method, css_selector)
        except (NoSuchElementException):
            return False
        return True

    def get_element(self, method, css_selector, error_message = ''):
        try:
            return self.browser.find_element(method, css_selector)
        except (NoSuchElementException):
            assert False, error_message

    def is_not_element_present(self, method, css_selector, timeout=4):
        """Check that the element does not appear on the page within the specified time"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return True # the element does NOT appear on the page within the specified time

        return False

    def is_disappeared(self, method, css_selector, timeout=4):
        """Check that the element disappear from the page within the specified time"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((method, css_selector)))
        except TimeoutException:
            return False # the element has NOT disappeared from the page within the given time

        return True

    def go_to_basket_page(self):
        self.get_element(*BasePageLocators.BASKET_LINK, r'View basket" button is not presented!').click()

    def solve_quiz_and_get_code(self):
        try:
            alert = self.browser.switch_to.alert
            x = alert.text.split(" ")[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()
        except NoAlertPresentException:
            pass
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            pass

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), r'User icon is not presented, probably unauthorized user!'