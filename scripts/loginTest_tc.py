# coding:utf-8

import unittest
from libs.shareBusiness import *
from time import sleep
from libs.shareModules import *

class LoginTest(unittest.TestCase):


    def setUp(self):
        self.driver = open_browser()
        self.log = InsertLog()

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def test1_login_password_error(self):
        '''
        验证错误密码
        :return:
        '''
        self.log.info("执行测试:test1_login_password_error")
        #登录系统
        menu_administration_page = login_B(self.driver,UserName="lingy",PassWord="1234567")
        msg = menu_administration_page.get_alert_message()
        self.assertEqual(msg, u'密码错误！', u"验证登录结果False")
        self.log.info("执行测试:test1_login_password_error结束")

    def test2_login_account_error(self):
        '''
        验证错误账号
        :return:
        '''
        self.log.info("执行测试:test2_login_account_error")
        #登录系统
        menu_administration_page = login_B(self.driver,UserName="lingy1",PassWord="123456")
        msg = menu_administration_page.get_alert_message()
        self.assertEqual(msg, u'账号错误！', u"验证登录结果False")
        self.log.info("执行测试:test2_login_account_error结束")