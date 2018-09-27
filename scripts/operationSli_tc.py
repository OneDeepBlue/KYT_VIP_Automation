# coding:utf-8

import unittest
from time import sleep
from libs.shareModules import *
from libs.shareBusiness import *

class OperationSli(unittest.TestCase):
    '''
    对托运书的操作：提交、删除、查询等操作
    '''
    def setUp(self):
        self.driver = open_browser()
        self.log = InsertLog()
        #登录系统
        self.menu_administration_page = login_B(self.driver,'lingy','123456')

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def test1_submit_sli(self):
        '''
        选择托运书并提交
        :return:
        '''
        self.log.info(u"执行测试:test1_submit_sli")
        # 展开菜单列表
        self.menu_administration_page.goto_storage()
        click = self.menu_administration_page.goto_submit_sli()
        click.click_inquire()#查询
        click.choice_data()#勾选一条数据
        click.customer_type(u"转出库存")
        click.submit()
        msg = click.page_should_contain(u'提1交成功')
        self.assertEqual(msg, True, u"验证托运书提交结果Fail")
        click.close_hint()
        self.log.info(u"执行测试:test1_submit_sli完成")




