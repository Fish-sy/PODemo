# coding = utf-8

import unittest, os
from selenium import webdriver
from pages.business_logic import Login
from pages.business_logic import Search
from pages.business_logic import Shop
from pages.business_logic import AccountOrder
from pages.business_logic import MyOrder
from pages.business_logic import Logo
from pages.models.myunit import MyunitTest
from pages.models.log import TestLog
from BeautifulReport import BeautifulReport
from common import conf

"""
    第三层:
    -使用单元测试框架对封装好的业务逻辑层进行测试
"""

log = TestLog().getlog()
class BasicFlow(MyunitTest):
    def save_img(self, img_name):
        self.driver.get_screenshot_as_file('{}/{}.png'.format(conf.imagePath, img_name))

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

    @BeautifulReport.add_test_img('test_shop')
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

    def test_to_my_order(self):
        """我的订单"""
        # 调用MyOrder方法
        order_for = MyOrder(driver=self.driver)
        order_number = order_for.myorder()
        log.info("订单日期: %s" % order_number)

    def test_withdraw_from(self):
        """退出"""
        # 调用Logo方法
        logo_for = Logo(driver=self.driver)
        home_page = logo_for.logo()
        # 调用Logout方法
        user_text = home_page.logout()
        self.assertNotIn('123@qq.com', user_text)

if __name__ == '__main__':
    unittest.main()
