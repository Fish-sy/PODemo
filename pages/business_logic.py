# coding = utf-8

from pages.basepage import Page
import time

"""
    第二层:
    -页面元素进行分离,每个元素只定位一次,隔离定位
    -业务逻辑分离
    -当页面发生跳转时,封装的业务逻辑要返回(return)对应的页面对象实例
"""


"""登录"""
class Login(Page):
    # 登录按钮定位(未登录)
    def login_button(self):
        return self.by_xpath("//*[text()='登录' and @class='am-btn-primary btn']")

    # 登录账号框定位
    def form_username(self):
        return self.by_xpath("/html/body/div[5]/div/form/fieldset/div[1]/input")

    # 登录密码框定位
    def form_password(self):
        return self.by_xpath("/html/body/div[5]/div/form/fieldset/div[2]/input")

    # 提交按钮定位
    def login_submit(self):
        return self.submit('/html/body/div[5]/div/form/fieldset/p/button')

    # 登录信息定位
    def login_error_text(self):
        return self.by_xpath("//*[@id='common-prompt']/p")

    # 登录操作(业务逻辑)
    def login(self, username, password):
        self.open('http://47.93.233.188/gpshop')
        self.click(webelement=self.login_button())
        self.send_key(webelement=self.form_username(), keys=username)
        self.send_key(webelement=self.form_password(), keys=password)
        self.login_submit()
        return HomePage(self.driver)


"""商城首页"""
class HomePage(Page):
    # 定位用户信息
    def hello_user(self):
        return self.by_xpath("//*[@class='s-name']")

    # 获取用户信息
    def hello_user_text(self):
        return self.hello_user().text


"""搜索"""
class Search(Page):
    # 定位搜索输入框
    def search_input(self):
        return self.by_xpath('//*[@id="search-input"]')

    # 定位搜索按钮
    def search_button(self):
        return self.by_xpath('//*[@id="ai-topsearch"]')

    # 定位选中商品
    def img_commodity(self):
        return self.by_xpath("//ul[contains(@class,'am-avg-sm-2')]/li[1]/div")

    # 搜索操作(业务逻辑)
    def search(self, value):
        self.send_key(webelement=self.search_input(), keys=value)
        self.click(webelement=self.search_button())
        self.click(webelement=self.img_commodity())
        return CommodityPage(self.driver)


"""商品详细信息页面"""
class CommodityPage(Page):
    # 获取当前窗口title
    def commodity_title(self):
        self.handle(1)
        return self.get_title()


"""添加购物车"""
class Shop(Page):
    # 选择套餐
    def set_meal(self):
        return self.by_xpath("//*[@data-value='套餐一']")

    # 选择颜色
    def sellphone_colour(self):
        return self.by_xpath("//*[@data-value='灰色']")

    # 选择存储
    def sellphone_storage(self):
        return self.by_xpath("//*[@data-value='32G']")

    # 定位加入购物车按钮
    def add_cart_button(self):
        return self.by_xpath("//*[text()='加入购物车']")

    # 提示是否添加成功
    def add_cart_text(self):
        return self.by_xpath("//*[@id='common-prompt']/p")

    # 加入购物车操作(业务逻辑)
    def shop(self):
        self.click(webelement=self.set_meal())
        time.sleep(1)
        self.click(webelement=self.sellphone_colour())
        time.sleep(1)
        self.click(webelement=self.sellphone_storage())
        self.click(webelement=self.add_cart_button())
        return self.add_cart_text().text


"""结算下单"""
class AccountOrder(Page):
    # 定位购物车按钮
    def shop_cart(self):
        return self.by_xpath("//*[@class='am-icon-shopping-cart am-icon-fw']")

    # 定位勾选框
    def check_box(self):
        return self.by_xpath("//*[@class='am-table']/tbody/tr[1]/td[1]/input")

    # 定位结算按钮
    def settle_accounts(self):
        return self.by_xpath("//*[text()='结算']")

    # 定位支付方式
    def payment_way(self):
        return self.by_xpath("//*[text()='现金支付']")

    # 定位提交订单按钮
    def submit_order(self):
        return self.by_xpath("//*[text()='提交订单']")

    # 定位是否支付成功
    def payment_success(self):
        return self.by_xpath("//*[text()='支付成功']")

    # 下单操作(业务逻辑)
    def accountorder(self):
        self.click(webelement=self.shop_cart())
        self.click(webelement=self.check_box())
        self.click(webelement=self.settle_accounts())
        self.click(webelement=self.payment_way())
        self.click(webelement=self.submit_order())
        return self.payment_success().text


"""我的订单"""
class MyOrder(Page):
    # 定位我的订单按钮
    def myorder_button(self):
        return self.by_xpath("//a[contains(@class,'am-btn') and text()='我的订单']")

    # 定位订单编号
    def order_number(self):
        return self.by_xpath("//*[@class='user-content-body']/table[1]/tbody/tr[1]/td/span[1]")

    # 查看订单操作(业务流程)
    def myorder(self):
        self.click(webelement=self.myorder_button())
        return self.order_number().text


"""Logo图标"""
class Logo(Page):
    # 定位logo
    def logo_button(self):
        return self.by_xpath("//*[@class='logo-big']/a/img")

    # 点击logo
    def logo(self):
        self.click(webelement=self.logo_button())
        return Logout(self.driver)


"""注销"""
class Logout(Page):
    # 定位退出按钮
    def logout_button(self):
        return self.by_xpath("//*[text()='退出' and @class='member-logout']")

    # 定位用户信息
    def user_message(self):
        return self.by_xpath("//*[@class='s-name']")

    # 退出(业务流程)
    def logout(self):
        self.click(webelement=self.logout_button())
        return self.user_message().text

