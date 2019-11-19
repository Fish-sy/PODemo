import os
import time
import logging


class TestLog(object):
    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入log
        self.log_time = time.strftime('%Y-%m-%d')
        self.log_path = os.path.join(os.path.abspath(os.path.dirname(os.getcwd()) + "\\report\\" + "\\Log\\" + "log"))
        self.log_name = self.log_path + self.log_time + '.log'

        # 日志输出格式
        formatter = logging.Formatter('[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')

        # 设置文件输出
        fh = logging.FileHandler(self.log_name, 'w')
        fh.setFormatter(formatter)
        fh.setLevel(logging.INFO)

        """
            # 设置控制台输出
            sh = logging.StreamHandler()
            sh.setFormatter(formatter)
            sh.setLevel(logging.INFO)
        """

        # 给logger添加handler
        self.logger.addHandler(fh)
        # self.logger.addHandler(sh)

        fh.close()

    def getlog(self):
        return self.logger
