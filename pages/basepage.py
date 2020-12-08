# coding = utf-8
import time
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

    # def open_browser(self, browser='gc'):
    #     """
    #     打开浏览器
    #     :param browser: 默认使用谷歌驱动调用谷歌浏览器
    #     :return: 打开成功
    #     """
    #     if browser == 'gc':
    #         # 使用缓存加载页面
    #         # option = Options()
    #         # user_file = os.environ["USERPROFILE"]
    #         # option.add_argument("--user-data-dir=%s\\AppData\\Local\\Google\\Chrome\\User Data" % user_file)
    #         self.driver = webdriver.Chrome()
    #     elif browser == 'ie':
    #         self.driver = webdriver.Ie()
    #     elif browser == 'ff':
    #         self.driver = webdriver.Firefox()
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #     return self.driver

    def _open(self, url):
        """

        :param url:
        :return:
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
        """
        调用_open函数访问baseUrl
        :return:
        """
        self._open(baseUrl)
        logger_F.info(f'{baseUrl} loading success!')
        return baseUrl

    def get_title(self):
        """
        获取当前窗口title
        :return:
        """
        return self.driver.title

    def click(self, locator):
        """
        点击操作
        :param locator:
        :return:
        """
        element = self.__find_element(locator)
        element.click()

    def click_href(self, locator):
        """
        通过定位器找到a标签元素，然后获取到href连接，进行跳转
        主要是处理IE点击失败的情况
        :param locator: 元素
        :return:
        """
        ele = self.__find_element(locator)
        if ele is None:
            return False

        try:
            href = ele.get_attribute('href')
            self.driver.get(href)
            return True
        except Exception as e:
            logger_F.exception(e, exc_info=True)

    def input(self, locator, text):
        """
        清除输入框后输入内容
        :param locator:
        :param text: 输入的文本
        :return:
        """
        element = self.__find_element(locator)
        element.clear()
        element.send_keys(text)

    def sleep(self, t=1):
        """
        强制睡眠
        :param t: 睡眠时间，默认1秒
        :return:
        """
        time.sleep(int(t))

    def close(self):
        """关闭当前窗口"""
        self.driver.close()

    def quit(self):
        """退出浏览器"""
        self.driver.quit()

    def submit(self, locator):
        """提交"""
        element = self.__find_element(locator)
        element.submit()

    def handle(self, value):
        """句柄切换"""
        try:
            handles = self.driver.window_handles
            self.driver.switch_to.window(handles[value])
        except:
            logger_F.info(f"failed to get handle based on {value} !", exc_info=True)

    def to_frame(self, locator):
        """内联框架"""
        element = self.__find_element(locator)
        self.driver.switch_to.frame(element)

    def back(self):
        """返回到旧的窗口"""
        self.driver.back()

    def forward(self):
        """前进到新窗口"""
        self.driver.forward()

    def mouse_hover(self, locator):
        """鼠标悬停"""
        try:
            element = self.__find_element(locator)
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            logger_F.info("mouse over operation failed!", exc_info=True)
            return False

    def get_value(self, locator):
        """
        获取元素内容
        :param locator:
        :return:
        """
        element = self.__find_element(locator)
        value = element.text
        return value

    def j_script(self, src):
        """
        点击a标签，针对selenium点击不了的情况
        （点击a标签触发js事件的，JavaScript:void(0);）
        :param src:
        :return:
        """
        try:
            self.driver.excute_script(src)
        except Exception as e:
            logger_F.exception(f'execute js script {src} failed')
            raise e
        else:
            logger_C.info(f'execute js script {src} successed')

    def __find_element(self, locator):
        """
        通过定位器查找元素
        :param locator: xpath
        :return: 返回找到的元素
        """
        try:
            if locator.startswith("id="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_id(locator)
            elif locator.startswith("xpath="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_xpath(locator)
            elif locator.startswith("name="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_name(locator)
            elif locator.startswith("linktext="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_link_text(locator)
            elif locator.startswith("css="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_css_selector(locator)
            elif locator.startswith("class="):
                locator = locator[locator.find('=') + 1:]
                element = self.driver.find_element_by_class_name(locator)
            else:
                element = self.driver.find_element_by_xpath(locator)
        except Exception as e:
            logger_F.exception('finding element timeout!', exc_info=True)
            raise e
        else:
            return element
