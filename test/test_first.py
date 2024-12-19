import time

from playwright.sync_api import Page

from pages.bugs.bug516 import Bug516
from pages.login_page import LoginPage
import allure

# @allure.epic("UI Tests")
# @allure.feature("Login")
# @allure.story("Login with valid credentials")
# @allure.id('1')
# @allure.severity(allure.severity_level.CRITICAL)
# def test_login(page):
#     """description of test"""
#     login_page = LoginPage(page)
#     login_page.navigate_to("https://www.saucedemo.com/")
#     login_page.login("standard_user", "secret_sauce")
#     assert login_page.is_login_successful(), "Login failed!"


def test_bug516(page):
    bug = Bug516(page)
    bug.navigate_to("https://capital.com/en-gb")
    bug.to_close_cookies_pop_up_window()
    bug.open_market_analysis_page()
    time.sleep(5)