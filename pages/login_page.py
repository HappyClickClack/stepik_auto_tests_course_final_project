from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.current_url.find(r'login') != -1, "Substring 'login' is not presented in the login URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        self.get_element(*LoginPageLocators.REGISTER_EMAIL_INPUT, r'Registration form does not contain an Email field!').send_keys(email)
        self.get_element(*LoginPageLocators.REGISTER_PASSWORD_INPUT, r'Registration form does not contain an Password field!').send_keys(password)
        self.get_element(*LoginPageLocators.REGISTER_CONFIRM_PASSWORD_INPUT, r'Registration form does not contain an Confirm Password field!').send_keys(password)
        self.get_element(*LoginPageLocators.REGISTATION_SUBMIT_BUTTON, r'Registration form does not contain a Submit button!').click()