import xlrd
import os
from common import log
from common.config import conf

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class ReadExcel(object):

    def __init__(self, fileName='elementDate.xlsx', sheetName='elementsInfo'):
        """
        初始workBook
        :param fileName: Excel文件名
        :param sheetName: 文件sheet名
        """
        try:
            self.excelFile = os.path.join(conf.excelPath, fileName)
            self.workBook = xlrd.open_workbook(self.excelFile)
            self.sheetName = self.workBook.sheet_by_name(sheetName)
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
    cellValue = ReadExcel().read_excel(6, 4)
    print(cellValue)
