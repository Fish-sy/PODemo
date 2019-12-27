import logging
import os
import configparser
# from pages.models.log import TestLog
from common import conf


log = logging.Logger(__name__)
class DoConfig(object):

    def __init__(self):
        self.config = configparser.ConfigParser()

    def getConfValue(self, filename, section, option):
        try:
            self.config.read(filename)
            value = self.config.get(section, option)
        except Exception as e:
            log.error('read file [%s] for [%s] failed , did not get the value' % (filename, section))
            raise e
        else:
            log.error('read config value [%s] success!' % value)
            return value


if __name__ == '__main__':
    read_config = DoConfig()
    value = read_config.getConfValue(os.path.join(conf.curPath, 'config.ini'), 'project', 'project_path')
    print(value)
