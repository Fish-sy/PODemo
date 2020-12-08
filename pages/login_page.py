# coding = utf-8
from common import log
from pages.basepage import BasePage
from pages.basepage import eleData
from common.readexcel import ReadExcel

logger_F = log.logging.getLogger('F')
logger_C = log.logging.getLogger('C')


class LoginPage(BasePage):

    """用户名，密码，验证码，登录按钮，错误提示，注册按钮"""
    userNameEle = (eleData.readExcel(2, 3))
    passWordEle = (eleData.readExcel(3, 3))
    verifyCode = (eleData.readExcel(4, 3))
    loginBtn = (eleData.readExcel(5, 3))
    errorMessage = (eleData.readExcel(6, 3))
    signInBtn = (eleData.readExcel(7, 3))

    testLoginData = ReadExcel("elementDate.xlsx", "loginData")
    # 登录场景测试数据
    loginData = [
        [testLoginData.read_excel(1, 0), testLoginData.read_excel(1, 1), testLoginData.read_excel(1, 2)],
        [testLoginData.read_excel(2, 0), testLoginData.read_excel(2, 1), testLoginData.read_excel(2, 2)],
        [testLoginData.read_excel(3, 0), testLoginData.read_excel(3, 1), testLoginData.read_excel(3, 2)],
        [testLoginData.read_excel(4, 0), testLoginData.read_excel(4, 1), testLoginData.read_excel(4, 2)],
        [testLoginData.read_excel(5, 0), testLoginData.read_excel(5, 1), testLoginData.read_excel(5, 2)],
        [testLoginData.read_excel(6, 0), testLoginData.read_excel(6, 1), testLoginData.read_excel(6, 2)],
        [testLoginData.read_excel(7, 0), testLoginData.read_excel(7, 1), testLoginData.read_excel(7, 2)],
        [testLoginData.read_excel(8, 0), testLoginData.read_excel(8, 1), testLoginData.read_excel(8, 2)],
        [testLoginData.read_excel(9, 0), testLoginData.read_excel(9, 1), testLoginData.read_excel(9, 2)],
        [testLoginData.read_excel(10, 0), testLoginData.read_excel(10, 1), testLoginData.read_excel(10, 2)],
    ]

    def login_fun(self, username='13800138006', password='123456', verify='1'):
        """
        统一登录函数
        :param username: 用户名
        :param password: 密码
        :param verify: 验证码
        :return:
        """
        self.input(self.userNameEle, username)
        self.input(self.passWordEle, password)
        self.input(self.verifyCode, verify)
        self.click(self.loginBtn)

    def get_fail_text(self):
        """
        登录失败时提示信息
        :return:
        """
        info = self.get_value(self.errorMessage)
        logger_F.info(f"login failed : {info}")
        return info


if __name__ == '__main__':
    pass
