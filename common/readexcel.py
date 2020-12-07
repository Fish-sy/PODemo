import xlrd
import os
from common import log
from common.config import conf

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class ReadExcel(object):

    def __init__(self, filename='elementDate.xlsx', sheetname='elementsInfo'):
        """
        初始workBook
        :param filename: Excel文件名
        :param sheetname: 文件sheet名
        """
        try:
            self.excelFile = os.path.join(conf.excelPath, filename)
            self.workBook = xlrd.open_workbook(self.excelFile)
            self.sheetName = self.workBook.sheet_by_name(sheetname)
        except Exception:
            logger_F.exception('初始workBook失败!', exc_info=True)
            raise
        else:
            logger_F.info('正在初始workBook!')

    def read_excel(self, rownum, colnum):
        """
        读取Excel
        :param rownum: 行
        :param colnum: 列
        :return:
        """
        try:
            value = self.sheetName.cell(rownum, colnum).value
        except Exception:
            logger_F.exception('读取Excel失败!', exc_info=True)
            raise
        else:
            logger_F.info(f'在 {self.excelFile} 中读取 {value} 成功')
            return value


if __name__ == '__main__':
    value = ReadExcel().read_excel(0, 1)
    print(value)
