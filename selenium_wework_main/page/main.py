# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium_wework_main.page.add_member import AddMember
from selenium.webdriver.chrome.options import Options

class Main:
    def __init__(self):
        options = Options()
        options.debugger_address = "127.0.0.1:9222"
        self._driver = webdriver.Chrome(options=options)
        self._driver.implicitly_wait(3)

    def goto_add_member(self):
        self._driver.get('https://work.weixin.qq.com/wework_admin/frame')
        self._driver.find_element(By.CSS_SELECTOR, "menu_contacts").click()
        return AddMember(self._driver)