# -*- coding: utf-8 -*-
import inspect
import json
import logging

import yaml
from appium import webdriver
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from xueqiu.page.handle_black import handle_black


class BasePage:
    _parame = {}
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

    def steps(self, path, name):
        with open(path, encoding="utf-8") as f:
            # 谁调用我inspect.stack()[1].function
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]
        raw = json.dumps(steps)
        for key, value in self._parame.items():
            raw = raw.replace('${'+key+'}', value)
            # raw = raw.replace(f'${{{key}', value)
        steps = json.loads(raw)
        for step in steps:
            if "click" == step["action"]:
                self.find(step["by"], step["locator"]).click()
            if "send" == step["action"]:
                self.find(step["by"], step["locator"]).send_keys(step["value"])
            if "len > 0" == step["action"]:
                eles = self.finds(step["by"], step["locator"])
                return len(eles) > 0