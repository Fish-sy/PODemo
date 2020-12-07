import sys
from selenium import webdriver
from common import log

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class WDriver(object):

    def chromeDriver(self):
        """
        谷歌浏览器驱动
        :return:
        """
        try:
            self.driver = webdriver.Chrome()
        except Exception as e:
            logger_F.exception('ChromeDriverServer executable needs to be in PATH. Please download!',
                               exc_info=True)
            raise e
        else:
            logger_C.info(f'{sys._getframe().f_code.co_name}:found the Chrome driver {self.driver} success!')
            return self.driver

    def fireFoxDriver(self):
        """
        火狐浏览器驱动
        :return:
        """
        try:
            self.driver = webdriver.Firefox()
        except Exception as e:
            logger_F.exception('FireFoxDriverServer executable needs to be in PATH. Please download!',
                               exc_info=True)
            raise e
        else:
            logger_C.info(f'{sys._getframe().f_code.co_name}:found the FireFox driver {self.driver} success!')
            return self.driver

    def ieDriver(self):
        """
        IE浏览器驱动
        :return:
        """
        try:
            self.driver = webdriver.Ie()
        except Exception as e:
            logger_F.exception('IEDriverServer executable needs to be in PATH. Please download!',
                               exc_info=True)
            raise e
        else:
            logger_C.info(f'{sys._getframe().f_code.co_name}:found the IE driver {self.driver} success!')
            return self.driver


if __name__ == '__main__':
    drive = WDriver()
    drive.chromeDriver()
