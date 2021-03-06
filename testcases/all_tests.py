"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
from pages.welcome_page import WelcomePage
from utility.drivermanager import DriverManager


class AllTests(DriverManager):
    def test_welcomepage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page()

    def test_checkboxpage(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Checkboxes").select_checkbox(2)

    def test_dropdown_page(self):
        welcome_page = WelcomePage(self.driver)
        welcome_page.verify_welcome_page().click_on_link("Dropdown")
