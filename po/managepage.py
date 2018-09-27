# coding:utf-8

from selenium.webdriver.common.by import By
from basepage import BasePage
from po.invoiceOperation.operation import operating_invoice
from po.sliSubmit.operation import operating_sli

class ManagePage(BasePage):
    """"
    菜单管理
    """
    #一级菜单：仓储业务链接
    storage_loc = (By.XPATH, '//*[@id="app"]/div[2]/div/div/nav/ul/li[3]/a')
    #二级菜单：发货单录入链接
    invoice_entry_loc = (By.XPATH, '//*[@id="app"]/div[2]/div/div/nav/ul/li[3]/ul/li[2]/a/span')
    #二级菜单：托运书提交
    submit_sli_loc = (By.XPATH, '//*[@id="app"]/div[2]/div/div/nav/ul/li[3]/ul/li[3]/a/span')

    def goto_storage(self):
        '''
        展开仓储业务菜单类表
        :return: None
        '''
        self.click_element(self.storage_loc)


    def goto_invoice_entry(self):
        '''
        打开发货单录入菜单
        :return: 菜单功能操作对象
        '''
        self.click_element(self.invoice_entry_loc)
        return operating_invoice(self._driver)

    def goto_submit_sli(self):
        '''
        打开托运书提交菜单界面
        :return:菜单功能操作对象
        '''
        self.click_element(self.submit_sli_loc)
        return operating_sli(self._driver)



