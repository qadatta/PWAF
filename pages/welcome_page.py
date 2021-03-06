"""
@author: Anuj Kumar
@email: cdac.anuj@gmail.com
"""
import logging

from pages.checkbox_page import CheckboxPage
from pages.dropdown_page import DropdownPage
from utility.services import Services


class WelcomePage:
    def __init__(self, driver):
        self.driver = driver
        self.services = Services(self.driver)
        self.title = "The Internet"
        self.xpath_link = "//a[text()='%s']"

    def verify_welcome_page(self):
        logging.info('## Verifying home page ##')
        actual_title = self.driver.title
        logging.info('# Actual Title: %s' % actual_title)
        assert actual_title == self.title, "Actual title %s, should be same as %s" % (actual_title, self.title)
        return self

    def click_on_link(self, link_txt):
        logging.info("# Click on link '%s'" % link_txt)
        self.services.assert_and_click_by_xpath(self.xpath_link % link_txt)

        if link_txt == "Checkboxes":
            checkbox_page = CheckboxPage(self.driver)
            checkbox_page.verify_checkbox_page()
            return checkbox_page
        # Dropdown
        if link_txt == "Dropdown":
            dropdown_page = DropdownPage(self.driver)
            dropdown_page.verify_dropdown_page()
            return dropdown_page

        return self
