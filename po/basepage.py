# coding:utf-8

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import alert_is_present
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):
    """
    页面类的基类
    """

    def __init__(self, driver):
        self._driver = driver



    def get_element(self, locator):
        """
        获取一个页面元素
        :param locator:
        :return: 页面元素对象
        """
        return self._driver.find_element(*locator)

    def get_elements(self, locator):
        """
        获取一个页面元素
        :param locator:
        :return: 页面元素对象
        """
        return self._driver.find_elements(*locator)

    def input_text(self, locator, text):
        """
        向文本框输入文本
        :param locator: 文本框定位参数
        :param text: 输入的文本内容
        :return: None
        """
        el = self.get_element(locator)
        el.clear()
        el.send_keys(text)

    def click_element(self, locator):
        """
        点击页面元素
        :param locator: 要点击的元素定位参数
        :return: None
        """
        el = self.get_element(locator)
        el.click()

    def select_from_list(self, locator, option_text):
        """
        从下拉列表选择
        :param locator: 下拉列表select元素
        :param option_text: 选项的文本
        :return:
        """
        sel = Select(self.get_element(locator))
        sel.select_by_visible_text(option_text)
        return

    def doubleclick_element(self,locator):
        '''
        双击一个元素
        :param locator: 要操作的元素
        :return: None
        '''
        el = self.get_element(locator)
        ActionChains(self._driver).double_click(el).perform()

    def page_should_contain(self, text):
        """
        验证页面的文本
        :param text:
        :return:  页面包含text,返回True,否则返回False
        """
        xpath = "//*[contains(., '%s')]"%text
        try:
            self._driver.find_element_by_xpath(xpath)
        except: return False
        return True

    def get_alert_message(self, dismiss=False):
        """
        获取页面上JavaScript生成的消息窗
        :param dismiss: True 关闭消息窗，False不关闭
        :return: 消息窗文本内容
        """
        try:
            a = WebDriverWait(self._driver, 5).until(alert_is_present())
            msg = a.text
            if dismiss:
                a.accept()
            return msg
        except: return

    def clear_element(self, locator):
        """
        清空元素（输入框）
        :param locator: 要清空的元素定位参数
        :return: None
        """
        el = self.get_element(locator)
        el.clear()

    def select_radio_checkbox(self, locator):
        """
        选择复选框
        :return:
        """
        el = self.get_element(locator)
        if not el.is_selected():
            el.click()

    def deselect_radio_checkbox(self, locator):
        """
        取消选择复选框
        :return:
        """
        el = self.get_element(locator)
        if el.is_selected():
            el.click()