from python.calc import Calc
import pytest


class TestCalc:
    def setup(self):
        self.calc = Calc()

    @pytest.mark.parametrize(('a', 'b', 'c'), [(1, 2, 3), (-1, -2 ,-3), (0, 3, 3)])
    def test_add(self, a, b, c):
        result = self.calc.add(a, b)
        assert c == result

    @pytest.mark.parametrize(('a', 'b', 'c'), [(4, 2, 2), (-4, -2, 2), (0, 3, 0)])
    def test_div(self, a, b, c):
        result = self.calc.div(a, b)
        assert c == result


if __name__ == '__main__':
    pytest.main(-v)
