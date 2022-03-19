from base.base_driver import init_driver
from page.contact_list_page import ContactListPage
from page.new_contact_page import NewContactPage


class Page:
    def __init__(self,driver):
        self.driver = driver

    @property
    def contact_list(self):
        return ContactListPage(self.driver)

    @property
    def new_contact_page(self):
        return NewContactPage(self.driver)