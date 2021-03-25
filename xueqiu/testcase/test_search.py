# -*- coding: utf-8 -*-
from xueqiu.page.app import App


class TestSearch:
    def setup(self):
        pass

    def teardown(self):
        pass

    def test_search(self):
        App().start().main().goto_market().goto_search().search()