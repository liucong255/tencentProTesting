# -*- coding: utf-8 -*-
import pytest


class Test_Ces:
    _parame = {"name" : "西西米"}
    def test_en(self):
        raw = "sdgsdfgdfgd${name}sfgfdgdfg"
        for key, value in self._parame.items():
            # raw = raw.replace('${'+key+'}', value)
            raw = raw.replace(f'${{{key}', value)
            print(raw)

            yaml.safe_load(open("./case.yaml", encoding="utf-8"))