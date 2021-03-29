# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By

from xueqiu.page.basepage import BasePage


class Search(BasePage):
    def search(self, name):
        # self._parame['name'] = name
        self.steps("../page/search.yaml")

    def is_choose(self, name):
        self._parame['name'] = name
        return self.steps("../page/search.yaml")

    def add(self, name):
        self._parame['name'] = name
        self.steps("../page/search.yaml")

    def reset(self, name):
        self._parame['name'] = name
        self.steps("../page/search.yaml")
