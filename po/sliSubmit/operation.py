# coding:utf-8
from selenium.webdriver.common.by import By
from po.basepage import BasePage
from time import sleep
from po.invoiceOperation.functionList.queryConditions import QueryConditions
from po.invoiceOperation.functionList.deleteInvoice import Deleteinvoice

class operating_sli(BasePage):
    '''
    数据操作
    '''
    #删除按钮
    dele_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[1]/div/button[4]')
    #查询按钮
    query_invoice_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[1]/div/button[1]')
    #重置按钮
    reset_query_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[1]/div/button[6]')
    #提交按钮
    submit_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[1]/div/button[3]')
    #关闭提示
    close_hint_loc = (By.ID, 'hintModal-close')
    #勾选第一条数据
    choice_data1_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[2]/input')
    #勾选第二条数据
    choice_data2_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[2]/td[2]/input')
    #选择操作类型
    customer_type_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div/div[2]/div/div/div[1]/div/table/tbody/tr[1]/td[7]/select')

    def click_inquire(self):
        '''
        点击查询
        :return:
        '''
        self.click_element(self.query_invoice_loc)
        sleep(2)

    def dele(self):
        '''
        点击删除按钮
        :return:
        '''
        sleep(1)
        self.click_element(self.dele_loc)
        return Deleteinvoice(self._driver)

    def input_query(self):
        '''
        查询条件
        :return:返回查询条件操作
        '''
        return QueryConditions(self._driver)

    def reset_query(self):
        '''
        点击重置按钮
        :return:
        '''
        self.click_element(self.reset_query_loc)

    def close_hint(self):
        '''
        点击关闭提示
        :return:
        '''
        self.click_element(self.close_hint_loc)
        sleep(1)

    def choice_data(self):
        '''
        勾选列表数据
        :return:
        '''
        self.select_radio_checkbox(self.choice_data1_loc)
        sleep(1)

    def customer_type(self,type):
        '''
        选择操作类型
        :return:
        '''
        self.select_from_list(self.customer_type_loc,type)

    def submit(self):
        '''
        点击提交按钮
        :return:
        '''
        self.click_element(self.submit_loc)









