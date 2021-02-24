# -*- coding: utf-8 -*-
from selenium.webdriver.remote.webdriver import WebDriver
from selenium_wework_main.page.main import Main


class TestADDMember:

    def __init__(self):
        self.main = Main()

    def test_addmember(self):
        self.main.goto_add_member().add_Member()
        # assert 'aaaa' in Main().goto_add_member().add_member()