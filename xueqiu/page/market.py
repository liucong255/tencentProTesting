# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from xueqiu.page.basepage import BasePage
from xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        #self.find(By.ID, "com.xueqiu.android:id/action_search").click()
        return Search(self._driver)
