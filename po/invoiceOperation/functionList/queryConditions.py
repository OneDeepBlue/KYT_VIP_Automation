# coding:utf-8

from selenium.webdriver.common.by import By
from po.basepage import BasePage

class QueryConditions(BasePage):
    '''
    输入查询条件
    '''
    #收货人查询条件输入框
    input_condition_receiver_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[1]/div[4]/input')
    #起始日期
    order_start_date_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[1]/div[1]/span/input[1]')
    #结束日期
    order_end_date_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[1]/div[2]/span/input[1]')
    #状态
    bill_status_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[1]/div[3]/select')
    #运输方式
    transport_type_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[2]/div[1]/select')
    #物控方式
    is_cargo_control_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[2]/div[2]/select')
    #数据来源
    data_source_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[2]/div[3]/select')
    #收货人电话
    re_tel_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[2]/div[4]/input')
    #目的站
    destination_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[3]/div[1]/input')
    #发货单号
    order_no_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[3]/div[2]/input')
    #托运书
    consign_no_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/div[3]/div[3]/input')


    def order_start_date(self,date):
        '''
        清空后输入起始日期
        日期格式：yyyy-MM-dd
        :return:
        '''
        self.clear_element(self.order_start_date_loc)
        self.input_text(self.order_start_date_loc,date)

    def order_end_date(self,date):
        '''
        清空后输入结束日期
        日期格式：yyyy-MM-dd
        :return:
        '''
        self.clear_element(self.order_end_date_loc)
        self.input_text(self.order_end_date_loc,date)

    def bill_status(self,option_text):
        '''
        选择单据状态
        :return:
        '''
        self.select_from_list(self.bill_status_loc,option_text)

    def input_condition_receiver(self,text):
        '''
        输入收货人
        :return:
        '''
        self.input_text(self.input_condition_receiver_loc,text)

    def transport_type(self,option_text):
        '''
        选择运输方式
        :return:
        '''
        self.select_from_list(self.transport_type_loc,option_text)

    def is_cargo_control(self,option_text):
        '''
        选择物控方式
        :return:
        '''
        self.select_from_list(self.is_cargo_control_loc,option_text)

    def data_source(self, option_text):
        '''
        选择数据来源
        :return:
        '''
        self.select_from_list(self.data_source_loc, option_text)

    def re_tel(self,text):
        '''
        输入收货人电话
        :return:
        '''
        self.input_text(self.re_tel_loc,text)

    def destination(self,text):
        '''
        输入目的站
        :return:
        '''
        self.input_text(self.destination_loc,text)


    def order_no(self,text):
        '''
        输入发货单号
        :return:
        '''
        self.input_text(self.order_no_loc,text)


    def consign_no(self,text):
        '''
        输入托运书号
        :return:
        '''
        self.input_text(self.consign_no_loc,text)


