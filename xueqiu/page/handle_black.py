# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        _max_num = 3
        _error_num = 0
        _black_list = [
            (By.ID, "com.xueqiu.android:id/action_search"),
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']")
        ]
        from xueqiu.page.basepage import BasePage
        self: BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if _error_num > _max_num:
                raise e
            _error_num += 1
            for ele in _black_list:
                elelist = self.finds(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper
