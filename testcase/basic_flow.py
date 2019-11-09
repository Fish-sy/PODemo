# coding = utf-8

import unittest
from selenium import webdriver
from pages.business_logic import Login
from pages.business_logic import Search
from pages.business_logic import Shop
from pages.business_logic import AccountOrder
from pages.business_logic import MyOrder

"""
    第三层:
    -使用单元测试框架对封装好的业务逻辑层进行测试
"""


class BasicFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)

    def test_login(self):
        """登录"""
        username = '123@qq.com'
        password = '123456'
        # 调用Login方法
        login_for = Login(driver=self.driver)
        home_page = login_for.login(username, password)
        # 获取首页提示信息
        text_login = home_page.hello_user_text()
        self.assertIn('123@qq.com', text_login)

    def test_search(self):
        """搜索"""
        value = '手机'
        # 调用Search方法
        search_for = Search(driver=self.driver)
        search_page = search_for.search(value)
        # 获取搜索商品头信息
        text_commodity = search_page.commodity_title()
        self.assertIn('苹果', text_commodity)

    def test_shop(self):
        """购物车"""
        # 调用Shop方法
        shop_for = Shop(driver=self.driver)
        shop_page = shop_for.shop()
        self.assertEqual('加入成功', shop_page)

    def test_submit_order(self):
        """结算下单"""
        # 调用AccountOrder方法
        order_for = AccountOrder(self.driver)
        order_page = order_for.accountorder()
        self.assertEqual('支付成功', order_page)

    def test_to_view_order(self):
        """我的订单"""
        # 调用MyOrder方法
        order_for = MyOrder(driver=self.driver)
        print(order_for)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
