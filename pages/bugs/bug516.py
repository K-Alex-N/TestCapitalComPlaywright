import allure

from pages.base_page import BasePage


class Bug516(BasePage):

    def open_market_analysis_page(self):
        with allure.step("Open Market and Analysis page"):
            try:
                self.hover_over('.menuGroup_item__jQrol span a[data-type="nav_id689"]')
                self.click('[data-type="nav_id771"]')
            except:
                # sometime Cookies Pop Up Windows appear in the middle of these two command. We just need to repeat it
                self.hover_over('.menuGroup_item__jQrol span a[data-type="nav_id689"]')
                self.click('[data-type="nav_id771"]')