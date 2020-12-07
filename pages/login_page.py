from pages.basepage import BasePage
from pages.basepage import eleData
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    """用户名，密码，验证码，登录按钮，错误提示，注册按钮"""
    userNameEle = (By.ID, eleData.readExcel(2, 3))
    passWordEle = (By.ID, eleData.readExcel(3, 3))
    verifyCode = (By.ID, eleData.readExcel(4, 3))
    loginBtn = (By.NAME, eleData.readExcel(5, 3))
    errorMessage = (By.XPATH, eleData.readExcel(6, 3))
    signInBtn = (By.XPATH, eleData.readExcel(7, 3))


