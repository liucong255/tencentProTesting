# -*- coding: utf-8 -*-
from selenium_wework_mai.page.main import Main


class TestADDMember:

    def setup(self):
        self.main = Main()

    def test_addm(self):
        #self.main.goto_add_member().add_Member()
        assert 'aaaa' in self.main.goto_add_member().add_Member()
