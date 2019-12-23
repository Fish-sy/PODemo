# coding = utf-8

import unittest
import os
import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport
from common import conf

case_path = '..\\testcase'
discover = unittest.defaultTestLoader.discover(case_path, pattern="basic_flow.py")

if __name__ == '__main__':
    # 用HTMLTestRunner 实现的测试报告
    """
    # 构造测试集
    suit = unittest.TestSuite()
    suit.addTest(discover)
    #定义测试报告的名称
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    f = open(conf.reportPath, 'wb')
    # 生成测试报告
    runner = HTMLTestRunner.HTMLTestRunner(
                stream=f,
                verbosity=2,
                title='Flow Path Test',
                description='Result')
    # 运行测试集
    runner.run(suit)
    # 关闭文件
    f.close()
    """

    # 用BeautifulReport生成测试报告
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    BeautifulReport(discover).report(filename=reportName, description='Basic Flow', report_dir=conf.reportPath)
