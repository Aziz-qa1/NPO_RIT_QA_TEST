# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.session import SessionHelper


class Application:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\Aziz\PycharmProjects\pythonProject2\geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def add_new_group(self, group):
        wd = self.wd
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()
