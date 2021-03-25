# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from xueqiu.page.basepage import BasePage
from xueqiu.page.market import Market


class Main(BasePage):
    def goto_market(self):
        self.find(By.XPATH, "//*[@text='行情']").click()
        return Market(self._driver)