# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep


class AddMember:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def add_Member(self):
        sleep(3)
        self._driver.find_element(By.CSS_SELECTOR, '.js_add_member:nth-child(2)').click()
        self._driver.find_element(By.CSS_SELECTOR, '#username').send_keys('aaaa')
        self._driver.find_element(By.CSS_SELECTOR, '#memberAdd_acctid').send_keys('aaaa')
        self._driver.find_element(By.CSS_SELECTOR, '#memberAdd_phone').send_keys('11111111111')
        self._driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(4)
        elements = self._driver.find_elements(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
        return [element.get_attribute('title') for element in elements]
