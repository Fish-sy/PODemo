import unittest
from selenium import webdriver
from pages.log import TestLog


log = TestLog().getlog()
class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        log.info("opened the browser successed!")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        log.info("quit the browser success!")




