# coding:utf-8

from selenium.webdriver.common.by import By
from managepage import ManagePage
from selenium import webdriver
from basepage import BasePage
from time import sleep

class LoginPage(BasePage):
    """
    登录页面
    """

    # 用户名输入框
    username_loc = (By.ID, "user_no")
    # 密码输入框
    password_loc = (By.ID, "password")
    # 登录按钮
    login_btn_loc = (By.CSS_SELECTOR, "#loginform > div > div:nth-child(4) > a")


    def input_username(self, username):
        """输入用户名"""
        self.input_text(self.username_loc, username)

    def input_password(self, password):
        """输入密码"""
        self.input_text(self.password_loc, password)

    def click_login_button(self):
        '''
        点击登录按钮
        :return: ManagePage
        '''
        self.click_element(self.login_btn_loc)
        return ManagePage(self._driver)


if __name__ == '__main__':
    url = 'http://113.98.248.185:8086/WebProject/syslogin.jsp'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(url=url)
    login_page = LoginPage(driver)
    login_page.input_username('simon')
    login_page.input_password('123456')

    sleep(2)
    driver.quit()