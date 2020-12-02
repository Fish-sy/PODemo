import unittest
from common import log
from pages.basepage import Page

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class MyunitTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        logger_F.info("opened the browser success!")

    def setUp(self) -> None:
        logger_C.info('************************starting run test cases************************')

    def tearDown(self) -> None:
        logger_C.info('************************test case run completed************************')

    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
    #     logger_F.info("quit the browser success!")
