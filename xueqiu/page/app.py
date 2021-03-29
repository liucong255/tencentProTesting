# -*- coding: utf-8 -*-
from appium import webdriver

from xueqiu.page.basepage import BasePage
from xueqiu.page.main import Main


class App(BasePage):
    def start(self):
        if self._driver == None:
            caps = {}
            caps["platformName"] = "android"
            caps["deviceName"] = "127.0.0.1:7555"
            caps["appPackage"] = "com.xueqiu.android"
            caps["appActivity"] = ".common.MainActivity"
            caps["ensureWebviewsHavePages"] = True
            caps["skipServerInstallation"] = True
            caps["skipDeviceInitialization"] = True
            caps["noReset"] = 'true'
            self._driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        else:
            self._driver.start_activity('com.xueqiu.android', '.common.MainActivity')

        self._driver.implicitly_wait(4)

        return self

    def restart(self):
        pass

    def stop(self):
        pass

    def main(self) ->Main:
        return Main(self._driver)
