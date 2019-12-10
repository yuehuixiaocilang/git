import unittest
from BeautifulReport import BeautifulReport
from news.test01 import ddt_demo1
import base.HTMLTestRunner

suit = unittest.TestSuite()
loader = unittest.TestLoader()
suit.addTest(loader.loadTestsFromModule(ddt_demo1))
if __name__ == '__main__':
    test_suite = suit
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')
