# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from xueqiu.page.basepage import BasePage


class Search(BasePage):
    def search(self):
        self.find(By.ID, "com.xueqiu.android:id/search_input_text").send_keys('alibaba')
        self.find(By.XPATH, "//*[@text='阿里巴巴']").click()
        self.find(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/stock_layout']//*[@text='阿里巴巴']/../..//*[@text='加自选']").click()

    def is_choose(self):
        eles = self.finds(By.XPATH, "//*[@resource-id='com.xueqiu.android:id/stock_layout']//*[@text='阿里巴巴']/../..//*[@text='已添加']")
        return len(eles) > 0