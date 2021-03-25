# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestDemo:
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        # options = options
        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_demodeleter(self):
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        sleep(19)

        elements = self.driver.find_elements(By.CSS_SELECTOR, '.jstree-contextmenu-hover')
        print(elements)
        elements[-5].click()
        self.driver.find_element(By.XPATH, '//*[@text ="删除"]').click()
        self.driver.find_element(By.XPATH, '//*[@text ="确定"]').click()
