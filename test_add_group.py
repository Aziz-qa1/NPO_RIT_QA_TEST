# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from group import Group


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\Aziz\PycharmProjects\pythonProject2\geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/")

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
        #self.open_home_page()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def test_add_groups(self):
        #self.open_home_page()
        self.login(username="admin", password="secret")
        #self.open_groups()
        self.create_group(Group(name="name", header="header", footer="footer"))
        #self.return_to_groups_page()
        self.logout()

    def test_add_empty_groups(self):
        #self.open_home_page()
        self.login(username="admin", password="secret")
        #self.open_groups()
        self.create_group(Group(name="", header="", footer=""))
        #self.return_to_groups_page()
        self.logout()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
