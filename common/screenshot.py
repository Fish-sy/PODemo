# -*- coding: utf-8 -*-
# @Author : Mr.sun
# @Time : 2019/12/30 21:20
# @File : screenshot.py

import os
from common.config import conf
from common.log import TestLog

log = TestLog().getlog()
class ScreenCapture(object):

    def saveScreenShot(self, filename):
        list_value = []
        list = filename.split('.')
        for value in list:
            list_value.append(value)
        if list_value[1] == 'png' or list_value[1] == 'jpg' or list_value[1] == 'PNG' or list_value[1] == 'JPG':
            if 'fail' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(conf.failImagePath, filename))
                except Exception:
                    log.exception('save screenshot failed !')
                else:
                    log.info('the %s save screenshot successfully under %s' % (filename, conf.failImagePath))
            elif 'pass' in list_value[0].split('_'):
                try:
                    self.driver.save_screenshot(os.path.join(conf.passImagePath, filename))
                except Exception:
                    log.exception('save screenshot failed !')
                else:
                    log.info('the %s save screenshot successfully under %s' % (filename, conf.passImagePath))
            else:
                log.info('save screenshot failed due to %s format incorrect' % filename)
        else:
            log.info('the file name of %s format incorrect cause save screenshot failed, please check!' % filename)
