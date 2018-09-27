# coding:utf-8
from selenium.webdriver.common.by import By
from po.managepage import BasePage

class Deleteinvoice(BasePage):
    '''
    是否删除
    '''

    #确定删除
    sure_dele_loc  = (By.XPATH, '//*[@id="confirmModal-save"]')
    #取消删除
    cancel_dele_loc = (By.XPATH, '//*[@id="confirmModal-cancel"]')


    def sure_dele(self):
        '''
        点击确定删除按钮
        :return:
        '''
        self.click_element(self.sure_dele_loc)

    def cancel_dele(self):
        '''
        点击取消删除按钮
        :return:
        '''
        self.click_element(self.cancel_dele_loc)