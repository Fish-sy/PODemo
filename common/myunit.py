import unittest
from common import log
from common.driver import WDriver
from pages.login_page import LoginPage

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        """

        :return:
        """
        cls.driver = WDriver().chromeDriver()
        cls.driver.maximize_window()
        logger_F.info("opened the browser success!")

    def setUp(self) -> None:
        """

        :return:
        """
        self.login = LoginPage(self.driver)
        self.login.open()
        logger_C.info('************************starting run test cases************************')

    def tearDown(self) -> None:
        """

        :return:
        """
        self.driver.refresh()
        logger_C.info('************************test case run completed************************')

    @classmethod
    def tearDownClass(cls) -> None:
        """

        :return:
        """
        cls.driver.quit()
        logger_F.info("quit the browser success!")
