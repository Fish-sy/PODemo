# coding = utf-8
import os
from common.readconfig import DoConfig


# 获取当前路径
curPath = os.path.split(os.path.realpath(__file__))[0]

# 读配置文件获取项目路径
readconf = DoConfig()
proPath = readconf.getConfValue(os.path.join(curPath, 'config.ini'), 'project', 'project_path')

# 保存截图路径
imagePath = os.path.join(proPath, "report", "Image")

# 测试报告路径
reportPath = os.path.join(proPath, "report", "TestReport")

# 日志路径
logPath = os.path.join(proPath, "report", "Log")

