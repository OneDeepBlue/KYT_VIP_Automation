# coding:utf-8
from selenium.webdriver.common.by import By
from po.basepage import BasePage
from po.invoiceOperation.functionList.addInvoicePage import AddInvoicePage
from time import sleep
from po.invoiceOperation.functionList.queryConditions import QueryConditions
from po.invoiceOperation.functionList.deleteInvoice import Deleteinvoice

class operating_invoice(BasePage):
    '''
    数据操作
    '''
    #新增按钮链接
    add_invoice_loc = (By.XPATH,'//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/button[2]')
    #删除按钮
    dele_invoice_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/button[4]')
    #查询按钮
    query_invoice_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/button[1]')
    #重置按钮
    reset_query_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/button[7]')
    #生成托运书按钮
    create_sli_loc = (By.XPATH, '//*[@id="tab1"]/div/ng-include/div/div[1]/div[1]/div/button[5]')
    #关闭提示
    close_hint_loc = (By.ID, 'hintModal-close')

    def add_invoice(self):
        '''
        点击新增按钮
        :return:
        '''
        self.click_element(self.add_invoice_loc)
        sleep(2)
        return AddInvoicePage(self._driver)

    def click_inquire(self):
        '''
        点击查询
        :return:
        '''
        self.click_element(self.query_invoice_loc)
        sleep(2)

    def dele_invoice(self):
        '''
        点击删除按钮
        :return:
        '''
        self.click_element(self.dele_invoice_loc)
        sleep(1)
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

    def choice_data(self,number=1):
        '''
        选择列表数据
        :return:
        '''
        for i in range(1, number+1):
            self.click_element((By.XPATH,
            '//*[@id="tab1"]/div/ng-include/div/div[1]/div[2]/div/div/div[1]/div/table/tbody/tr[%s]'%i))
            sleep(0.5)

    def create_sli(self):
        '''
        点击生成托运书按钮
        :return:
        '''
        self.click_element(self.create_sli_loc)





