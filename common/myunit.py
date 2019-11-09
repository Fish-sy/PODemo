from selenium import webdriver
import unittest
from common import readconfig


# 测试用例初始化操作
class Initialize(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(readconfig.url)
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()




