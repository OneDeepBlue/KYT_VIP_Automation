# coding:utf-8

import unittest
from time import sleep
from libs.shareModules import *
from libs.shareBusiness import *

class AddWaybill(unittest.TestCase):
    '''
    创建发货单
    '''
    def setUp(self):
        self.driver = open_browser()
        self.log = InsertLog()
        #登录系统
        self.menu_administration_page = login_B(self.driver,'lingy','123456')

    def tearDown(self):
        sleep(3)
        self.driver.quit()

    def test1_add_invoice(self):
        '''
        正常发货单录入用例
        :return:
        '''
        self.log.info(u"执行测试:test1_add_invoice")
        #展开菜单列表
        self.menu_administration_page.goto_storage()
        click_add = self.menu_administration_page.goto_invoice_entry()
        #进入新增界面
        add_invoice = click_add.add_invoice()
        #填写发货信息
        add_invoice.input_consignee_name(u'张智')
        add_invoice.select_roll_transp(u'汽运')
        add_invoice.select_roll_contro(u'不物控')
        add_invoice.delivery_notes(u'自动化测试录单。。。')
        #打开商品选择窗口
        add_invoice.goods_window()
        sleep(1)
        add_invoice.goods_choice1()
        add_invoice.goods_choice2()
        add_invoice.goods_close()
        #输入商品数量
        add_invoice.goods_number1(10)
        add_invoice.goods_number2(10)
        save_screen_picture(self.driver)#截图
        #保存发货单信息
        add_invoice.invoice_save()
        msg = add_invoice.page_should_contain(u'新增成功')
        self.assertEqual(msg, True, u"验证新增发货单结果Fail")
        self.log.info(u"执行测试：test1_add_invoice结束")
        click_add.close_hint()#关闭提示

    def test2_del_invoice(self):
        '''
        删除发货单
        :return:
        '''
        self.log.info(u"执行测试：test2_del_invoice")
        #展开菜单列表
        self.menu_administration_page.goto_storage()
        operating = self.menu_administration_page.goto_invoice_entry()
        #点击查询按钮
        operating.click_inquire()
        sleep(2)
        #选择第一数据
        operating.choice_data()
        #点击删除并确定删除
        dele = operating.dele_invoice()
        dele.sure_dele()
        #验证是否删除成功
        msg = operating.page_should_contain(u"删除成功")
        self.assertEqual(msg, True, u"验证查询发货单结果Fail")
        self.log.info(u"执行测试：test2_del_invoice结束")
        operating.close_hint()#关闭提示

    def test3_query_invoice(self):
        '''
        输入查询条件查询发货单
        :return:
        '''
        self.log.info(u"执行测试:test3_query_invoice")
        #展开菜单列表
        self.menu_administration_page.goto_storage()
        click_query = self.menu_administration_page.goto_invoice_entry()
        input_query = click_query.input_query()
        #选择查询条件
        input_query.order_start_date('2018-07-03')
        input_query.order_end_date('2018-07-03')
        input_query.bill_status(u"未生成托运书")
        input_query.input_condition_receiver(u"李霞")
        input_query.transport_type(u"空运")
        input_query.is_cargo_control(u"物控")
        input_query.data_source(u"网站创建")
        input_query.re_tel("15953393668")
        input_query.destination(u"东港区")
        input_query.order_no("DD1807037212")
        # input_query.consign_no("TY11111")
        # 点击查询按钮
        click_query.click_inquire()
        #验证查询结果
        msg = click_query.page_should_contain(u"DD1807037212")
        self.assertEqual(msg, True, u"验证查询发货单结果Fail")
        #重置查询条件
        click_query.reset_query()
        self.log.info(u"执行测试:test3_query_invoice结束")

    def test4_create_sli(self):
        '''
        发货单录入后生成托运书
        :return:
        '''
        self.log.info(u"执行测试:test4_create_sli")
        #展开菜单列表
        self.menu_administration_page.goto_storage()
        click = self.menu_administration_page.goto_invoice_entry()
        #进入新增界面
        add_invoice = click.add_invoice()
        #填写发货信息
        add_invoice.input_consignee_name(u'张智')
        add_invoice.select_roll_transp(u'汽运')
        add_invoice.select_roll_contro(u'不物控')
        add_invoice.delivery_notes(u'自动化测试录单。。。')
        #打开商品选择窗口
        add_invoice.goods_window()
        sleep(1)
        add_invoice.goods_choice1()
        add_invoice.goods_choice2()
        add_invoice.goods_close()
        #输入商品数量
        add_invoice.goods_number1(10)
        add_invoice.goods_number2(10)
        #保存发货单信息
        add_invoice.invoice_save()
        click.close_hint()#关闭提示
        #选择数据并点击生成托运书
        click.click_inquire()#点击查询按钮
        click.choice_data(1)
        click.create_sli()
        #验证查询结果
        msg = click.page_should_contain(u"生成托运书成功")
        self.assertEqual(msg, True, u"验证生成托运书结果Fail")
        click.close_hint()#关闭提示
        self.log.info(u"执行测试:test4_create_sli结束")











