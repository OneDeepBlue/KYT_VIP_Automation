# coding:utf-8

import unittest
from time import strftime
from HTMLTestRunner import HTMLTestRunner
from libs.shareModules import *

#获取不需要执行的模块名称
ConfigFilePath = "./cofig/config.xlsx"
m = GetSkipScripts(ConfigFilePath)
log = InsertLog()
log.info(u"不需要执行的模块：%s"%m)

#获取不需要执行的用例名称
TestCasePath = u"./cases/KYT_VIP测试用例_V1.0.xlsx"
t = GetSkipTestCases(TestCasePath)
log.info(u"不需要执行的用例：%s"%t)


if __name__ == '__main__':
    try:
        # 从指定目录加载测试用例
        discover = unittest.defaultTestLoader.discover(r"scripts", "*_tc.py")
        #过滤不需要执行的脚本和用例
        suite = get_test_suite(discover,m,t)
        # 创建TestRunner
        runner = unittest.TextTestRunner(verbosity=2)
        t = strftime("%Y%m%d_%H%M%S")
        # filename = "output/report/test_report_%s.txt"%t
        filename = "output/report/test_report_%s.html"%t
        # filename = "output/report/test_report_%s.xls"%t
        pf = open(filename, 'w')
        runner = unittest.TextTestRunner(stream=pf, verbosity=2)
        runner = HTMLTestRunner(stream=pf, verbosity=2, title="【KYT_VIP平台】自动化测试报告", description="描述消息")
        # runner = ExcelTestRunner(stream=filename)
        runner.run(suite)
        pf.close()

    except BaseException as msg:
        log = InsertLog()
        log.error(msg)