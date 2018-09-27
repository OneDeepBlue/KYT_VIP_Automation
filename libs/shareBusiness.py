# coding:utf-8

from selenium import webdriver
from po.loginpage import LoginPage

#-------------------------------------------------------------------------------
# 函数/过程名称：open_browser
# 函数/过程的目的：打开浏览器函数
# 假设：无
# 影响：无
# 输入：无
# 返回值：driver实例对象
# 创建者：lingy
# 创建时间：2018/7/16
# 修改者：
# 修改原因：
# 修改时间:
#-------------------------------------------------------------------------------

url = 'http://113.98.248.185:20000/login.html'

def open_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)#全局等待
    driver.maximize_window()#窗口最大化
    driver.get(url=url)
    return driver

#-------------------------------------------------------------------------------
# 函数/过程名称：login_B
# 函数/过程的目的：登录业务函数
# 假设：无
# 影响：无
# 输入：无
# 返回值：ManagePage实例对象
# 创建者：lingy
# 创建时间：2018/7/16
# 修改者：
# 修改原因：
# 修改时间:
#-------------------------------------------------------------------------------

def login_B(driver,UserName='lingy',PassWord='123456'):
    login_page = LoginPage(driver)
    login_page.input_username(UserName)
    login_page.input_password(PassWord)
    menu_administration_page = login_page.click_login_button()
    return menu_administration_page

if __name__ == "__main__":
    open_browser()
