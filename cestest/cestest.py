import pytest
import yaml

class Testces:
    def setup_class(self):
        print('类的setup')

    def setup(self):
        print('方法的setup')


    def teardown(self):
        print('方法的teardown')

    @pytest.mark.parametrize(("active", "elment"), [(1, 2), (3, 4)])
    def test_da(self, active, elment):
        print('方法：', active + elment)

if __name__ == '__main__':
    pytest.main()

