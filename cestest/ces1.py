# coding=utf-8
from selenium import webdriver
import selenium
import time
import sys
import pytest
import yamail
import yaml




class Testces:
    def setup_class(self):
        print('`````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````')
        driver = webdriver.Chrome()
        timems111 = time.strftime('%Y-%m-%d-%H:%M:%S', time.localtime(time.time()))
        driver.maximize_window()
        driver.get('http://bmlx.ematong.com/')
        driver.implicitly_wait(10)
        driver.find_element_by_xpath('//*[@id="layui-layer1"]/span[1]/a').click()
        driver.find_element_by_id('username2').send_keys('lxtest')
        driver.find_element_by_id('password2').send_keys('lxtest2020')
        ipt = input()
        driver.find_element_by_id('yzm2').send_keys(ipt)
        driver.find_element_by_id('submit2').click()

    def setup(self):
        """
        打开浏览器登陆系统
        """
        print('123')


    def teardown(self):
        """
        关闭浏览器
        """
        driver.quit()

    @pytest.mark.parametrize(("active", "elment"), yaml.safe_load(open("/cestest/element.yaml")))
    def test_da(self, active, elment):
        active = self.active
        driver.find_element_by_id(self.elment).click()
        time.sleep(10)
        print(timems111, active, '页面加载成功')


if __name__ == '__main__':
    pytest.main()

