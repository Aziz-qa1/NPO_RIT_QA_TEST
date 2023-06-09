from selenium.webdriver.support.select import Select


class UserFieldsHelper:
    def __init__(self, app):
        self.app = app

    def add(self, userfield):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(userfield.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(userfield.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(userfield.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(userfield.nickname)
        wd.find_element_by_name("title").send_keys(userfield.title)
        wd.find_element_by_name("company").send_keys(userfield.company)
        wd.find_element_by_name("address").send_keys(userfield.address)
        wd.find_element_by_name("home").send_keys(userfield.home)
        wd.find_element_by_name("mobile").send_keys(userfield.mobile)
        wd.find_element_by_name("work").send_keys(userfield.work)
        wd.find_element_by_name("fax").send_keys(userfield.fax)
        wd.find_element_by_name("email").send_keys(userfield.email)
        wd.find_element_by_name("email2").send_keys(userfield.email2)
        wd.find_element_by_name("email3").send_keys(userfield.email3)
        wd.find_element_by_name("homepage").send_keys(userfield.homepage)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(userfield.bday)
        wd.find_element_by_xpath("//option[@value='" + userfield.bday + "']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(userfield.bmonth)
        wd.find_element_by_xpath("//option[@value='" + userfield.bmonth + "']").click()
        wd.find_element_by_name("byear").send_keys(userfield.byear)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("address2").send_keys(userfield.address2)
        wd.find_element_by_name("phone2").send_keys(userfield.phone2)
        wd.find_element_by_name("notes").send_keys(userfield.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        wd.find_element_by_link_text("home").click()
