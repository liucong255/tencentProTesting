# -*- coding: utf-8 -*-
import logging

from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from xueqiu.page.handle_black import handle_black


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def finds(self, locator, value: str = None):
        element: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        #element = self._driver.find_element(*locator) if isinstance(locator, tuple) else self._driver.find_element(locator, value)
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator, value)
        self._driver.implicitly_wait(10)
        return element
