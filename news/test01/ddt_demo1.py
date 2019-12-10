from ddt import ddt,data,unpack
import unittest

data1=[1,2]

@ddt #装饰测试类
class TestMath(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self) -> None:
        pass

    @data(*data1)#装饰测试方法
    def test_printdata(self,a):
        print("a=",a)


if __name__ == "__main__":
    a= TestMath()
    a.test_printdata()

