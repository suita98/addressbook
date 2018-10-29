from selenium import webdriver
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def create_group(self, group):
        driver = self.driver
        # Open Groups page
        driver.find_element_by_link_text("groups").click()
        # Init a new group
        driver.find_element_by_name("new").click()
        # Fill the form
        driver.find_element_by_name("group_name").click()
        driver.find_element_by_name("group_name").send_keys(group.name)
        driver.find_element_by_name("group_header").click()
        driver.find_element_by_name("group_header").clear()
        driver.find_element_by_name("group_header").send_keys(group.header)
        driver.find_element_by_name("group_footer").click()
        driver.find_element_by_name("group_footer").clear()
        driver.find_element_by_name("group_footer").send_keys(group.footer)
        # Submit group creation
        driver.find_element_by_name("submit").click()
        # Return to Groups page
        driver.find_element_by_link_text("groups").click()

    def destroy(self):
        self.driver.quit()