# coding:utf-8

from time import sleep
from po.managepage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class AddInvoicePage(BasePage):
    '''
    新增发货单页面
    '''

    #收货人输入框
    consignee_name_loc = (By.XPATH,'//*[@id="InvoiceEntryMain_layer"]/div/div/div[2]/ngform/div[2]/div[1]/input')
    #运输方式
    transp_list_loc = (By.CSS_SELECTOR, '#InvoiceEntryMain_layer > div > div > div.modal-body > ngform > div:nth-child(4) > div:nth-child(2) > select')
    #物控方式
    contro_list_loc =  (By.CSS_SELECTOR, '#InvoiceEntryMain_layer > div > div > div.modal-body > ngform > div:nth-child(4) > div:nth-child(3) > select')
    #备注
    delivery_note_loc = (By.XPATH, '//*[@id="InvoiceEntryMain_layer"]/div/div/div[2]/ngform/div[5]/div/input')
    #货品选择窗口
    goods_window_loc = (By.XPATH, '//*[@id="top"]/tbody/tr')
    #第一个商品
    goods_choice1_loc = (By.XPATH, '//*[@id="InvoiceEntrySelect_layer"]/div/div/div[2]/ngform/div[2]/table/tbody/tr[1]')
    #第二个商品
    goods_choice2_loc = (By.XPATH, '//*[@id="InvoiceEntrySelect_layer"]/div/div/div[2]/ngform/div[2]/table/tbody/tr[2]')
    #选择并关闭
    goods_close_loc = (By.XPATH, '//*[@id="InvoiceEntrySelect_layer"]/div/div/div[3]/button[1]')
    #第一条商品数量输入框
    goods_number1_loc = (By.XPATH, '//*[@id="top"]/tbody/tr[1]/td[10]/input')
    # 第一条商品数量输入框
    goods_number2_loc = (By.XPATH, '//*[@id="top"]/tbody/tr[2]/td[10]/input')
    #保存发货单
    invoice_save_loc = (By.XPATH, '//*[@id="InvoiceEntryMain_layer"]/div/div/div[3]/button[1]')



    def input_consignee_name(self,consignee_name):
        '''
        :param consignee_name: 输入收货人名称+回车键
        :return: None
        '''
        self.input_text(self.consignee_name_loc,consignee_name+Keys.RETURN)

    def select_roll_transp(self,transport):
        """
        选择角色
        :param transport: 要选择的运输方式
        :return: None
        """
        self.select_from_list(self.transp_list_loc,transport)

    def select_roll_contro(self,contro):
        """
        选择物控
        :param contro: 要选择的物控方式
        :return: None
        """
        self.select_from_list(self.contro_list_loc,contro)

    def delivery_notes(self,note):
        '''
        输入备注
        :param note: 输入的备注信息
        :return: None
        '''
        self.input_text(self.delivery_note_loc,note)

    def goods_window(self):
        '''
        双击弹出货品选择窗口
        :return:
        '''
        self.doubleclick_element(self.goods_window_loc)
    def goods_choice1(self):
        '''
        选中第一条商品信息
        :return:
        '''
        self.click_element(self.goods_choice1_loc)

    def goods_choice2(self):
        '''
        选中第二条商品信息
        :return:
        '''
        self.click_element(self.goods_choice2_loc)

    def goods_close(self):
        '''
        点击选择并关闭按钮
        :return:
        '''
        self.click_element(self.goods_close_loc)

    def goods_number1(self,number):
        '''
        输入第一条商品的数量
        :return:
        '''
        self.input_text(self.goods_number1_loc,number)

    def goods_number2(self,number):
        '''
        输入第二条商品的数量
        :return:
        '''
        self.input_text(self.goods_number2_loc,number)

    def invoice_save(self):
        '''
        点击保存按钮，保存发货单
        :return:
        '''
        self.click_element(self.invoice_save_loc)
        sleep(3)





