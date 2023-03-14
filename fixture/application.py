# -*- coding: utf-8 -*-
from selenium import webdriver

from fixture.group import GroupHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        self.wd = webdriver.Firefox(executable_path=r'C:\Users\Aziz\PycharmProjects\pythonProject2\geckodriver.exe',
                                    options=options)
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/")

    def destroy(self):
        self.wd.quit()
