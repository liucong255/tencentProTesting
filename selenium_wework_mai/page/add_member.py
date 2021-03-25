# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from selenium_wework_mai.page.base_page import BasePage


class AddMember(BasePage):
    def add_Member(self):
        #   self.waif_for_click((By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)'))
        def wait_add_member(x):
            elements_len = len(self.find(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.js_has_member>div:nth-child(1)>a:nth-child(2)').click()
            return elements_len > 0
        self.waif_for_element(wait_add_member)
        self.find(By.CSS_SELECTOR, '#username').send_keys('aaaa')
        self.find(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('aaaa')
        self.find(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('11111111111')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(4)
        elements = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute('title') for element in elements]
