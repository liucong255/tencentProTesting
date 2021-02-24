# -*- coding: utf-8 -*-=
import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import selenium


class TestDemo:
    def setup(self):
        options = Options()
        options.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome(options=options)
        # options = options

    def teardown(self):
        self.driver.quit()

    def test_demo(self):
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # db = shelve.open("cookies")
        # #db["cookie"] = self.driver.get_cookies()
        # cookies = db["cookie"]
        # for cookie in cookies:
        #     if "expiry" in cookie.keys():
        #         cookie.pop("expiry")
        #     self.driver.add_cookie(cookie)
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        # db.close()
        # sleep(5)
        # self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
        # sleep(5)
        print(self.driver.get_cookies())
