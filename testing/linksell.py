# -*- coding: utf-8 -*-

# coding=utf-8
from selenium import webdriver
import selenium
import time
import sys
import pytest
import yamail
import yaml




class TestLinKsell:
    def setup_class(self):
        print('class的setup方法')
        self.driver = webdriver.Chrome()
        self.timems111 = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        self.driver.maximize_window()
        self.driver.get('http://bmlx.ematong.com/')
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
        self.driver.find_element_by_id('username2').send_keys('lxtest')
        self.driver.find_element_by_id('password2').send_keys('lxtest2020')
        time.sleep(20)
        # ipt = input()
        # self.driver.find_element_by_id('yzm2').send_keys(ipt)
        #self.driver.find_element_by_id('submit2').click()

    def setup(self):
        print('setup方法')
        time.sleep(10)


    def teardown_class(self):
        """
        关闭浏览器
        """
        self.driver.quit()

    @pytest.mark.parametrize(('active, elment'), yaml.safe_load(open('datas/element.yml')))
    def test_da(self, active, elment):
        self.driver.find_element_by_id(elment).click()
        time.sleep(10)
        print(self.timems111, active, '页面加载成功')


if __name__ == '__main__':
    pytest.main()

