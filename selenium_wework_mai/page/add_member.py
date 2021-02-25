# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from selenium_wework_mai.page.base_page import BasePage


class AddMember(BasePage):
    def add_Member(self):
        sleep(3)
        self.find(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
        self.find(By.CSS_SELECTOR, '#username').send_keys('aaaa')
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('aaaa')
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('11111111111')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(4)
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute('title') for element in elements]
