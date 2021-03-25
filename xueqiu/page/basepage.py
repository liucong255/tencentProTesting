# -*- coding: utf-8 -*-
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _max_num = 3
    _error_num = 0
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='确定']"),
        (By.XPATH, "//*[@text='下次再说']")
    ]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            self._error_num = 0
            self._driver.implicitly_wait(10)
            return element
        except Exception as e:
            self._driver.implicitly_wait(1)
            if self._error_num > self._max_num:
                raise e
            self._error_num +=1
            for ele in self._black_list:
                elelist = self._driver.find_elements(*ele)
                if len(elelist)>0:
                    elelist[0].click()
                    return self.find(locator, value)
            raise e









