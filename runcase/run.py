# coding = utf-8

import unittest
import os
import HTMLTestRunner
import time
from BeautifulReport import BeautifulReport

case_path = '..\\testcase'
discover = unittest.defaultTestLoader.discover(case_path, pattern="basic_flow.py")

if __name__ == '__main__':
    # 用HTMLTestRunner 实现的测试报告
    """
    # 构造测试集
    suit = unittest.TestSuite()
    suit.addTest(discover)
    # 自定义报告存放路径
    file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))    # 获取当前路径的父级路径
    #定义测试报告的名称
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    file_path = os.path.join(file_path_father + "\\report\\" + reportName)
    f = open(file_path, 'wb')
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
    file_path_father = os.path.abspath(os.path.dirname(os.getcwd()))
    file_path = os.path.join(file_path_father + "\\report\\" + "\\TestReport\\")
    reportName = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + '.html'
    BeautifulReport(discover).report(filename=reportName, description='Basic Flow', report_dir=file_path)
