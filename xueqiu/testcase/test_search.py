# -*- coding: utf-8 -*-
import pytest
import yaml

from xueqiu.page.app import App


class TestSearch:
    def setup(self):
        self.search = App().start().main().goto_market().goto_search()

    def teardown(self):
        pass

    # @pytest.mark.parametrize('name', yaml.safe_load(open("./case.yaml", encoding="utf-8")))
    @pytest.mark.parametrize('name', ["阿里巴巴", "阿里巴巴-SW"])
    def test_search(self, name):
        self.search.search(name)
        if self.search.is_choose(name):
            self.search.reset(name)
        self.search.add(name)
        assert self.search.is_choose(name)
