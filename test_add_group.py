# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest


class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
    
    def test_add_group(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver)
        self.open_groups_page(driver)
        self.init_new_group(driver)
        self.fill_form(driver)
        self.submit_group_creation(driver)
        self.return_to_group_page(driver)
        self.logout(driver)

    @staticmethod
    def logout(driver):
        driver.find_element_by_link_text("Logout").click()

    @staticmethod
    def return_to_group_page(driver):
        driver.find_element_by_link_text("groups").click()

    @staticmethod
    def submit_group_creation(driver):
        driver.find_element_by_name("submit").click()

    @staticmethod
    def fill_form(driver):
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").clear()
        driver.find_element_by_name("group_name").send_keys("dfdfsdfsf")
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys("sdfdfs")
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys("sdfsdfsdf")

    @staticmethod
    def init_new_group(driver):
        driver.find_element_by_name("new").click()

    @staticmethod
    def open_groups_page(driver):
        driver.find_element_by_link_text("groups").click()

    @staticmethod
    def login(driver):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_id("LoginForm").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='Password:'])[1]/following::input[2]").click()

    @staticmethod
    def open_home_page(driver):
        driver.get("http://localhost/addressbook/index.php")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
