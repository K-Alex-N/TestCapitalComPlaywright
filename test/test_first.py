from pages.login_page import LoginPage
import allure

@allure.title("Test Login Functionality")
@allure.description("This test verifies that a user can successfully log in to the application.")
def test_login(browser_context):
    with allure.step("Create a new browser tab"):
        page = browser_context.new_page()
    with allure.step("Initialize LoginPage"):
        login_page = LoginPage(page)

    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful(), "Не удалось авторизоваться!"
