# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

"""
    第一层:二次封装selenium,定义一个所有页面都继承的Page类
"""

"""
def open_browser(name, url):
    if name == 'chrome':
        driver = webdriver.Chrome()
        print('Starting for Chrome')
    elif name == 'ie':
        driver = webdriver.Ie()
        print('Starting for IE')
    elif name == 'ff':
        driver = webdriver.Firefox()
        print('Starting for FireFox')
    driver.get(url)
    driver.maximize_window()
    return driver
"""

class Page(object):
    def __init__(self, driver):
        self.driver = driver

    def max_window(self):
        """窗口最大化"""
        self.driver.maximize_window()

    def _open(self, url):
        """打开URL"""
        self.driver.get(url)

    def open(self, base_url):
        """调用_open"""
        self._open(base_url)

    def by_xpath(self, xpath):
        """封装xpath定位"""
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            print(f"页面未定位到 {xpath} 元素")

    def get_title(self):
        """获取当前窗口title"""
        return self.driver.title

    def click(self, webelement):
        """点击操作"""
        webelement.click()

    def send_key(self, webelement, keys):
        """清除输入框后输入内容"""
        webelement.clear()
        webelement.send_keys(keys)

    def close(self):
        """关闭当前窗口"""
        self.driver.close()

    def quit(self):
        """退出浏览器"""
        self.driver.quit()

    def submit(self, xpath):
        """提交"""
        element = self.by_xpath(xpath)
        element.submit()

    def handle(self, value):
        """句柄切换"""
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[value])
        except:
            print(f"根据 {value} 获取句柄失败")

    def to_frame(self, xpath):
        """内联框架"""
        element = self.by_xpath(xpath)
        self.driver.switch_to.frame(element)

    def back(self):
        """返回到旧的窗口"""
        self.driver.back()

    def forward(self):
        """前进到新窗口"""
        self.driver.forward()

    def mouse_hover(self, xpath):
        """鼠标悬停"""
        try:
            element = self.by_xpath(xpath)
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            print("鼠标悬停操作失败")
            return False


