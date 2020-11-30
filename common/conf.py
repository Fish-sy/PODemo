# coding = utf-8
import os
from common import readconfig


# 获取当前路径
curPath = os.path.split(os.path.realpath(__file__))[0]
curr = os.path.realpath(__file__)
print(curPath)

# 读配置文件获取项目路径
readconf = readconfig.DoConfig()
proPath = readconf.getConfValue(os.path.join(curPath, 'config.ini'), 'project', 'project_path')
print(proPath)

# 保存截图路径
ImagePath = os.path.join(proPath, "report", "Image")
"""错误截图"""
failImagePath = os.path.join(ImagePath, "fail")
"""正确截图"""
passImagePath = os.path.join(ImagePath, "pass")

# 保存测试报告路径
reportPath = os.path.join(proPath, "report", "TestReport\\")

# 保存日志路径
logPath = os.path.join(proPath, "report", "Log\\")

# 测试数据路径
dataPath = os.path.join(proPath, "testcase", "testdata\\")
