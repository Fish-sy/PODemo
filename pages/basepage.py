# coding = utf-8

import traceback
from common import log
from selenium import webdriver
from common.readexcel import ReadExcel
from selenium.webdriver.common.action_chains import ActionChains

"""
    第一层:二次封装selenium,定义一个所有页面都继承的Page类
"""
logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')
eleData = ReadExcel()    # 加载Excel中所有元素
baseUrl = eleData.read_excel(0, 1)


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_browser(self, browser='gc'):
        """
        打开浏览器
        :param browser: 默认使用谷歌驱动调用谷歌浏览器
        :return: 打开成功
        """
        if browser == 'gc':
            # 使用缓存加载页面
            # option = Options()
            # user_file = os.environ["USERPROFILE"]
            # option.add_argument("--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data" % user_file)
            self.driver = webdriver.Chrome()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'ff':
            self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        return self.driver

    def _open(self, url):
        """
        打开url
        :param url: url
        :return: 打开成功/失败
        """
        try:
            self.driver.get(url)
            self.driver.implicitly_wait(10)
        except Exception as e:
            logger_F.exception(e, traceback.print_exc())
            raise ValueError(f'访问 {url} 失败, 请重新输入!')
        else:
            logger_F.info(f'访问 {url} 成功!')

    def open(self):
        self._open(baseUrl)
        logger_F.info(f'{baseUrl} loading success!')
        return baseUrl

    def by_xpath(self, xpath):
        """
        xpath定位元素
        :param xpath: xpath表达式
        :return: 定位到的元素
        """
        try:
            return self.driver.find_element_by_xpath(xpath)
        except:
            logger_F.info(f"页面未定位到 {xpath} 元素!")

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
            logger_F.info(f"根据 {value} 获取句柄失败!")

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
            logger_F.info("鼠标悬停操作失败!")
            return False

    def get_value(self, xpath):
        """
        获取元素内容
        :param xpath:
        :return:
        """
        element = self.by_xpath(xpath)
        value = element.text
        return value

    def j_script(self, src):
        """

        :param src:
        :return:
        """
        try:
            self.driver.excute_script(src)
        except Exception as e:
            logger_F.exception('execute js script [%s] failed ' % src)
            raise e
        else:
            logger_C.info('execute js script [%s] successed ' % src)
