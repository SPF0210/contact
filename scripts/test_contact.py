import time

import pytest

from base.base_driver import init_driver
from page.page import Page


class TestContact:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"),
                                 [("zhangsan", "18888888888"), ("lisi", "13333333333"), ("wangwu", "17777777777")])
    def test_contact(self,name,phone):
        self.page.contact_list.click_add_contact()
        self.page.new_contact_page.input_name(name)
        self.page.new_contact_page.input_phone(phone)