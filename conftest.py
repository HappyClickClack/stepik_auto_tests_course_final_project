import pytest
from selenium import webdriver
firefox_binary_path = r'C:\Program Files\Mozilla Firefox\firefox.exe'

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Define language: en, ru, etc.")

@pytest.fixture(scope="function")
def browser(request):
    browser = None
    match request.config.getoption("browser_name"):
        case "chrome":
            options = webdriver.ChromeOptions()
            options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption("language")})
            options.add_experimental_option('excludeSwitches', ['enable-logging'])
            browser = webdriver.Chrome(options=options)
        case "firefox":
            options = webdriver.FirefoxOptions()
            options.set_preference("intl.accept_languages", request.config.getoption("language"))
            options.binary_location = firefox_binary_path
            browser = webdriver.Firefox(options=options)
        case _:
            raise pytest.UsageError("--browser_name should be chrome or firefox")

    yield browser

    browser.quit()

def pytest_make_parametrize_id(config, val):
    return repr(val)