# -*- coding: utf-8 -*-
import yaml
from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.css = Calc()
        self.steps = yaml.safe_load(open('datas/testInfo.yml'))

    @pytest.mark.parametrize('a, b, c', yaml.safe_load(open('datas/testYmal.yml')))
    def test_add(self, a, b, c):
        for step in self.steps:
            print(step)
            if step == 'add':
                result = self.css.add(a, b)
                assert c == result
            if step == 'add1':
                result = self.css.add(a, b)
                assert c == result


    #
    # @pytest.mark.parametrize('a, b, c', yaml.safe_load(open('datas/testYmal.yml')))
    # def test_div(self, a, b, c):
    #     result = self.css.div(a, b)
    #     assert c == result


# if __name__ == '__main__':
#     pytest.main('-vs')