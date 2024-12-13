from pages.login_page import LoginPage


def test_login(browser_context):
    page = browser_context.new_page()
    login_page = LoginPage(page)
    login_page.navigate_to("https://www.saucedemo.com/")
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_login_successful(), "Не удалось авторизоваться!"
