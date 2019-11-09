import configparser
import os

conf = configparser.RawConfigParser()
# 读取文件
conf.read(os.path.join(os.getcwd(), 'common\\config.ini'))
# 获取账号、密码
username = conf.get("Login", "username")
password = conf.get("Login", "password")

# 获取url
url = conf.get("Address", "base_url")