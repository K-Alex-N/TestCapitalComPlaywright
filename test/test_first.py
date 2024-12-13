from pages.login_page import LoginPage
import allure


@allure.epic("UI Tests")
@allure.feature("Login")
@allure.story("Login with valid credentials")
@allure.id('1')
@allure.severity(allure.severity_level.CRITICAL)
def test_login(browser_context):
    """description of test"""
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_successful(), "Login failed!"
