# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_wework_mai.page.add_member import AddMember
from selenium.webdriver.chrome.options import Options
from selenium_wework_mai.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    def goto_add_member(self):
        self.find(By.CSS_SELECTOR, "#menu_contacts").click()
        return AddMember(self._driver)