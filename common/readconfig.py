from common import log
import configparser

logger_F = log.logging.getLogger('F')


class DoConfig:

    def __init__(self):
        self.config = configparser.ConfigParser()

    def getConfValue(self, filename, section, name):
        """
        获取文件内容
        :param filename: 要读取的文件
        :param section: 字段名
        :param name: section的键
        :return: section的值
        """
        try:
            self.config.read(filename, encoding='utf-8')
            value = self.config.get(section, name)
        except Exception as e:
            logger_F.info(f'读取 {filename} 中的 {section} 失败,获取不到 {value}')
            logger_F.error(e)
        else:
            logger_F.info(f'读取 {value} 成功!')
            return value


if __name__ == '__main__':
    read_config = DoConfig()
    value = read_config.getConfValue('mysql', 'mysql_db1')
    print(value)
